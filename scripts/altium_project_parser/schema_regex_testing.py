import json
from galvanic.signal import determine_signal_type
from galvanic.utils.enums import RAIL_REGULATION


def get_signal_list(project):
    signals = {}
    for name, net in project["nets"].items():
        result = determine_signal_type(name)

        if result:
            sig_type = result["class"].__name__
        else:
            sig_type = None
        if sig_type not in signals:
            signals[sig_type] = []
        signals[sig_type].append(name)
    return signals


if __name__ == "__main__":
    with open("Sensor Node.json", "r") as f:
        project = json.load(f)
    signals = get_signal_list(project)
    print()
