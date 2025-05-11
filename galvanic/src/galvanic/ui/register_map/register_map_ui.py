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


class FieldWidget(GWidget):
    def __init__(self, field):
        super().__init__(FieldForm)
        self.field = field

        self._setup()

    def _setup(self):
        self.ui.field_name_label.setText(self.field.name)

        # Choose Value widgets based on digital to physical mapping
        print()
