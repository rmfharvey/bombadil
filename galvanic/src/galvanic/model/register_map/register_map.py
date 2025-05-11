from galvanic.ui.register_map.register_map_ui import RegisterWidget, FieldWidget


class RegisterMap:
    def __init__(self, config):
        self.registers = []
        self.fields = []
        self.load_config(config)

    def load_config(self, config):
        for reg in config.get("registers", []):
            self.registers.append(Register(reg))

        for field in config.get("fields", []):
            self.fields.append(Field(field))


class Register:
    name: str
    read_only: bool = False
    address: int
    bit_width: int
    init_value: int = 0

    def __init__(self, config):
        self.load_config(config)
        self.ui_object = RegisterWidget(self)

    def load_config(self, config):
        self.name = config.get("name")
        self.read_only = config.get("read_only", self.read_only)
        self.address = config.get("address")
        self.bit_width = config.get("bit_width")
        self.init_value = config.get("init_value", self.init_value)

    @property
    def hex_address(self):
        return "0x{:02X}".format(self.address)


class Field:
    description: str
    digital_physical_map: dict = {}
    name: str
    register_location: list

    def __init__(self, config):
        self.load_config(config)
        self.ui_object = FieldWidget(self)

    def load_config(self, config):
        self.description = config.get("description")
        self.digital_physical_map = config.get("digital_physical_map", self.digital_physical_map)
        self.name = config.get("name")
        self.register_location = config.get("register_location")
