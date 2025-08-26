from PySide6 import QtCore
from galvanic.ui import GWidget
from galvanic.ui.register_map.forms.register_map_ui import Ui_Form as RegisterMapForm
from galvanic.ui.register_map.forms.register_ui import Ui_Form as RegisterForm
from galvanic.ui.register_map.forms.field_ui import Ui_Form as FieldForm


class RegisterMapWidget(GWidget):
    def __init__(self, register_map):
        super().__init__(RegisterMapForm)
        self.register_map = register_map
        self._setup()

    def _setup(self):
        for reg in self.register_map.registers.values():
            self.ui.register_map_scrollarea_layout.addWidget(reg.ui_object)


class RegisterWidget(GWidget):
    def __init__(self, register):
        super().__init__(RegisterForm)
        self.register = register

        self._setup()

    def update_frame_data_label(self, value):
        # TODO calculate full frame later
        self.ui.frame_data_label.setText(f"0x{value:0{int(self.register.bit_width/4)}x}")

    def _setup(self):
        title = f"{self.register.name} ({self.register.hex_address})"
        self.ui.register_id_label.setText(title)
        self.update_frame_data_label(self.register.value)

    def refresh_fields_in_ui(self):
        for f in self.register.fields.values():
            ui_obj = f.register_location_by_addr[self.register.address]["ui_object"]
            self.ui.register_layout.insertWidget(0, ui_obj)


class FieldWidget(GWidget):
    BITWIDTH = 150
    SPACING = 2
    HEIGHT = 55

    def __init__(self, field, width=1):
        super().__init__(FieldForm)
        self.field = field
        self._bit_width = width

        self._setup()
        self._connect_signals()

    def _setup(self):
        self.ui.field_name_label.setText(self.field.name)

        # Choose Value widgets based on digital to physical mapping
        if self.field.digital_physical_map:
            self.ui.value_combobox.addItems(self.field.digital_physical_map.values())
            self.ui.value_combobox.show()
            self.ui.value_lineedit.hide()
        else:
            self.ui.value_combobox.hide()
            self.ui.value_lineedit.show()

        # Increase UI entry element widths if in a larger field
        if self._bit_width > 1:
            for obj in [self.ui.value_combobox, self.ui.value_lineedit]:
                pxwidth = obj.width() * 2
                pxheight = obj.height()
                obj.setMinimumSize(QtCore.QSize(pxwidth, pxheight))

        pxwidth = (self._bit_width - 1) * (self.BITWIDTH + self.SPACING) + self.BITWIDTH
        self.ui.frame.setMinimumSize(QtCore.QSize(pxwidth, self.HEIGHT))
        self.ui.frame.setMaximumSize(QtCore.QSize(pxwidth, self.HEIGHT))

    def _connect_signals(self):
        self.ui.value_combobox.currentIndexChanged.connect(self._handler_combobox_changed)
        self.ui.value_lineedit.editingFinished.connect(self._handler_lineedit_changed)

    # Signal Handlers
    def _handler_combobox_changed(self):
        value = self.ui.value_combobox.currentText()
        pd_map = {v: k for k, v in self.field.digital_physical_map.items()}
        self.field.value = int(pd_map[value])

    def _handler_lineedit_changed(self):
        value = self.ui.value_lineedit.text()
        self.field.value = int(value)


class FieldWidgetDummy(FieldWidget):
    def _setup(self):
        super()._setup()
        self.ui.field_name_label.setText(self.field.name)
        self.ui.value_lineedit.hide()
        self.ui.value_combobox.hide()
