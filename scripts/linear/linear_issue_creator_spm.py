import os
from galvanic_tracking.linear_client import LinearHelper


_root = os.path.dirname(__file__)
# template_path = "/galvanic_tracking/tasks/task_lists"
template_path = "C:/VersionControl/Software/galvanic/src/galvanic_tracking/tasks/task_lists"

API_KEY = None
PROJECT = "Skynode Power Module (R0.5)"

linear = LinearHelper()

# Create Issues
p = os.path.join(template_path, "controller_basic.json")
new_issues = linear.create_issues_from_json(project=PROJECT, json_tasks=p, post=True)

p = os.path.join(template_path, "smps.json")
new_issues = linear.create_issues_from_json(project=PROJECT, json_tasks=p, element_name="PWR_5V0", post=True)
new_issues = linear.create_issues_from_json(project=PROJECT, json_tasks=p, element_name="PWR_3V3", post=True)
new_issues = linear.create_issues_from_json(project=PROJECT, json_tasks=p, element_name="VBUS_14V", post=True)

p = os.path.join(template_path, "load_switch.json")
for switch_name in [
    "PWR_5V0_SW",
    "PWR_3V3_SW",
]:
    new_issues = linear.create_issues_from_json(project=PROJECT, json_tasks=p, element_name=switch_name, post=True)

p = os.path.join(template_path, "hsd.json")
new_issues = linear.create_issues_from_json(project=PROJECT, json_tasks=p, element_name="VBUS_14V_OUTPUT", post=True)


