import logging
from galvanic import colored_logger

from galvanic_altium.constants_and_enums import PRIMITIVE
from galvanic_altium.utils import validate_json_serialization, AltiumBasic

logger = colored_logger(__file__, level=logging.DEBUG)


class NET_SCOPE:
    LOCAL = "Local"
    GLOBAL = "Global"


class Pin(AltiumBasic):
    def __init__(self, metadata):
        self._meta = metadata
        self.name = self._meta["name"]
        self.connected_net = None
        self.number = self._meta["hash"].split("|")[1]

    @validate_json_serialization
    def get_config(self):
        config = {
            "name": self.name,
            "number": self.number,
            "connected_net": self.connected_net.name if self.connected_net else None,
        }
        return config

    def __finalize_loading(self, parent):
        net_name = self.connected_net
        if not isinstance(net_name, str):
            logger.warning(f"Could not find net for pin {self.name} in {parent.name}")
            return False
        self.connected_net = parent.nets[net_name]


class Net(AltiumBasic):
    def __init__(self, metadata, parent, name=None, scope=NET_SCOPE.LOCAL):
        self._meta = metadata
        self.connected_pins = {}
        self._scope = scope
        self._parent = parent
        self.name = name
        if self._meta is not None:
            self.name = self._meta["name"]
            self.connected_pins = self.find_connected_pins()

    def find_connected_pins(self):
        connected_pins = {}
        for primitive_id in self._meta["primitives"]:
            primitive = self._parent.get_primitive(primitive_id)
            if primitive["kind"] != PRIMITIVE.PIN:
                continue
            # Get the component designator and pin name
            component, pin = primitive["fullName"].split("-")

            # Add to pin to connecte_pins dictionary
            if component not in connected_pins:
                connected_pins[component] = []
            connected_pins[component].append(pin)
        return connected_pins

    @validate_json_serialization
    def get_config(self):
        config = {
            "connected_pins": {k: v for k, v in self.connected_pins.items()},
            "_scope": self._scope,
            "name": self.name,
        }
        return config

    @property
    def scope(self):
        return self._scope


class Component(AltiumBasic):
    _MAX_AVL_LENGTH = 3

    def __init__(self, metadata, parent):
        self._meta = metadata
        self._parent = parent
        self.designator, __ = self.split_logical_physical_designators(self._meta["designator"])
        self.parameters = {p["name"]: p["value"] for p in self._meta["parameters"]}
        self.avl = self.compile_avl()
        self.pins = self.extract_pins()

    def compile_avl(self):
        avl = []
        for i in range(1, self._MAX_AVL_LENGTH + 1):
            mfg = self.parameters.pop(f"Manufacturer {i}", None)
            pn = self.parameters.pop(f"Manufacturer {i} PN", None)
            if all([mfg, pn]):
                avl.append((mfg, pn))
        return avl

    def extract_pins(self):
        pins_dict = {}
        for pid in self._meta["primitives"]:
            prm = self._parent.get_primitive(pid)
            if not PRIMITIVE.PIN:
                continue
            pin = Pin(prm)
            assert pin.number not in pins_dict
            pins_dict[pin.number] = pin
        return pins_dict

    @validate_json_serialization
    def get_config(self):
        config = {
            "avl": self.avl,
            "designator": self.designator,
            "parameters": self.parameters,
            "pins": {k: v.get_config() for k, v in self.pins.items()},
            "_MAX_AVL_LENGTH": self._MAX_AVL_LENGTH,
        }
        return config

    @staticmethod
    def split_logical_physical_designators(designator):
        """Split a designator into logical and physical components."""
        try:
            logical, physical = designator.replace(")", "").split("(")
            return logical.strip(), physical.strip()
        except ValueError as err:
            logger.warning(f"Could not perform logical/physical split on designator {designator}")
            return designator, None

    @property
    def has_avl(self):
        return len(self.avl) > 0


class SchematicSheet(AltiumBasic):
    def __init__(self, metadata):
        self._meta = metadata

        self._reformat_metadata()

        self.filename = self._meta["schDocuments"][0]["originalFileName"]
        self.name = self.filename.replace(".SchDoc", "")
        self.nets = self.create_nets(self._meta["nets"])
        self.components = self.create_components(self._meta["components"])

        self.link_nets_to_pins()

    def link_nets_to_pins(self):
        """Iterate through all nets and register their connection to the appropriate pins."""
        for net in self.nets.values():
            for des, pins in net.connected_pins.items():
                target_component = self.components[des]
                for pin in pins:
                    target_component.pins[pin].connected_net = net

    def create_nets(self, metadata):
        return {n["name"]: Net(n, self) for n in metadata}

    def create_components(self, metadata):
        components = {}
        for c in metadata:
            c_obj = Component(c, self)
            # assert c_obj.designator not in components
            components[c_obj.designator] = c_obj
        return components

    def get_primitive(self, id):
        prm = self._indexed_primitives.get(id)

        return prm

    def _reformat_metadata(self):
        ### Index primitives
        self._indexed_primitives = {p["id"]: p for p in self._meta["primitives"]}
        assert len(self._indexed_primitives) == len(self._meta["primitives"])

    @validate_json_serialization
    def get_config(self):
        config = {
            # "components": {k: v.get_config() for k, v in self.components.items()},
            "components": {k: v.designator for k, v in self.components.items()},
            "filename": self.filename,
            "name": self.name,
            "nets": {k: v.name for k, v in self.nets.items()},
        }
        return config

    def __finalize_loading(self, parent):
        for des, c in self.components.items():
            component = parent.components[des]
            self.components[des] = component
        for name, net in self.components.items():
            net = parent.nets[name]
            self.nets[name] = net
