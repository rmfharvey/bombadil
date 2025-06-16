import json
import os
import re
from csv import DictReader

from galvanic.utils.passive_naming_schema.series import ESeries
from galvanic.utils.metric_formatting import MetricValue
from galvanic import colored_logger


logger = colored_logger("capacitor Part Numbers")


class Capacitor:
    package: str
    capacitance: float
    rated_voltage: float
    dielectric: str
    tolerance: float
    height: float
    temp_min: float
    temp_max: float
    manufacturer: str
    part_number: str

    def __init__(
        self,
        package,
        capacitance,
        rated_voltage,
        dielectric,
        tolerance,
        manufacturer,
        height=None,
        temp_min=-55,
        temp_max=155,
        part_number=None,
    ):
        self.package = package
        self.capacitance = capacitance
        self.rated_voltage = rated_voltage
        self.dielectric = dielectric
        self.tolerance = tolerance
        self.height = height
        self.temperature_min = temp_min
        self.temperature_max = temp_max
        self.manufacturer = manufacturer
        self._part_number = part_number

    @property
    def name(self):
        return f"CAP,{self.package},{self.capacitance_str},{self.rated_voltage}V,{self.tolerance}%,"

    @property
    def name_short(self):
        return f"CAP,{self.package},{self.capacitance_str},{self.rated_voltage}V"

    @property
    def capacitance_str(self):
        return MetricValue.num_to_str(self.capacitance, units="F")

    @property
    def capacitance_str_prefix_delimited(self):
        return MetricValue.num_to_prefix_as_decimal_str(self.capacitance, default_decimal=".", str_length=3)

    @property
    def part_number(self):
        return self._part_number


def create_gcm_cap(pn):
    mapping = {
        "package": {
            "03": "0201",
            "15": "0402",
            "18": "0603",
            "21": "0805",
            "31": "1206",
            "32": "1210",
        },
        "voltage": {
            "0G": 2,
            "0E": 2.2,
            "0D": 4.0,
            "0J": 6.3,
            "1A": 10,
            "1C": 16,
            "1E": 25,
            "1H": 50,
            "2A": 100,
            "2B": 125,
            "2E": 250,
            "2J": 630,
        },
        "height": {
            "1": 0.125,
            "2": 0.2,
            "3": 0.3,
            "4": 0.4,
            "5": 0.5,
            "6": 0.6,
            "7": 0.7,
            "8": 0.8,
            "9": 0.85,
            "A": 1.0,
            "B": 1.25,
            "C": 1.6,
            "D": 2.0,
            "E": 2.5,
            "K": 0.08,
            "M": 1.15,
            "Q": 1.5,
            "S": 0.16,
            "T": 0.18,
            "Y": 0.135,
        },
        "temp_characteristic": {
            "5C": {"dielectric": "C0G", "temp_min": -55, "temp_max": 125},
            "C8": {"dielectric": "X6S", "temp_min": -55, "temp_max": 105},
            "D8": {"dielectric": "X6T", "temp_min": -55, "temp_max": 105},
            "C7": {"dielectric": "X7R", "temp_min": -55, "temp_max": 125},
            "R7": {"dielectric": "X7S", "temp_min": -55, "temp_max": 125},
            "D7": {"dielectric": "X7T", "temp_min": -55, "temp_max": 125},
            "E7": {"dielectric": "X7U", "temp_min": -55, "temp_max": 125},
            "L8": {"dielectric": "X8L", "temp_min": -55, "temp_max": 150},
            "M8": {"dielectric": "X8M", "temp_min": -55, "temp_max": 150},
            "N8": {"dielectric": "X8N", "temp_min": -55, "temp_max": 150},
            "R9": {"dielectric": "X8R", "temp_min": -55, "temp_max": 150},
        },
        "packaging": {
            "L": "180mm Embossed Taping",
            "D": "180mm Paper Taping",
            "E": "180mm Paper Taping",
            "W": "180mm Paper Taping",
            "K": "330mm Embossed Taping",
            "J": "330mm Paper Taping",
            "F": "330mm Paper Taping",
            "T": "Bulk Tray",
        },
        "tolerance": {
            "B": 0.1,
            "C": 0.25,
            "D": 0.5,
            "F": 1,
            "G": 2,
            "J": 5,
            "K": 10,
            "M": 20,
            "W": 0.05,
        },
    }

    def str_pop_to(idx, string):
        first = string[:idx]
        rem = string[idx:]
        return first, rem

    pn_copy = pn

    # Extract codes
    series, pn = str_pop_to(3, pn)
    package, pn = str_pop_to(2, pn)
    height, pn = str_pop_to(1, pn)
    temp_characteristic, pn = str_pop_to(2, pn)
    voltage, pn = str_pop_to(2, pn)
    capacitance, pn = str_pop_to(3, pn)
    tolerance, pn = str_pop_to(1, pn)
    packaging = pn[-1]

    try:
        # Get capacitance
        if "R" in capacitance:
            capacitance = float(capacitance.replace("R", "."))
        else:
            val = float(capacitance[:-1])
            exponent = int(capacitance[-1])
            capacitance = val * 10**exponent
        capacitance *= 1e-12  # Convert from pF

        dielectric = mapping["temp_characteristic"][temp_characteristic]["dielectric"]
        temp_max = mapping["temp_characteristic"][temp_characteristic]["temp_max"]
        temp_min = mapping["temp_characteristic"][temp_characteristic]["temp_min"]

        info = {
            "package": mapping["package"][package],
            "capacitance": capacitance,
            "rated_voltage": mapping["voltage"][voltage],
            "dielectric": dielectric,
            "tolerance": mapping["tolerance"][tolerance],
            "manufacturer": "Murata",
            "height": mapping["height"][height],
            "temp_min": temp_min,
            "temp_max": temp_max,
            "part_number": pn_copy,
        }

        return Capacitor(**info)
    except KeyError as err:
        logger.warning(f"Failed to parse {pn_copy}.  Failed with error: {err}")
        return None


class CapacitorSet:
    def __init__(self, capacitors={}):
        self.capacitors = capacitors
        self._validate_components()

    def _validate_components(self):
        """Brute force shcek to make sure there
        are no fatal errors"""
        vals = self._get_component_vals_dict()

        all_same = lambda k: len(list(set(vals[k]))) == 1

        assert all_same("package")
        assert all_same("capacitance")

    def _get_component_vals_dict(self):
        """Compile a dictionary opf all component values"""
        vals = {}
        for k in list(self.capacitors.values())[0].__dict__.keys():
            vals[k] = [getattr(r, k) for r in self.capacitors.values()]
        return vals

    @property
    def name(self):
        vals = self._get_component_vals_dict()

        return f"RES,{self.package},{self.capacitance_str_prefix_delimited},{self.tolerance}%,{self.power}W,{self.rated_voltage}V,{self.temp_coefficient}ppm"

    @property
    def capacitance_str_prefix_delimited(self):
        return list(self.capacitors.values())[0].capacitance_str_prefix_delimited

    @property
    def tolerance(self):
        vals = self._get_component_vals_dict()
        tolerance = max(vals["tolerance"])
        return tolerance

    @property
    def temp_coefficient(self):
        vals = self._get_component_vals_dict()
        temp_coeff = max(vals["temp_coefficient"])
        return temp_coeff

    @property
    def power(self):
        vals = self._get_component_vals_dict()
        power = min(vals["power"])
        return power

    @property
    def rated_voltage(self):
        vals = self._get_component_vals_dict()
        voltage = min(vals["rated_voltage"])
        return voltage

    @property
    def temperature_max(self):
        vals = self._get_component_vals_dict()
        temp_max = min(vals["temperature_max"])
        return temp_max

    @property
    def temperature_min(self):
        vals = self._get_component_vals_dict()
        temp_min = min(vals["temperature_min"])
        return temp_min

    @property
    def package(self):
        vals = self._get_component_vals_dict()
        package = vals["package"][0]
        return package

    @property
    def capacitance(self):
        vals = self._get_component_vals_dict()
        capacitance = vals["capacitance"][0]
        return capacitance


def compile_capacitor_pn_list():
    def add_capacitor(capacitor, target):
        key = capacitor.name_short
        # key = capacitor.capacitance
        if key not in target:
            target[key] = {}
        pn = capacitor.part_number
        if pn:
            target[key][pn] = capacitor

    # def add_vishay(capacitor_dict):
    #     ###################################################################################
    #     ### 0201                                                                        ###
    #     ###################################################################################
    #     PACKAGE = "0201"
    #
    #     kw = {
    #         "package": PACKAGE,
    #         "tolerance": 1,
    #         "temp_coefficient": 200,
    #         "manufacturer": "Vishay",
    #         "rated_voltage": 25,
    #     }
    #
    #     ### 0R
    #     res = capacitor(capacitance=0, **kw)
    #     add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     # 10R-10M
    #     for r in ESeries.get_values(10, 10e6, ESeries.E96):
    #         res = capacitor(capacitance=r, **kw)
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     ### 1R-9.76R
    #     for r in ESeries.get_values(1, 9.76, ESeries.E96):
    #         kw["temp_coefficient"] = 400
    #         res = capacitor(capacitance=r, **kw)
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     ###################################################################################
    #     ### 0402                                                                        ###
    #     ###################################################################################
    #     PACKAGE = "0402"
    #
    #     kw = {
    #         "package": PACKAGE,
    #         "tolerance": 1,
    #         "temp_coefficient": 100,
    #         "manufacturer": "Vishay",
    #         "rated_voltage": 75,
    #         "power": 0.1,
    #     }
    #
    #     ### 0R
    #     res = capacitor(capacitance=0, **kw)
    #     add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     # 1R-10M
    #     for r in ESeries.get_values(1, 10e6, ESeries.E96):
    #         res = capacitor(capacitance=r, **kw)
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     ###################################################################################
    #     ### 0603                                                                        ###
    #     ###################################################################################
    #     PACKAGE = "0603"
    #
    #     kw = {
    #         "package": PACKAGE,
    #         "tolerance": 1,
    #         "temp_coefficient": 100,
    #         "manufacturer": "Vishay",
    #         "rated_voltage": 75,
    #         "power": 0.125,
    #     }
    #
    #     ### 0R
    #     res = capacitor(capacitance=0, **kw)
    #     add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     # 1R-10M
    #     for r in ESeries.get_values(1, 10e6, ESeries.E96):
    #         res = capacitor(capacitance=r, **kw)
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     ###################################################################################
    #     ### 0805                                                                        ###
    #     ###################################################################################
    #     PACKAGE = "0805"
    #
    #     kw = {
    #         "package": PACKAGE,
    #         "tolerance": 1,
    #         "temp_coefficient": 100,
    #         "manufacturer": "Vishay",
    #         "rated_voltage": 125,
    #         "power": 0.15,
    #     }
    #
    #     ### 0R
    #     res = capacitor(capacitance=0, **kw)
    #     add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     # 1R-10M
    #     for r in ESeries.get_values(1, 10e6, ESeries.E96):
    #         res = capacitor(capacitance=r, **kw)
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     ###################################################################################
    #     packages = ["1206", "2010", "2512"]
    #     ###################################################################################
    #     for PACKAGE in packages:
    #         kw = {
    #             "package": PACKAGE,
    #             "tolerance": 1,
    #             "temp_coefficient": 100,
    #             "manufacturer": "Vishay",
    #         }
    #
    #         ### 0R
    #         res = capacitor(capacitance=0, **kw)
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #         # 1R-10M
    #         for r in ESeries.get_values(1, 10e6, ESeries.E96):
    #             res = capacitor(capacitance=r, **kw)
    #             add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     # TODO add larger packages
    #
    # def add_yageo(capacitor_dict):
    #     ###################################################################################
    #     ### 0201                                                                        ###
    #     ###################################################################################
    #     PACKAGE = "0201"
    #
    #     kw = {
    #         "package": PACKAGE,
    #         "tolerance": 1,
    #         "temp_coefficient": 200,
    #         "manufacturer": "Yageo",
    #         "rated_voltage": 30,
    #     }
    #
    #     # ### 0R
    #     # res = capacitor(capacitance=0, **kw)
    #     # add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     # 1R-10M, 1%
    #     for r in ESeries.get_values(1, 10e6, ESeries.E96):
    #         res = capacitor(capacitance=r, **kw)
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 10R-1M, 0.5%
    #     kw["tolerance"] = 0.5
    #     for r in ESeries.get_values(10, 1e6, ESeries.E96):
    #         res = capacitor(capacitance=r, **kw)
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     ###################################################################################
    #     ### Others                                                                      ###
    #     ###################################################################################
    #     for package in ["0402", "0603", "0805", "1206", "2010", "2512"]:
    #         kw = {
    #             "package": package,
    #             "temp_coefficient": 100,
    #             "manufacturer": "Yageo",
    #         }
    #
    #         ### 0R
    #         res = capacitor(capacitance=0, tolerance=1, **kw)
    #         add_capacitor(res, capacitor_dict[package])
    #
    #         # 1R-10M
    #         for r in ESeries.get_values(1, 10e6, ESeries.E96):
    #             # 1%
    #             res = capacitor(capacitance=r, tolerance=1, **kw)
    #             add_capacitor(res, capacitor_dict[package])
    #             # 0.5%
    #             res = capacitor(capacitance=r, tolerance=0.5, **kw)
    #             add_capacitor(res, capacitor_dict[package])
    #
    # def add_koa(capacitor_dict):
    #     ### Add 0R capacitors
    #     for PACKAGE in ["0201", "0402", "0603", "0805", "1206", "2010", "2512"]:
    #         res = capacitor(
    #             capacitance=0,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=400,
    #             manufacturer="KOA Speer",
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     #########################################################################
    #     PACKAGE = "0201"
    #     #########################################################################
    #     # 10R-10M, 1%
    #     for r in ESeries.get_values(10, 1e6, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=200,
    #             manufacturer="KOA Speer",
    #             rated_voltage=25,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     for r in ESeries.get_values(1.02e6, 10e6, ESeries.E24):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=200,
    #             manufacturer="KOA Speer",
    #             rated_voltage=25,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 1R-9.1R, 1%
    #     for r in ESeries.get_values(1, 9.1, ESeries.E24):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=400,
    #             manufacturer="KOA Speer",
    #             rated_voltage=25,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 10R-1M, 0.5%
    #     for r in ESeries.get_values(10, 1e6, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=0.5,
    #             temp_coefficient=200,
    #             manufacturer="KOA Speer",
    #             rated_voltage=25,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     #########################################################################
    #     PACKAGE = "0402"
    #     #########################################################################
    #     # 10R-10M, 1%
    #     for r in ESeries.get_values(10, 1e6, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=100,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 1R-9.1R, 1.02M-10M 1%
    #     for r in ESeries.get_values(1, 9.1, ESeries.E24) + ESeries.get_values(1.02e6, 10e6, ESeries.E24):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=200,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 10R-1M, 0.5%
    #     for r in ESeries.get_values(10, 1e6, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=0.5,
    #             temp_coefficient=200,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 10R-1M, 0.5%
    #     for r in ESeries.get_values(10, 1e6, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=0.5,
    #             temp_coefficient=100,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     #########################################################################
    #     PACKAGE = "0603"
    #     #########################################################################
    #     # 1.02k-1M, 1%
    #     for r in ESeries.get_values(1.02e3, 1e6, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=100,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 1.02M-10M 1%
    #     for r in ESeries.get_values(1.02e6, 10e6, ESeries.E24):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=200,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 10R-1k 1%
    #     for r in ESeries.get_values(10, 1e3, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=100,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #             power=0.125,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 1R-9.76k 1%
    #     for r in ESeries.get_values(1, 9.76, ESeries.E24):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=200,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #             power=0.125,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     # 1.02k-1M, 0.5%
    #     for r in ESeries.get_values(1.02e3, 1e6, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=0.5,
    #             temp_coefficient=100,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 10R-1k, 0.5%
    #     for r in ESeries.get_values(10, 1e3, ESeries.E96):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=0.5,
    #             temp_coefficient=100,
    #             manufacturer="KOA Speer",
    #             rated_voltage=75,
    #             power=0.125,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     #########################################################################
    #     PACKAGE = "0805"
    #     #########################################################################
    #     # 10-1M
    #     for r in ESeries.get_values(10, 1e6, ESeries.E96):
    #         # 1%
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=100,
    #             manufacturer="KOA Speer",
    #             rated_voltage=150,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #         # 0.5%
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=0.5,
    #             temp_coefficient=100,
    #             manufacturer="KOA Speer",
    #             rated_voltage=150,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 1-9.76 1%
    #     for r in ESeries.get_values(1, 9.76, ESeries.E24):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=200,
    #             manufacturer="KOA Speer",
    #             rated_voltage=150,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #     # 1.02M-10M 1%
    #     for r in ESeries.get_values(1.02e6, 10e6, ESeries.E24):
    #         res = capacitor(
    #             capacitance=r,
    #             package=PACKAGE,
    #             tolerance=1,
    #             temp_coefficient=400,
    #             manufacturer="KOA Speer",
    #             rated_voltage=150,
    #         )
    #         add_capacitor(res, capacitor_dict[PACKAGE])
    #
    #     #########################################################################
    #     packages = ["1206", "2010", "2512"]
    #     #########################################################################
    #     for PACKAGE in packages:
    #         # 10-1M
    #         for r in ESeries.get_values(10, 1e6, ESeries.E96):
    #             # 1%
    #             res = capacitor(
    #                 capacitance=r,
    #                 package=PACKAGE,
    #                 tolerance=1,
    #                 temp_coefficient=100,
    #                 manufacturer="KOA Speer",
    #                 rated_voltage=200,
    #             )
    #             add_capacitor(res, capacitor_dict[PACKAGE])
    #             # 0.5%
    #             res = capacitor(
    #                 capacitance=r,
    #                 package=PACKAGE,
    #                 tolerance=0.5,
    #                 temp_coefficient=100,
    #                 manufacturer="KOA Speer",
    #                 rated_voltage=200,
    #             )
    #             add_capacitor(res, capacitor_dict[PACKAGE])
    #         # 1-9.76 1%
    #         for r in ESeries.get_values(1, 9.76, ESeries.E24) + ESeries.get_values(1.02e6, 5.6e6, ESeries.E24):
    #             res = capacitor(
    #                 capacitance=r,
    #                 package=PACKAGE,
    #                 tolerance=1,
    #                 temp_coefficient=200,
    #                 manufacturer="KOA Speer",
    #                 rated_voltage=200,
    #             )
    #             add_capacitor(res, capacitor_dict[PACKAGE])
    #         # 5.62M-10M 1%
    #         for r in ESeries.get_values(5.62e6, 10e6, ESeries.E24):
    #             res = capacitor(
    #                 capacitance=r,
    #                 package=PACKAGE,
    #                 tolerance=1,
    #                 temp_coefficient=400,
    #                 manufacturer="KOA Speer",
    #                 rated_voltage=200,
    #             )
    #             add_capacitor(res, capacitor_dict[PACKAGE])

    def add_murata(cap_dict):
        _root = os.path.dirname(__file__)

        with open(os.path.join(_root, "docs/Murata GCM Parts List.csv"), "r") as f:
            reader = DictReader(f)
            for cfg in reader:
                cap = create_gcm_cap(cfg["Part Number"])
                if cap is None:
                    continue
                add_capacitor(cap, cap_dict[cap.package])
                print()

    capacitors = {
        "0201": {},
        "0402": {},
        "0603": {},
        "0805": {},
        "1206": {},
        "1210": {},
        "2010": {},
        "2512": {},
    }

    # add_vishay(capacitors)
    # add_yageo(capacitors)
    # add_koa(capacitors)
    add_murata(capacitors)

    # Convert to multisourced
    capacitor_sets = {}
    for package, instances in capacitors.items():
        capacitor_sets[package] = {}
        for name, entry in instances.items():
            capacitor_sets[package][name] = CapacitorSet(entry)

    return capacitor_sets


if __name__ == "__main__":
    capacitors = compile_capacitor_pn_list()
    print()
