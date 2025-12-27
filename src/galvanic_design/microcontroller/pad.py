from __future__ import annotations
import typing
from galvanic_design.base_objects import BaseObject
from galvanic.ui.microcontroller.pad_widget import PadWidget, PadListWidget

if typing.TYPE_CHECKING:
    from galvanic_design.microcontroller.microcontroller import Microcontroller


class PadFunction:
    direction: str
    open_drain_capable: bool = False
    peripheral_instance: str
    peripheral_name: str
    peripheral_subusage: str | None = None

    def __init__(self, function_dict):
        self._info = function_dict

        self.direction = function_dict["direction"]
        self.peripheral_instance = function_dict["peripheral_instance"]
        self.peripheral_name = function_dict["peripheral_name"]
        self.peripheral_subusage = function_dict["peripheral_subusage"]
        self.open_drain_capable = function_dict.get("open_drain_capable", False)

    @property
    def function_name(self):
        fname = f"{self.peripheral_name}{self.peripheral_instance}"
        if self.peripheral_subusage:
            fname = f"{fname}_{self.peripheral_subusage}"
        return fname


class PadFunctions:
    def __init__(self, functions):
        self.functions = [PadFunction(f) for f in functions]

    def get_function_by_name(self, name):
        return self.as_dict.get(name)

    def check_validity(self, f):
        name_match = f in self.as_dict.keys()
        obj_match = f in self.functions
        valid = name_match or obj_match or (f is None)
        return valid

    @property
    def as_dict(self):
        return {f.function_name: f for f in self.functions}


class Pad(BaseObject):
    WIDGET_CLASS = PadWidget

    def __init__(
        self,
        pad_name: str = None,
        functions: list = [],
        net_name: str = None,
        current_function: str = None,
        create_ui: bool = False,
        parent_micro: Microcontroller = None,
    ):
        super().__init__(name=pad_name)

        self.parent_micro = parent_micro
        self.functions = PadFunctions(functions)
        self.net_name = net_name

        self.current_function = None
        self.set_function(current_function)

        if create_ui:
            self.ui_object = self.create_ui_element()

    def load_config(self, config):
        config = self._resolve_config_path(config)
        self.functions = PadFunctions(config.pop("functions", []))
        self._load_dict_values(config)
        self.ui_object = self.create_ui_element()

    def set_function(self, function: str = None):
        try:
            valid_function = self.functions.check_validity(function)
            assert valid_function, f"'{function}' not in available functions."
            self.current_function = function
            return True
        except AssertionError as err:
            self.logger.warning(err)
            return False

    @property
    def pad_name(self):
        return self.name

    @pad_name.setter
    def pad_name(self, value):
        assert isinstance(value, str), "Pad name must be a string"
        self.name = value

    @property
    def pin_name(self):
        # TODO retrieve associated based on package in parent micro
        return None


class PadList(BaseObject):
    WIDGET_CLASS = PadListWidget

    def __init__(self, pads):
        self.pads = {k: Pad.from_config(v) for k, v in pads.items()}
        super().__init__(create_ui=True)
