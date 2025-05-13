from galvanic.ui import GWidget
from galvanic.ui.register_map.forms.register_ui import Ui_Form as RegisterForm
from galvanic.ui.register_map.forms.field_ui import Ui_Form as FieldForm


class RegisterWidget(GWidget):
    def __init__(self, register):
        super().__init__(RegisterForm)
        self.register = register

        self._setup()

    def _setup(self):
        self.ui.register_groupbox.setTitle(self.register.name)

    def refresh_fields_in_ui(self):
        print()


class FieldWidget(GWidget):
    def __init__(self, field):
        super().__init__(FieldForm)
        self.field = field

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
