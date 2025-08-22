import os
from galvanic_tracking.linear_client import LinearHelper


_root = os.path.dirname(__file__)
# template_path = "/galvanic_tracking/tasks/task_lists"
template_path = "C:/VersionControl/Software/galvanic/src/galvanic_tracking/tasks/task_lists"

API_KEY = None
PROJECT = "Mother Node Control Board (R0.5)"

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
p = os.path.join(template_path, "controller_basic.json")
ex(linear.create_issues_from_json(json_tasks=p, **kw))
#
# ########################################################################################################################
# ### SMPS
# ########################################################################################################################
p = os.path.join(template_path, "smps.json")
ex(linear.create_issues_from_json(json_tasks=p, element_name="BATTERY_CHARGE_CONTROLLER", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_12V0_ATX", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_5V0_ATX", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_3V3_ATX", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_5VSB_ATX", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_5V0", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_2V5_ETH", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_1V0_ETH", **kw))

# ########################################################################################################################
# ### Load Switches
# ########################################################################################################################
p = os.path.join(template_path, "load_switch.json")
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_5VSB_ATX Switch", **kw))
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_3V3_SW", **kw))
#
# ########################################################################################################################
# ### HSDs
# ########################################################################################################################
p = os.path.join(template_path, "hsd.json")
ex(linear.create_issues_from_json(json_tasks=p, element_name="PoE_PWR_STARLINK", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="PoE_PWR_GATEWAY", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="FAN_POWER_A", **kw))
ex(linear.create_issues_from_json(json_tasks=p, element_name="FAN_POWER_B", **kw))
#
# ########################################################################################################################
# ### LDOs
# ########################################################################################################################
p = os.path.join(template_path, "ldo.json")
ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_3V3", **kw))

########################################################################################################################
### Comms
########################################################################################################################
p = os.path.join(template_path, "comms.json")
for bus in [
    "I2C.LED",
    "UART.ETH",
    "UART.DEBUG",
    "SPI.12V_ATX"
    "RMII.MCU"
]:
    ex(linear.create_issues_from_json(json_tasks=p, element_name=bus, **kw))

print()