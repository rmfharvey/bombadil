import json
from galvanic.utils.datasheet_parser.datasheet_converter import MicroDatasheetConverter

fn = "stm32h7/datasheet.json"

with open(fn, "r") as f:
    ds = json.load(f)

ds['peripherals'] = MicroDatasheetConverter.build_peripherals_from_pads(ds['pads'])


with open(fn, "w") as f:
    f.write(json.dumps(ds, indent=2, sort_keys=True, separators=(",", ": ")))