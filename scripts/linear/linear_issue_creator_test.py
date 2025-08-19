import os
import json
from linear_api import LinearPriority
from galvanic_validation.linear_client import LinearClient, LinearHelper
from galvanic_validation.tasks.enums import TASK_TYPE, VALIDATION_PHASE


_root = os.path.dirname(__file__)
template_path = "/Users/rossharvey/Documents/SoftwareDevelopment/galvanic/src/galvanic_validation/tasks/task_lists"

linear = LinearHelper()

for task_list in os.listdir(template_path):
    p = os.path.join(template_path, task_list)
    with open(p, "r") as f:
        tasks = json.load(f)
    print()
