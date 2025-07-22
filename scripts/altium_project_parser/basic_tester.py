import json
from galvanic.signal import determine_signal_type
from galvanic_altium.altium_server_api import AltiumServerAPI, AltiumProject

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
    nets = {}
    for n in project.nets:
        nets[n] = determine_signal_type(n)
    print()
