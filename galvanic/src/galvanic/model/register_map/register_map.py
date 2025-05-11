from galvanic.ui.register_map.register_map_ui import RegisterWidget, FieldWidget


class RegisterMap:
    registers: dict
    fields: list

    def __init__(self, config):
        self.registers = {}
        self.fields = []
        self.load_config(config)
        print()

    def load_config(self, config):
        """Load from configuration

        :param dict config: Configuration information
        """
        for addr, reg in config.get("registers", {}).items():
            self.registers[addr] = Register(reg)

        for field in config.get("fields", []):
            self.fields.append(Field(field))

        self._add_fields_to_registers()

    def _add_fields_to_registers(self):
        """Look through all fields and add them to the appropriate register object."""
        registers = {}

        for f in self.fields:
            for chunk in f.register_location:
                addr = chunk["register_address"]
                if addr not in registers:
                    registers[addr] = []
                registers[addr].append(f)

        fields_dict = self._organize_fields()
        for addr, fields in fields_dict.items():
            target_reg = self.registers[addr]
            target_reg.add_fields(fields)


class Register:
    name: str
    read_only: bool = False
    address: int
    bit_width: int
    init_value: int = 0
    fields: list = []

    def __init__(self, config):
        self.load_config(config)
        self.ui_object = RegisterWidget(self)

    def load_config(self, config):
        self.name = config.get("name")
        self.read_only = config.get("read_only", self.read_only)
        self.address = config.get("address")
        self.bit_width = config.get("bit_width")
        self.init_value = config.get("init_value", self.init_value)

    def add_fields(self, fields_list):
        print()

    @property
    def hex_address(self):
        return "0x{:02X}".format(self.address)


class Field:
    description: str
    digital_physical_map: dict = {}
    name: str
    register_location: list
    parent_register: Register = None

    def __init__(self, config):
        self.load_config(config)
        self.ui_object = FieldWidget(self)

    def load_config(self, config):
        self.description = config.get("description")
        self.digital_physical_map = config.get("digital_physical_map", self.digital_physical_map)
        self.name = config.get("name")
        self.register_location = config.get("register_location")

    @property
    def register_location_by_addr(self):
        return {l["register_address"]: l for l in self.register_location}
