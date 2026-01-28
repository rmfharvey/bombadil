import json
from bombadil_design.controller import Controller
from bombadil_altium.server_api import AltiumServerAPI
from bombadil_ai.llm_client.gemini_client import GeminiClient

glm = GeminiClient()

AltiumServerAPI.load_urls(
    base_url="https://specter-industries.365.altium.com", api_url="https://usw.365.altium.com/viewer/api"
)


guid = {
    "Sensor Node": "DA220208-0D1D-4C1A-A0FF-E0D169E92F96",
    "Skynode Power Module": "A3271523-CB6E-428C-985C-8895C26F87C0",
    "Mothernode Control Board": "8FFEC27D-C20D-4837-A862-F81EF9A4EC6E",
}
# PRJ_NAME = "Mothernode Control Board"
PRJ_NAME = "Sensor Node"


c = Controller(guid[PRJ_NAME])
c.chat()
print()
