from pathlib import Path


class PATHS:
    ROOT = Path(__file__).parent
    ALTIUM = ROOT / "galvanic_altium"
    DESIGN = ROOT.parent / "galvanic_design"
    SCHEMAS = ROOT.parent / "galvanic_schemas"
    VALIDATION = ROOT.parent / "galvanic_validation"
