import os

_protobuf_files = {}

_root = os.path.dirname(__file__)
for dir in os.listdir(_root):
    dir_path = os.path.join(_root, dir)
    not_dir = not os.path.isdir(dir_path)
    private = dir.startswith("_")
    if not_dir or private:
        continue
    _protobuf_files[dir] = {}
    for fl in os.listdir(dir_path):
        if not fl.endswith(".proto"):
            continue
        fl_name = fl.replace(".proto", "")
        with open(os.path.join(dir_path, fl), "r") as f:
            _protobuf_files[dir][fl_name] = f.read()


class _ProtobufFiles:
    """Helper class to hold all existing protobuf files.  Useful if you want to acces these from other packages or areas"""

    def __init__(self, protobuf_files):
        for k, v in protobuf_files.items():
            if isinstance(v, dict):
                setattr(self, k, _ProtobufFiles(v))
            else:
                setattr(self, k, v)


PROTOBUF = _ProtobufFiles(_protobuf_files)
