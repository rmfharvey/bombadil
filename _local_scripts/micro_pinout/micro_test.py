from galvanic import MainApp
from galvanic_datasheets.datasheet_manager import DatasheetManager
from galvanic_design.microcontroller.microcontroller import Microcontroller

ds = DatasheetManager.get_datasheet("stm32h743")
m = Microcontroller.from_config(ds)
m.ui_object.show()
MainApp.exec()
print()
