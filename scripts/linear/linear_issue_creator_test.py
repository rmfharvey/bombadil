import os
import json
from linear_api import LinearPriority
from galvanic_tracking.linear_client import LinearClient, LinearHelper
from galvanic_tracking.tasks.enums import TASK_TYPE, VALIDATION_PHASE


_root = os.path.dirname(__file__)
template_path = "/galvanic_tracking/tasks/task_lists"

linear = LinearHelper()

for task_list in os.listdir(template_path):
    p = os.path.join(template_path, task_list)
    new_issues = linear.create_issues_from_json(project="Vision Sensor Node (R0.5)", json_filepaths=p, post=False)
    print()
