import json
from galvanic.model.register_map.register_map import RegisterMap
from galvanic import MainApp

cfg_path = "./tp92520.json"
with open(cfg_path, "r") as f:
    cfg = json.load(f)

rm = RegisterMap(cfg["serial_bus"])
rm.field_dict["CH1PWM"].value = 0b1100001100
# d = rm.field_dict["CH1PWM"].get_binary_value_dict()
print(rm.registers[13].value)
print(rm.registers[14].value)

rm.ui_object.show()
MainApp.exec()
print()
