import json
from bombadil import global_logger
from bombadil_altium.server_api import AltiumServerAPI
from bombadil_altium.project import AltiumProject
from bombadil_datasheets.datasheet_manager import DatasheetManager
from schema_regex_testing import get_signal_list

FORCE_RELOAD_DATASHEETS = False

if __name__ == "__main__":
    AltiumServerAPI.load_urls(
        base_url="https://specter-industries.365.altium.com", api_url="https://usw.365.altium.com/viewer/api"
    )
    projects = AltiumServerAPI.get_project_list()

    guid = {
        "Sensor Node": "DA220208-0D1D-4C1A-A0FF-E0D169E92F96",
        "Skynode Power Module": "A3271523-CB6E-428C-985C-8895C26F87C0",
        "Mothernode Control Board": "8FFEC27D-C20D-4837-A862-F81EF9A4EC6E",
    }
    PRJ_NAME = "Sensor Node"

    for PRJ_NAME in guid.keys():
        project = AltiumProject(guid[PRJ_NAME])

        cfg_init = project.get_config()

        # Save project config
        with open(f"{PRJ_NAME}.json", "w") as f:
            json.dump(cfg_init, f, indent=2, separators=(",", ": "))
