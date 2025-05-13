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

    def _setup(self):
        self.ui.register_groupbox.setTitle(self.register.name)

    def refresh_fields_in_ui(self):
        for f in self.register.fields.values():
            self.ui.register_layout.addWidget(f.ui_object)


class FieldWidget(GWidget):
    BITWIDTH = 2016

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

        self.resize(self._bit_width * self.BITWIDTH, 70)

    def _connect_signals(self):
        self.ui.value_combobox.currentIndexChanged.connect(self._handler_combobox_changed)
        self.ui.value_lineedit.editingFinished.connect(self._handler_lineedit_changed)

    # Signal Handlers
    def _handler_combobox_changed(self):
        value = self.ui.value_combobox.currentText()
        pd_map = {v: k for k, v in self.field.digital_physical_map.items()}
        self.field.value = pd_map[value]

    def _handler_lineedit_changed(self):
        value = self.ui.value_lineedit.currentText()
        self.field.value = value


class FieldWidgetDummy(FieldWidget):
    def _setup(self):
        self.ui.field_name_label.setText(self.field.name)
        self.ui.value_lineedit.hide()
        self.ui.value_combobox.hide()
        self.resize(self._bit_width * self.BITWIDTH, 70)
