import os
from galvanic_tracking.linear_client import LinearHelper


_root = os.path.dirname(__file__)
# template_path = "/galvanic_tracking/tasks/task_lists"
template_path = "C:/VersionControl/Software/galvanic/src/galvanic_tracking/tasks/task_lists"

API_KEY = None
PROJECT = "Vision Sensor Node (R0.5)"

linear = LinearHelper()

kw ={
    "project": PROJECT,
    "post": False
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
# ex(linear.create_issues_from_json(json_tasks=p, element_name="VBUS_PoE", **kw))
#
# ########################################################################################################################
# ### Load Switches
# ########################################################################################################################
# p = os.path.join(template_path, "load_switch.json")
# for switch_name in [
#     "VBUS_14V_SW",
#     "PWR_5V0_SW",
#     "PWR_HALOW_SW",
#     "PWR_5V0_RK_SW",
#     "PWR_5V0_CAMERA_SW",
#     "PWR_3V3_SW",
#     "PWR_3V3_LTE_SW",
#     "PWR_3V3_RK_SW",
# ]:
#     ex(linear.create_issues_from_json(json_tasks=p, element_name=switch_name, **kw))
#
# ########################################################################################################################
# ### LDOs
# ########################################################################################################################
# p = os.path.join(template_path, "ldo.json")
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_1V8_IMU", **kw))
# ex(linear.create_issues_from_json(json_tasks=p, element_name="PWR_HALOW_1V8", **kw))

########################################################################################################################
### Comms
########################################################################################################################
p = os.path.join(template_path, "comms.json")
for bus in [
    "I2C.MCU",
    "I2C.RK",
    "I2C.TELEMETRY_1",
    "I2C.TELEMETRY_2",
    "SPI.HALOW_MCU",
    "SPI.HALOW_RK",
    "UART.IPC",
    "UART.RK_DEBUG",
    "USB.RK_LTE",
]:
    ex(linear.create_issues_from_json(json_tasks=p, element_name=bus, **kw))


print()
