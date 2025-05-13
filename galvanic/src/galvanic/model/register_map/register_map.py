from galvanic.ui.register_map.register_map_ui import RegisterMapWidget, RegisterWidget, FieldWidget


class RegisterMap:
    registers: dict
    fields: list

    def __init__(self, config):
        self.registers = {}
        self.fields = []
        self.load_config(config)

        self.ui_object = RegisterMapWidget(self)

    def load_config(self, config):
        """Load from configuration

        :param dict config: Configuration information
        """
        registers = config.get("registers", {})
        for addr in sorted(registers.keys()):
            reg = registers[addr]
            self.registers[int(addr)] = Register(reg)

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

        for addr, fields in registers.items():
            target_reg = self.registers[addr]
            target_reg.add_fields(fields)


class Register:
    def __init__(self, config):
        self.read_only = False
        self.init_value = 0
        self.fields = {}

        self.load_config(config)
        self.ui_object = RegisterWidget(self)

    def load_config(self, config):
        self.name = config.get("name")
        self.read_only = config.get("read_only", self.read_only)
        self.address = config.get("address")
        self.bit_width = config.get("bit_width")
        self.init_value = config.get("init_value", self.init_value)

    def add_fields(self, fields_list):
        """Add fields (ordered) to Register object.

        :param list fields_list: List of individual fields in register:
        """
        # Compile fields with sortable keys
        temp_fields = {}  # Indexed by start bit
        for f in fields_list:
            loc = f.register_location_by_addr[self.address]
            temp_fields[loc["reg_start_bit"]] = f

        sorted_fields = sorted(temp_fields.keys())
        for addr in sorted_fields:
            self.fields[addr] = temp_fields[addr]

        self.ui_object.refresh_fields_in_ui()

    @property
    def hex_address(self):
        return "0x{:02X}".format(self.address)


class Field:
    def __init__(self, config):
        self.parent_register = None
        self.digital_physical_map = {}

        self.load_config(config)

        # Set up UI
        bw = self.get_bit_widths()
        bw.pop("total")
        width = max(bw.values())
        self.ui_object = FieldWidget(self, width)

    def load_config(self, config):
        self.description = config.get("description")
        self.digital_physical_map = config.get("digital_physical_map", self.digital_physical_map)
        self.name = config.get("name")
        self.register_location = config.get("register_location")

    def get_bit_widths(self):
        """Get widths of all individual segments, if the field is split up across multiple registers.

        :return: Dictionary of total field width and widths for all segments
        :rtype: dict
        """
        widths = {"total": 0}
        for seg in self.register_location:
            seg_width = seg["reg_end_bit"] - seg["reg_start_bit"] + 1
            widths[seg["register_address"]] = seg_width
            widths["total"] += seg_width
        return widths

    @property
    def register_location_by_addr(self):
        return {l["register_address"]: l for l in self.register_location}
