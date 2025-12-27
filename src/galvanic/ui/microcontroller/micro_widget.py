from __future__ import annotations  # Skip typehinting evaluation


from galvanic.ui.microcontroller.forms.micro_widget_ui import Ui_Form as MicroForm
from galvanic.ui import GWidget
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoid circular dependency with Pad/PadWidget
    from galvanic_design.microcontroller.microcontroller import MicroController


class MicroWidget(GWidget):
    def __init__(self, micro_object: MicroController):
        super().__init__(form=MicroForm, linked_obj=micro_object)
        self._setup()

    def _setup(self):
        self.ui.pads_frame_layout.addWidget(self.obj.pads.ui_object)

    def _connect_signals(self):
        pass
