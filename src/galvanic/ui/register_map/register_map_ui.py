import re
from PySide6 import QtCore
from galvanic import global_logger
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
        # TODO calculate full frame later, needs additional config input
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

    @staticmethod
    def _format_user_input(uin_str, range=None):
        """
        Formats and validates user input string as an integer in various number bases. Supports binary,
        hexadecimal, and decimal input formats. The input string is sanitized and converted to a base 10
        integer. Optionally checks if the integer value falls within a specified range.

        Parameters:
            uin_str (str): The input string to be formatted and validated.
            range (Optional[Iterable[int]]): Optional range (e.g., [min, max]) to assert the integer falls
                within the range. If not specified, no range validation is performed.

        Returns:
            Optional[int]: The formatted integer value if valid, otherwise None.
        """
        uin_str = uin_str.strip().lower()
        base = 10
        if re.fullmatch(r"0b[01]+", uin_str):
            base = 2
            uin_str = uin_str.replace("0b", "")
        # elif re.fullmatch(r"[01]+", uin_str) and len(uin_str) > 1:
        #     base = 2

        # Hexadecimal (prefix 0x or digits with A-F)
        elif re.fullmatch(r"0x[0-9a-f]+", uin_str):
            base = 16
            uin_str = uin_str.replace("0x", "")
        elif re.fullmatch(r"[0-9a-f]+", uin_str) and any(c in uin_str for c in "abcdef"):
            base = 16

        try:
            val = int(uin_str, base)
            if range:
                assert min(range) <= val <= max(range), "Value out of range"
            return val
        except (AssertionError, ValueError) as err:
            global_logger.error(f"Invalid input: {uin_str}")
            return None

    # Signal Handlers
    def _handler_combobox_changed(self):
        value = self.ui.value_combobox.currentText()
        pd_map = {v: k for k, v in self.field.digital_physical_map.items()}
        self.field.value = int(pd_map[value])
        print(f"{self.field.name} changed to {self.field.value}")

    def _handler_lineedit_changed(self):
        value = self.ui.value_lineedit.text()
        self.field.value = int(value)
        print(f"{self.field.name} changed to {self.field.value}")


class FieldWidgetDummy(FieldWidget):
    def _setup(self):
        super()._setup()
        self.ui.field_name_label.setText(self.field.name)
        self.ui.value_lineedit.hide()
        self.ui.value_combobox.hide()
