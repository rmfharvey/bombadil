import json
from galvanic.model.register_map.register_map import RegisterMap
from galvanic import MainApp

cfg_path = "./tp92520.json"
with open(cfg_path, "r") as f:
    cfg = json.load(f)

rm = RegisterMap(cfg["serial_bus"])


rm.ui_object.show()
MainApp.exec()
print()
