from galvanic_design.base_objects import BaseObject
from galvanic.ui.microcontroller.pad_widget import PadWidget


class Pad(BaseObject):
    pad_name: str
    pin_name: str = None
    functions: list = []
    net_name: str = None
    current_function: str = None

    WIDGET_CLASS = PadWidget

    def __init__(
        self,
        pad_name: str = None,
        pin_name: str = None,
        functions: list = [],
        net_name: str = None,
        current_function: str = None,
    ):
        super().__init__(name=pad_name)

        self.pin_name = pin_name
        self.functions = functions
        self.net_name = net_name

        self.current_function = None
        self.set_function(current_function)

        self.ui_object = self.create_ui_element()

    def set_function(self, function: str = None):
        try:
            valid_function = function in self.functions + [None]
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
        self._name = value
