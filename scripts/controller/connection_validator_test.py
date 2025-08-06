import json
from galvanic_design.controller import Controller
from galvanic_altium.server_api import AltiumServerAPI
from galvanic_ai.llm_client import GeminiClient

glm = GeminiClient()

AltiumServerAPI.load_urls(
    base_url="https://specter-industries.365.altium.com", api_url="https://usw.365.altium.com/viewer/api"
)


guid = {"Sensor Node": "DA220208-0D1D-4C1A-A0FF-E0D169E92F96"}
PRJ_NAME = "Sensor Node"


c = Controller(guid[PRJ_NAME])
inst = "This content includes part and connectivity information for an electronic PCBA.  It describes all of the connectivity in the 'nets' field and  You shall answer any questions based this content."
glm.add_cache(cache_item_name="project_metadata", instructions=inst, contents=json.dumps(c.project.get_config()))

print(glm.generate("how many microcontrollers are used and what are their part numbers?", cache_name='project_metadata').text)

print()
