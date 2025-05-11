import os
import json


_root = os.path.dirname(__file__)

with open("build_list.json", "r") as f:
    build_list = json.load(f)

print("\nConverting ui files to py")
for dir, __, files in os.walk(_root):
    for fn in files:
        if not fn.endswith(".ui"):
            continue
        py_fn = fn.replace(".ui", "_ui.py")
        print(f"\t{fn} -> {py_fn}")

        ui_file = os.path.join(dir, fn)
        py_file = os.path.join(dir, py_fn)

        os.system(f"pyuic6 -o {py_file} {ui_file}")

print("End")
