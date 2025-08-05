from galvanic_design.controller import Controller
from galvanic_altium.server_api import AltiumServerAPI

AltiumServerAPI.load_urls(
    base_url="https://specter-industries.365.altium.com", api_url="https://usw.365.altium.com/viewer/api"
)

guid = {"Sensor Node": "DA220208-0D1D-4C1A-A0FF-E0D169E92F96"}
PRJ_NAME = "Sensor Node"


c = Controller(guid[PRJ_NAME])
print()
