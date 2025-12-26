from __future__ import annotations  # Skip typehinting evaluation
from galvanic.ui.microcontroller.forms.pad_ui import Ui_Form as PadForm
from galvanic.ui import GWidget
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoid circular dependency with Pad/PadWidget
    from galvanic_design.microcontroller.pad import Pad


class PadWidget(GWidget):
    def __init__(self, pad_object: Pad):
        super().__init__(form=PadForm, linked_obj=pad_object)
        self._setup()

    def _setup(self):
        self.ui.pad_name_label.setText(self.obj.pad_name)
        self.ui.pin_name_label.setText(self.obj.pin_name or "")
        self.ui.net_name_lineedit.setText(self.obj.net_name or "")

    def _connect(self):
        self.ui
