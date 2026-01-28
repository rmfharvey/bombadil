import os
from bombadil_tracking.linear_client import LinearHelper


_root = os.path.dirname(__file__)
# template_path = "/bombadil_tracking/tasks/task_lists"
template_path = "C:/VersionControl/Software/bombadil/src/bombadil_tracking/tasks/task_lists"

API_KEY = None
PROJECT = "Skynode Power Module (R0.5)"

linear = LinearHelper()

kw ={
    "project": PROJECT,
    "post": True
}

all_issues = []
ex = lambda issues: all_issues.extend(issues)

# ########################################################################################################################
# ### Controller Basic
# ########################################################################################################################
# p = os.path.join(template_path, "controller_basic.json")
# ex(linear.create_issues_from_json(json_tasks=p, **kw))
#
# ########################################################################################################################
# ### SMPS
# ########################################################################################################################
# p = os.path.join(template_path, "smps.json")
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_5V0", **kw))
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_3V3", **kw))
# ex(linear.create_issues_from_json(json_tasks=p, element_name="VBUS_14V", **kw))
#
# ########################################################################################################################
# ### Load Switches
# ########################################################################################################################
# p = os.path.join(template_path, "load_switch.json")
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_5V0_SW", **kw))
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_3V3_SW", **kw))
#
# ########################################################################################################################
# ### HSDs
# ########################################################################################################################
# p = os.path.join(template_path, "hsd.json")
# ex(linear.create_issues_from_json(json_tasks=p, element_name="VBUS_14V_OUTPUT", **kw))
#
# ########################################################################################################################
# ### LDOs
# ########################################################################################################################
# p = os.path.join(template_path, "ldo.json")
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_1V8_IMU", **kw))

########################################################################################################################
### Comms
########################################################################################################################
p = os.path.join(template_path, "comms.json")
for bus in [
    "I2C.MAIN",
    "I2C.TELEMETRY",
    "SPI.T1S"
]:
    ex(linear.create_issues_from_json(json_tasks=p, element_name=bus, **kw))



print()