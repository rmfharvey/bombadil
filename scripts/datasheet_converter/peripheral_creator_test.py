import json
from galvanic.utils.datasheet_parser.datasheet_converter import MicroDatasheetConverter

fn = "stm32h7/datasheet.json"

with open(fn, "r") as f:
    ds = json.load(f)

peripheral = MicroDatasheetConverter.build_peripherals_from_pads(ds['pads'])
print()


with open(fn, "r") as f:
    ds = json.load(f)
with open("peripheral.json", "w") as f:
    json.dump(peripheral, f, indent=2, separators=(",", ": "))