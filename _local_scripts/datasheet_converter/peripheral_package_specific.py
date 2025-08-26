"""Test script to convert pads to pins based on package type.
WILL GET DELETED SOON
"""
import json

FN = 'stm32h723/datasheet.json'
PACKAGE = 'TFBGA100'

with open(FN, 'r') as f:
    ds = json.load(f)

def get_pin(pad_name):
    return ds['pin_pad_mapping'].get(pad_name,{}).get(PACKAGE)

for periph, instances in ds['peripherals'].items():
    for inst in instances.values():
        new_assignable = [get_pin(pn) for pn in inst['assignable_pins']]
        new_assignable = list(filter(None, new_assignable))

        inst['assignable_pins'] = new_assignable

        for sub, pads in inst['subusages'].items():
            new_assignable = [get_pin(pn) for pn in pads]
            new_assignable = list(filter(None, new_assignable))
            inst['subusages'][sub] = new_assignable
periphs = ds['peripherals']
print()