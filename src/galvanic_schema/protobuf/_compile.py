"""Compile proto files to Python
"""

import os
import logging
import subprocess

logger = logging.getLogger("Protobuf Compiler")
_root = os.path.dirname(__file__)

for dir, __, files in os.walk(_root):
    for f in files:
        if not f.endswith(".proto"):
            continue
        fp = os.path.join(dir, f)
        subprocess.call(["protoc", f"--proto_path={_root}", f"--python_out={_root}", f"{fp}"])
        # os.system(f"protoc --proto_path={_root} --python_out={dir} {fp}")
