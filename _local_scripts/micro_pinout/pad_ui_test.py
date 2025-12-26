from galvanic import MainApp
from galvanic_datasheets.datasheet_manager import DatasheetManager
from galvanic_design.microcontroller.pad import Pad

ds = DatasheetManager.get_datasheet("stm32h743")
pads = {pn: Pad.from_config(p) for pn, p in ds["pads"].items()}

print()
list(pads.values())[0].ui_object.show()
MainApp.exec()
