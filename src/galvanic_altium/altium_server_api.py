import json
import requests
import logging
import os
from uuid import uuid4
from galvanic import colored_logger

from galvanic_altium.utils import validate_json_serialization, AltiumBasic
from galvanic_altium.schematic import SchematicSheet, Net, NET_SCOPE


logger = colored_logger(__file__, level=logging.DEBUG)


class AltiumServerAPI:
    @staticmethod
    def load_urls(base_url, api_url):
        AltiumServerAPI.BASE_URL = base_url
        AltiumServerAPI.API_URL = api_url

    @staticmethod
    def get_project_list(query=""):
        params = {
            "query": query,
            "orderBy": "modified",
            "order": "desc",
            "page": "0",
            "pageSize": "20",
        }
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "app": "Explorer",
            "authorization": f"AFSSessionID {os.environ['ALTIUM_TOKEN']}",
        }
        response = requests.get(
            f"{AltiumServerAPI.BASE_URL}/svc/explorer/api/v1/entities",
            params=params,
            headers=headers,
        )
        return json.loads(response.content)["entities"]

    @staticmethod
    def get_project(guid):
        headers = {"x-auth": os.environ["ALTIUM_TOKEN"]}

        response = requests.get(
            f"{AltiumServerAPI.API_URL}/widget/get/data/{guid}",
            headers=headers,
        )
        return json.loads(response.content)

    @staticmethod
    def get_project_bom(guid, skip_live_data=True):
        headers = {"x-auth": os.environ["ALTIUM_TOKEN"]}

        params = {
            "skipLiveData": str(skip_live_data).lower(),
        }

        response = requests.get(
            f"{AltiumServerAPI.API_URL}/design/bom/{guid}",
            params=params,
            headers=headers,
        )
        return json.loads(response.content)

    @staticmethod
    def download_json_from_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            logger.error(f"Failed to download from {url}")
            return False


class AltiumProject(AltiumBasic):
    def __init__(self, guid):
        """

        :param str guid: Project unique id
        """

        self.bom = None
        self.pcb = None
        self.project = None
        self.schematics = None
        self.components = {}
        self.nets = {}

        self._guid = guid
        self._raw_metadata = AltiumServerAPI.get_project(self._guid)["data"]

        self._extract_file_metadata()
        self.bom = AltiumServerAPI.get_project_bom(self._guid, skip_live_data=False)

        self.create_project_level_components_and_nets()

    def create_project_level_components_and_nets(self):
        for sch in self.schematics.values():
            for c in sch.components.values():
                try:
                    assert (
                        c.designator not in self.components
                    ), f"Component designator ({c.designator}) already exists.  Marking as duplicate."
                    designator = c.designator
                except AssertionError as err:
                    logger.error(err)
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
                logger.info(f"Downloading {filename} from {url}")
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
                logger.info(f"{obj_type} container only has one member.  Flattenning.")
            setattr(self, obj_type, obj)
        return objs
