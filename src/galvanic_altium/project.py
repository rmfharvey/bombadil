import re
import logging
from uuid import uuid4

from galvanic import colored_logger
from galvanic_altium.utils import validate_json_serialization, AltiumBasic
from galvanic_altium.schematic import SchematicSheet, Net, NET_SCOPE
from galvanic_altium.server_api import AltiumServerAPI

# TODO somehow get controller name from Altium Project metadata


class AltiumBom:
    def __init__(self, component_dict, bom_metadata, parent):
        self._parent = parent
        self.components = {}
        for c in bom_metadata["systemBom"]["items"]:
            cmp = self._parent.get_component(c["designator"])
            cmpid = c["libRef"]
            if cmpid not in self.components:
                self.components[cmpid] = []
            self.components[cmpid].append(cmp)
        self.components_by_pn
        self.components_by_type
        self.components_by_designator

    @property
    def total_parts(self):
        return sum(map(len, self.components.values()))

    @property
    def unique_parts(self):
        return len(self.components.values())

    # Useful properties for sorting/indexing components
    @property
    def components_by_pn(self):
        components = {}
        for design_item_id, c_list in self.components.items():
            if len(c_list[0].avl):
                key = c_list[0].avl[0][1]  # Get first PN in AVL
            else:
                key = design_item_id
            components[key] = c_list
        return components

    @property
    def components_by_type(self):
        by_type = {}

        def get_leading_alpha(text):
            match = re.match(r"^[a-zA-Z]+", text)
            return match.group() if match else None

        for des, c in self._parent.components.items():
            alpha = get_leading_alpha(des)
            if alpha not in by_type:
                by_type[alpha] = {}
            by_type[alpha][des] = c
        return by_type

    @property
    def components_by_designator(self):
        return self._parent.components


class AltiumProject(AltiumBasic):
    def __init__(self, guid):
        """

        :param str guid: Project unique id
        """
        self.logger = colored_logger(__file__, level=logging.DEBUG)

        self.bom = None
        self.pcb = None
        self.project = None
        self.schematics = None
        self.components = {}
        self.nets = {}

        self._guid = guid
        self._raw_metadata = AltiumServerAPI.get_project(self._guid)["data"]

        self._extract_file_metadata()
        self._raw_metadata["bom"] = AltiumServerAPI.get_project_bom(self._guid, skip_live_data=False)

        self.create_project_level_components_and_nets()
        self.bom = AltiumBom(component_dict=self.components, bom_metadata=self._raw_metadata["bom"], parent=self)

    def create_project_level_components_and_nets(self):
        for sch in self.schematics.values():
            for c in sch.components.values():
                try:
                    assert (
                        c.designator not in self.components
                    ), f"Component designator ({c.designator}) already exists.  Marking as duplicate."
                    designator = c.designator
                except AssertionError as err:
                    self.logger.error(err)
                    designator = f"{c.designator}_{uuid4()}"
                self.components[designator] = c

            for local_net in sch.nets.values():
                # Create new global net if needed, else use existing
                if local_net.name not in self.nets:
                    global_net = Net(metadata=None, parent=self, name=local_net.name, scope=NET_SCOPE.GLOBAL)
                else:
                    global_net = self.nets[local_net.name]

                # Iterate through all connected components in local net and add pins if needed
                for des, pins in local_net.connected_pins.items():
                    if des not in global_net.connected_pins:
                        global_net.connected_pins[des] = pins
                    else:
                        global_net.connected_pins[des] += pins
                        global_net.connected_pins[des] = list(set(global_net.connected_pins[des]))

                self.nets[local_net.name] = global_net

    def get_component(self, designator):
        cmp = self.components.get(designator)
        if not cmp:
            self.logger.warning(f"Could not find component {designator} in project {self.project.name}")
        return cmp

    @validate_json_serialization
    def get_config(self):
        config = {
            # "bom": self.bom,
            "guid": self._guid,
            # "pcb": self.pcb,
            # "project": self.project,
            "schematics": {k: v.get_config() for k, v in self.schematics.items()},
            "components": {k: v.get_config() for k, v in self.components.items()},
            "nets": {k: v.get_config() for k, v in self.nets.items()},
        }
        return config

    def _extract_file_metadata(self):
        """Create class objects from each file type"""
        _FILE_TYPE_MAPPING = {
            "PrjMetadata": {"type": "project", "class": None},
            "SchMetadata": {"type": "schematics", "class": SchematicSheet},
            "PcbMetadata": {"type": "pcb", "class": None},
        }
        objs = {}
        for f in self._raw_metadata["files"]:
            mapping = _FILE_TYPE_MAPPING.get(f["fileType"])
            if mapping:
                if mapping["type"] not in objs:
                    objs[mapping["type"]] = {}

                cls = mapping["class"]

                filename = f["originalName"]
                url = f["dataFileUrl"]
                self.logger.info(f"Downloading {filename} from {url}")
                metadata = AltiumServerAPI.download_json_from_url(url)
                if cls:
                    obj = cls(metadata)
                else:
                    obj = metadata
                name = filename[: filename.index(".")]
                objs[mapping["type"]][name] = obj

        # Add newly create objects to class
        for obj_type, obj in objs.items():
            assert hasattr(self, obj_type)  # Ensure the object type exists
            if len(obj) == 1:
                obj = list(obj.values())[0]
                self.logger.info(f"{obj_type} container only has one member.  Flattenning.")
            setattr(self, obj_type, obj)
        return objs
