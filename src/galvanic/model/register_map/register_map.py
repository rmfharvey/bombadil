from galvanic.ui.register_map.register_map_ui import RegisterMapWidget, RegisterWidget, FieldWidget, FieldWidgetDummy
from galvanic import global_logger


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

    @property
    def field_dict(self):
        field_count = len(self.fields)
        fdict = {f.name: f for f in self.fields}
        if field_count != len(fdict):
            global_logger.warning("Some field names are repeated based on list/dict lengths")
        return fdict


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

            # Also set parent in Field
            f.parent_register = self

        sorted_fields = sorted(temp_fields.keys())
        for addr in sorted_fields:
            self.fields[addr] = temp_fields[addr]

        self.ui_object.refresh_fields_in_ui()

    @property
    def hex_address(self):
        return "0x{:02X}".format(self.address)

    @property
    def value(self):
        """Register value is calculated on the fly as the sum of all of its elements"""
        bin_val = f"{self.init_value:0{self.bit_width+1}b}"
        for f in self.fields.values():
            fval = f.get_binary_value_dict()[self.address]
            start = f.register_location_by_addr[self.address]["reg_start_bit"]
            end = f.register_location_by_addr[self.address]["reg_end_bit"] + 1
            bin_val = bin_val[:start] + fval + bin_val[end:]
        return int(bin_val[:-1][::-1], 2)


class Field:
    def __init__(self, config):
        self.value = 0
        self.parent_register = None
        self.digital_physical_map = {}

        self.load_config(config)

        # Set up UI
        bw = self.get_bit_widths()
        bw.pop("total")
        width = max(bw.values())
        if self.reserved_field:
            self.ui_object = FieldWidgetDummy(self, width)
        else:
            self.ui_object = FieldWidget(self, width)

        # Determine if a dummy widget is needed and link widgets to register locations
        reg_dict = self.register_location_by_addr
        for loc in reg_dict.values():
            loc["width"] = loc["reg_end_bit"] - loc["reg_start_bit"] + 1
            loc["master"] = False

        # Determine which field fragment is that largest, therefore 'master'
        max_width = max([r["width"] for r in reg_dict.values()])
        for r in reg_dict.values():
            if r["width"] == max_width:
                r["master"] = True
                break  # Break from loop to avoid

        self.value_range = [0, 2 ** self.get_bit_widths()["total"] - 1]

        # Assign UI objects
        for r in self.register_location:
            target = reg_dict[r["register_address"]]
            is_master = target["master"]
            if is_master:
                r["ui_object"] = self.ui_object
            else:
                width = target["reg_end_bit"] - target["reg_start_bit"] + 1
                r["ui_object"] = FieldWidgetDummy(self, width)

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

    def get_binary_value_dict(self):
        width = self.get_bit_widths()["total"]
        bin_val = f"{self.value:0{width}b}"[::-1]

        val_dict = {}
        for f in self.register_location:
            has_start_bit = "field_start_bit" in f
            has_end_bit = "field_end_bit" in f
            if has_start_bit and has_end_bit:
                val_dict[f["register_address"]] = bin_val[f["field_start_bit"] : f["field_end_bit"] + 1]
            else:
                val_dict[f["register_address"]] = bin_val
        return val_dict

    @property
    def reserved_field(self):
        return self.name.startswith("RESERVED_0x")

    @property
    def register_location_by_addr(self):
        return {l["register_address"]: l for l in self.register_location}
