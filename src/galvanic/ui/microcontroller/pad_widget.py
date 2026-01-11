from __future__ import annotations  # Skip typehinting evaluation

from galvanic.ui.microcontroller.forms.pad_ui import Ui_Form as PadForm
from galvanic.ui.microcontroller.forms.pad_list_ui import Ui_Form as PadListForm
from galvanic.ui import GWidget
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # Avoid circular dependency with Pad/PadWidget
    from galvanic_design.microcontroller.pad import Pad, PadList


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
        self.ui.function_combobox.addItems(["-"] + list(self.obj.functions.as_dict.keys()))
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
        if selected_function == "-":
            selected_function = None
        self.obj.set_function(selected_function)

    def _handler_net_name_changed(self):
        """Update the net name of the pad when user input is provided"""
        new_net_name = self.ui.net_name_lineedit.text()
        if new_net_name == "":
            new_net_name = None
        self.obj.net_name = new_net_name


class PadListWidget(GWidget):
    def __init__(self, pad_list_obj: PadList):
        super().__init__(form=PadListForm, linked_obj=pad_list_obj)

    def _repopulate(self, sort_by="pad"):
        """Repopulate the pad list, sorted by either pad or pin

        :param str sort_by: 'pad' or 'pin'
        """
        sort_by = "pad"  # TODO Just assert for now need to get pin names assigned in Pad/Microcontroller
        assert sort_by in ["pin", "pad"]

        values = {getattr(pad, f"{sort_by}_name"): pad for pad in self.obj.pads.values()}
        values.pop(None, None)  # Pop unused pads
        sorted_keys = sorted(values.keys(), reverse=True)  # TODO Change to alphanumeric sort with re later

        for k in sorted_keys:
            pad_obj = values[k]
            self.ui.pad_scrollarea_layout.insertWidget(0, pad_obj.ui_object)

    def _setup(self):
        self._repopulate(sort_by="pin")

    def _connect_signals(self):
        """Nothing to do for now"""
        pass
