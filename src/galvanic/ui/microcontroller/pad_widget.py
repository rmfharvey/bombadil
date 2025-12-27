from __future__ import annotations  # Skip typehinting evaluation

from sympy import solve_linear_system

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
        pp_name = [self.obj.pad_name or ""]
        if self.obj.pin_name:
            pp_name.append(self.obj.pin_name)
        pp_name = " | ".join(pp_name)
        self.ui.pad_name_label.setText(pp_name)

        self.ui.function_combobox.clear()
        self.ui.function_combobox.addItems(list(self.obj.functions.as_dict.keys()))
        self.ui.net_name_lineedit.setText(self.obj.net_name or "")

    def _connect_signals(self):
        self.ui.function_combobox.currentIndexChanged.connect(self._handler_function_changed)
        self.ui.net_name_lineedit.editingFinished.connect(self._handler_net_name_changed)

    ####################################################################################################################
    ### Signal Handlers
    ####################################################################################################################
    def _handler_function_changed(self):
        """Update the function of the pad when user input is provided"""
        selected_function = self.ui.function_combobox.currentText()
        if selected_function == "":
            selected_function = None
        self.obj.set_function(selected_function)

    def _handler_net_name_changed(self):
        """Update the net name of the pad when user input is provided"""
        new_net_name = self.ui.net_name_lineedit.text()
        if new_net_name == "":
            new_net_name = None
        self.obj.net_name = new_net_name
