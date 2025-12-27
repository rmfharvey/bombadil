from galvanic_design.microcontroller.pad import Pad, PadList


from galvanic_design.base_objects import BaseObject
from galvanic.ui.microcontroller.micro_widget import MicroWidget


class Microcontroller(BaseObject):
    WIDGET_CLASS = MicroWidget

    # def __init__(self, create_ui=True):
    #     super().__init__()

    def load_config(self, config):
        config = self._resolve_config_path(config)

        self.pads = PadList(config.pop("pads", {}))

        self._load_dict_values(config)
        self.ui_object = self.create_ui_element()

    def _load_pads(self, pads):
        print()
