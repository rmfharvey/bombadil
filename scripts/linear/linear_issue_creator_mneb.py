import os
from bombadil_tracking.linear_client import LinearHelper


_root = os.path.dirname(__file__)
template_path = "../../src/bombadil_tracking/tasks/task_lists"
# template_path = "C:/VersionControl/Software/bombadil/src/bombadil_tracking/tasks/task_lists"

API_KEY = None
PROJECT = "Mothernode Ethernet PCBA (100425-xx-A)"

linear = LinearHelper()

kw = {"project": PROJECT, "post": True}

all_issues = []
ex = lambda issues: all_issues.extend(issues)

########################################################################################################################
### Controller Basic
########################################################################################################################
p = os.path.join(template_path, "controller_basic.json")
ex(linear.create_issues_from_json(json_tasks=p, **kw))

########################################################################################################################
### SMPS
########################################################################################################################
p = os.path.join(template_path, "smps.json")
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_5V0_EIC", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_3V3", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="SWITCH_VDDL", **kw))

########################################################################################################################
### Load Switches
########################################################################################################################
# p = os.path.join(template_path, "load_switch.json")
# for switch_name in []:
#     ex(linear.create_issues_from_json(json_tasks=p, element_name=switch_name, **kw))

########################################################################################################################
### LDOs
########################################################################################################################
# p = os.path.join(template_path, "ldo.json")
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_1V8_IMU", **kw))
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_HALOW_1V8", **kw))

########################################################################################################################
### Comms
########################################################################################################################
# p = os.path.join(template_path, "comms.json")
# for bus in []:
#     ex(linear.create_issues_from_json(json_tasks=p, element_name=bus, **kw))


print()
