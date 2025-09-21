import json
from galvanic_datasheets.datasheet_manager import DatasheetManager
from galvanic.model.register_map.register_map import RegisterMap
from galvanic import MainApp

pn = "ina236aiddfr"

cfg_path = DatasheetManager.datasheets[pn].json_path
with open(cfg_path, "r") as f:
    cfg = json.load(f)

rm = RegisterMap(cfg["serial_bus"])


rm.ui_object.show()
MainApp.exec()
print()
