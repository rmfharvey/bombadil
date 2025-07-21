from functools import wraps
import json
import inspect
from types import FunctionType, MethodType


def is_jsonable(v):
    try:
        if not isinstance(v, dict):
            v = {"key": v}
        json.dumps(v)
        return True, True
    except (TypeError, OverflowError) as e:
        return False, e


def validate_json_serialization(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        retval = f(*args, **kwargs)
        jsonable, err = is_jsonable(retval)
        if jsonable:
            return retval
        else:
            raise ValueError(f"JSON serialization failed: {err}")

    return wrapper


def get_class_members(cls, include_private=False):
    members = {}

    for name in dir(cls):
        # Skip built-in attributes unless specifically requested
        if not include_private and name.startswith("_"):
            continue

        try:
            attr = getattr(cls, name)

            # Skip functions and methods
            if isinstance(attr, (FunctionType, MethodType)):
                continue

            # Skip built-in functions, methods, and descriptors
            if inspect.isbuiltin(attr) or inspect.ismethod(attr) or inspect.isfunction(attr):
                continue

            # Skip Magic Methods
            if name.startswith("__") and name.endswith("__"):
                continue

            # Skip properties that are actually methods
            if isinstance(attr, property):
                continue

            # Skip class methods and static methods
            if isinstance(attr, (classmethod, staticmethod)):
                continue

            members[name] = attr

        except AttributeError:
            # Some attributes might not be accessible
            continue

    return members


###IGNORE  runs into recursion issues
# def get_config_members(obj, ignore=[]):
#     config = {}
#
#     # Preformat into dict based on type
#     is_list = False
#     if isinstance(obj, dict):
#         members = obj
#     elif isinstance(obj, list):
#         members = dict(enumerate(obj))
#         is_list = True
#     else:
#         members = get_class_members(obj, include_private=True)
#
#     # Compile into dict
#     for key, val in members.items():
#         jsonable, err = is_jsonable(val)
#         if not jsonable:
#             val = get_config_members(val)
#         config[key] = val
#
#     # Strip list if necessary
#     if is_list:
#         config = list(config.values())
#
#     return config


class AltiumBasic:
    @validate_json_serialization
    def get_config(self):
        return get_config_members(self)
