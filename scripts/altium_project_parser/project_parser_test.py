import json
from galvanic_altium.server_api import AltiumServerAPI
from galvanic_altium.project import AltiumProject

from schema_regex_testing import get_signal_list


if __name__ == "__main__":
    AltiumServerAPI.load_urls(
        base_url="https://specter-industries.365.altium.com", api_url="https://usw.365.altium.com/viewer/api"
    )
    projects = AltiumServerAPI.get_project_list()

    guid = {"Sensor Node": "AEFD9A33-5A97-4C99-B21D-D2D9B3A4D90B"}
    PRJ_NAME = "Sensor Node"

    project = AltiumProject(guid[PRJ_NAME])

    cfg = project.get_config()

    with open(f"{PRJ_NAME}.json", "w") as f:
        json.dump(cfg, f, indent=2, separators=(",", ": "))

    # Try to determine all signal types
    signals = get_signal_list(cfg)
    print()
