import json
import pyperclip
from galvanic import global_logger
from galvanic_altium.server_api import AltiumServerAPI
from galvanic_altium.project import AltiumProject
from galvanic_datasheets.datasheet_manager import DatasheetManager
from schema_regex_testing import get_signal_list

FORCE_RELOAD_DATASHEETS = False

if __name__ == "__main__":
    AltiumServerAPI.load_urls(
        base_url="https://specter-industries.365.altium.com", api_url="https://usw.365.altium.com/viewer/api"
    )
    projects = AltiumServerAPI.get_project_list()

    guid = {
        # "Sensor Node": "DA220208-0D1D-4C1A-A0FF-E0D169E92F96",
        # "Skynode Power Module": "A3271523-CB6E-428C-985C-8895C26F87C0",
        "Mothernode Control Board": "8FFEC27D-C20D-4837-A862-F81EF9A4EC6E",
    }
    # PRJ_NAME = "Mothernode Control Board"

    for PRJ_NAME in guid.keys():
        project = AltiumProject(guid[PRJ_NAME])

        cfg = project.get_config()

        # Get all datasheets
        for des, component in project.bom.components_by_type["U"].items():
            pn = component.parameters.get("Comment")
            if len(component.avl):
                pn = component.avl[0][1]
            pn = pn.lower()

            if pn in DatasheetManager.datasheets and not FORCE_RELOAD_DATASHEETS:
                global_logger.info(f"{pn} exists, skipping")
                continue

            pyperclip.copy(pn)
            get = input(f"Get datasheet for {pn}? (y/n):")
            if not get.lower() == "y":
                continue
            DatasheetManager.new_datasheet(pn, autocreate_json=True)

        signals = get_signal_list(cfg)

        # Save project config
        with open(f"{PRJ_NAME}.json", "w") as f:
            json.dump(cfg, f, indent=2, separators=(",", ": "))

        # Try to determine all signal types
        # with open(f"{PRJ_NAME}_signals.json", "w") as f:
        #     json.dump(signals, f, indent=2, separators=(",", ": "))
        # print()
