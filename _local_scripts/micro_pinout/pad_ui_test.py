from galvanic import MainApp
from galvanic_datasheets.datasheet_manager import DatasheetManager
from galvanic_design.microcontroller.pad import Pad

ds = DatasheetManager.get_datasheet("stm32h723")

pad = Pad.from_config(list(ds["pads"].values())[10])
pad.ui_object.show()

# pads = {pn: Pad.from_config(p) for pn, p in ds["pads"].items()}
# list(pads.values())[10].ui_object.show()

MainApp.exec()
print()
