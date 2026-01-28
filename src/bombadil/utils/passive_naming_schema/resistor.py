import json
import os

import requests.packages
from mypy_extensions import KwArg

from bombadil.utils.passive_naming_schema.series import ESeries
from bombadil.utils.metric_formatting import MetricValue
from bombadil import colored_logger

logger = colored_logger("Resistor Part Numbers")


class VISHAY_CRCW:
    _PN_MAPPING = {
        "type/size": {
            "0201": "CRCW0201",
            "0402": "CRCW0402",
            "0603": "CRCW0603",
            "0805": "CRCW0805",
            "1206": "CRCW1206",
            "2010": "CRCW2010",
            "2512": "CRCW2512",
        },
        "tolerance": {
            1: "F",
            5: "J",
            "JUMPER": "Z",
        },
        "temp_coeff": {
            100: "K",
            200: "N",
            400: "X",
            "JUMPER": "0",
        },
        "reel": {
            "0201": ["ED", "EI", "EE"],
            "0402": ["ED", "EE"],
            "0603": ["ED", "EI", "EE"],
            "0805": ["EA", "EC"],
            "1206": ["EA", "EC"],
            "2010": ["EF"],
            "2512": ["EG", "EH"],
        },
    }

    @staticmethod
    def get_pn(resistor):
        series = VISHAY_CRCW._PN_MAPPING["type/size"][resistor.package]

        resistance = resistor.resistance
        reel_str = VISHAY_CRCW._PN_MAPPING["reel"][resistor.package][0]
        if resistance == 0:
            res_str = "0000"
            tol_str = VISHAY_CRCW._PN_MAPPING["tolerance"]["JUMPER"]
            temp_co_str = VISHAY_CRCW._PN_MAPPING["temp_coeff"]["JUMPER"]
        else:
            res_str = MetricValue.num_to_prefix_as_decimal_str(resistance, default_decimal="R", str_length=4)
            tol_str = VISHAY_CRCW._PN_MAPPING["tolerance"][resistor.tolerance]
            temp_co_str = VISHAY_CRCW._PN_MAPPING["temp_coeff"][resistor.temp_coefficient]

        return f"{series}{res_str}{tol_str}{temp_co_str}{reel_str}"  # TODO decide on how to handle packaging


class YAGEO_AC:
    _PN_MAPPING = {
        "type/size": {
            "0201": "0201",
            "0402": "0402",
            "0603": "0603",
            "0805": "0805",
            "1206": "1206",
            "1210": "1210",
            "1218": "1218",
            "2010": "2010",
            "2512": "2512",
        },
        "tolerance": {
            0.1: "B",
            0.5: "D",
            1: "F",
            5: "J",
        },
        "packaging": {
            "paper_reel": "R",
            "embossed_reel": "K",
        },
        "temp_coeff": {
            "spec": "-",
            50: "E",
        },
        "reel": {
            "7in standard power": "07",
            "13in standard power": "13",
            "7in standard 2x power": "7W",
            "13in standard 2x power": "3W",
        },
    }

    PACKAGING = "paper_reel"
    REEL = "7in standard power"
    TEMP_CO = "spec"

    @staticmethod
    def get_pn(resistor):
        series = YAGEO_AC._PN_MAPPING["type/size"][resistor.package]

        resistance = resistor.resistance
        res_str = MetricValue.num_to_prefix_as_decimal_str(resistance, default_decimal="R", str_length=4).rstrip("0")
        tol_str = YAGEO_AC._PN_MAPPING["tolerance"][resistor.tolerance]
        temp_co_str = YAGEO_AC._PN_MAPPING["temp_coeff"][YAGEO_AC.TEMP_CO]
        if resistor.package in ["1218", "2010", "2512"]:
            packaging = YAGEO_AC._PN_MAPPING["packaging"]["embossed_reel"]
        else:
            packaging = YAGEO_AC._PN_MAPPING["packaging"]["paper_reel"]
        reel_str = YAGEO_AC._PN_MAPPING["reel"][YAGEO_AC.REEL]

        return f"AC{series}{tol_str}{packaging}{temp_co_str}{reel_str}{res_str}L"


class KOA_RK73H:

    _PN_MAPPING = {
        "type/size": {
            "0201": "1H",
            "0402": "1E",
            "0603": "1J",
            "0805": "2A",
            "1206": "2B",
            "1210": "2E",
            "2010": "2H",
            "2512": "3A",
        },
        "tolerance": {
            0.5: "D",
            1: "F",
        },
        "reel": {
            "0201": "TC",
            "0402": "TP",
            "2010": "TE",
            "2512": "TE",
            "all others": "TD",
        },
    }
    SERIES = "RK73H"
    PACKAGING = "paper_reel"
    REEL = "2mm pitch punch paper"
    TEMP_CO = "spec"

    @staticmethod
    def get_pn(resistor):

        resistance = resistor.resistance

        if resistance == 0:
            jumper_mapping = {
                "0201": "RK73Z1HTTC",
                "0402": "RK73Z1ETTP",
                "0603": "RK73Z1JTTD",
                "0805": "RK73Z2ATTD",
                "1206": "RK73Z2BTTD",
                "2010": "RK73Z2HTTE",
                "2512": "RK73Z3ATTE",
            }
            return jumper_mapping[resistor.package]

        package_str = KOA_RK73H._PN_MAPPING["type/size"][resistor.package]
        tol_str = KOA_RK73H._PN_MAPPING["tolerance"][resistor.tolerance]

        if resistance < 100:
            res_str = "{:2.2f}".format(resistance).replace(".", "R")[:4]
        else:
            res_str = str(resistance)
            num = res_str[:3]
            multiplier = len(res_str[3:])
            res_str = f"{num}{multiplier}"

        reel_str = KOA_RK73H._PN_MAPPING["reel"].get(resistor.package, "TD")

        return f"RK73H{package_str}T{reel_str}{res_str}{tol_str}"


class Resistor:
    package: str
    power: float
    rated_voltage: float
    resistance: float
    temp_coefficient: float
    tolerance: float
    temp_min: float
    temp_max: float

    PACKAGE_DEFAULTS = {
        "0201": {
            "power": 0.05,
            "voltage": 25,
        },
        "0402": {
            "power": 0.063,
            "voltage": 50,
        },
        "0603": {
            "power": 0.1,
            "voltage": 75,
        },
        "0805": {
            "power": 0.125,
            "voltage": 150,
        },
        "1206": {
            "power": 0.25,
            "voltage": 200,
        },
        "1210": {
            "power": 0.5,
            "voltage": 200,
        },
        "1218": {
            "power": 1,
            "voltage": 200,
        },
        "2010": {
            "power": 0.75,
            "voltage": 200,
        },
        "2512": {
            "power": 1,
            "voltage": 200,
        },
    }

    def __init__(
        self,
        package,
        resistance,
        tolerance,
        temp_coefficient,
        manufacturer,
        power=None,
        rated_voltage=None,
        temp_min=-55,
        temp_max=155,
    ):
        self.package = package
        self.resistance = resistance
        self.tolerance = tolerance
        self.temp_coefficient = temp_coefficient
        self.manufacturer = manufacturer
        self.power = power
        self.rated_voltage = rated_voltage
        self.temperature_min = temp_min
        self.temperature_max = temp_max

        defaults = self.PACKAGE_DEFAULTS.get(self.package, {})
        if self.power is None:
            self.power = defaults.get("power")
        if self.rated_voltage is None:
            self.rated_voltage = defaults.get("voltage")

    @property
    def name(self):
        return f"RES,{self.package},{self.resistance_str_prefix_delimited},{self.tolerance}%,{self.power},{self.rated_voltage}"

    @property
    def name_short(self):
        return f"RES,{self.package},{self.resistance_str_prefix_delimited},{self.tolerance}%"

    @property
    def resistance_str(self):
        return MetricValue.num_to_str(self.resistance, units="Ohm")

    @property
    def resistance_str_prefix_delimited(self):
        return MetricValue.num_to_prefix_as_decimal_str(self.resistance, default_decimal="R", str_length=4)

    @property
    def part_number(self):
        mfg_mapping = {"Vishay": VISHAY_CRCW.get_pn, "Yageo": YAGEO_AC.get_pn, "KOA Speer": KOA_RK73H.get_pn}
        pn_func = mfg_mapping.get(self.manufacturer)
        if pn_func is None:
            logger.warning("Could not derive a PN")
            return False
        return pn_func(self)


class ResistorSet:
    def __init__(self, resistors={}):
        self.resistors = resistors
        self._validate_components()

    def _validate_components(self):
        """Brute force shcek to make sure there
        are no fatal errors"""
        vals = self._get_component_vals_dict()

        all_same = lambda k: len(list(set(vals[k]))) == 1

        assert all_same("package")
        assert all_same("resistance")

    def _get_component_vals_dict(self):
        """Compile a dictionary opf all component values"""
        vals = {}
        for k in list(self.resistors.values())[0].__dict__.keys():
            vals[k] = [getattr(r, k) for r in self.resistors.values()]
        return vals

    @property
    def name(self):
        vals = self._get_component_vals_dict()

        return f"RES,{self.package},{self.resistance_str_prefix_delimited},{self.tolerance}%,{self.power}W,{self.rated_voltage}V,{self.temp_coefficient}ppm"

    @property
    def resistance_str_prefix_delimited(self):
        return list(self.resistors.values())[0].resistance_str_prefix_delimited

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
    def resistance(self):
        vals = self._get_component_vals_dict()
        resistance = vals["resistance"][0]
        return resistance


def compile_resistor_pn_list():
    def add_resistor(resistor, target):
        key = resistor.name_short
        # key = resistor.resistance
        if key not in target:
            target[key] = {}
        pn = resistor.part_number
        if pn:
            target[key][pn] = resistor

    def add_vishay(resistor_dict):
        ###################################################################################
        ### 0201                                                                        ###
        ###################################################################################
        PACKAGE = "0201"

        kw = {
            "package": PACKAGE,
            "tolerance": 1,
            "temp_coefficient": 200,
            "manufacturer": "Vishay",
            "rated_voltage": 25,
        }

        ### 0R
        res = Resistor(resistance=0, **kw)
        add_resistor(res, resistor_dict[PACKAGE])

        # 10R-10M
        for r in ESeries.get_values(10, 10e6, ESeries.E96):
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

        ### 1R-9.76R
        for r in ESeries.get_values(1, 9.76, ESeries.E96):
            kw["temp_coefficient"] = 400
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

        ###################################################################################
        ### 0402                                                                        ###
        ###################################################################################
        PACKAGE = "0402"

        kw = {
            "package": PACKAGE,
            "tolerance": 1,
            "temp_coefficient": 100,
            "manufacturer": "Vishay",
            "rated_voltage": 75,
            "power": 0.1,
        }

        ### 0R
        res = Resistor(resistance=0, **kw)
        add_resistor(res, resistor_dict[PACKAGE])

        # 1R-10M
        for r in ESeries.get_values(1, 10e6, ESeries.E96):
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

        ###################################################################################
        ### 0603                                                                        ###
        ###################################################################################
        PACKAGE = "0603"

        kw = {
            "package": PACKAGE,
            "tolerance": 1,
            "temp_coefficient": 100,
            "manufacturer": "Vishay",
            "rated_voltage": 75,
            "power": 0.125,
        }

        ### 0R
        res = Resistor(resistance=0, **kw)
        add_resistor(res, resistor_dict[PACKAGE])

        # 1R-10M
        for r in ESeries.get_values(1, 10e6, ESeries.E96):
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

        ###################################################################################
        ### 0805                                                                        ###
        ###################################################################################
        PACKAGE = "0805"

        kw = {
            "package": PACKAGE,
            "tolerance": 1,
            "temp_coefficient": 100,
            "manufacturer": "Vishay",
            "rated_voltage": 125,
            "power": 0.15,
        }

        ### 0R
        res = Resistor(resistance=0, **kw)
        add_resistor(res, resistor_dict[PACKAGE])

        # 1R-10M
        for r in ESeries.get_values(1, 10e6, ESeries.E96):
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

        ###################################################################################
        packages = ["1206", "2010", "2512"]
        ###################################################################################
        for PACKAGE in packages:
            kw = {
                "package": PACKAGE,
                "tolerance": 1,
                "temp_coefficient": 100,
                "manufacturer": "Vishay",
            }

            ### 0R
            res = Resistor(resistance=0, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

            # 1R-10M
            for r in ESeries.get_values(1, 10e6, ESeries.E96):
                res = Resistor(resistance=r, **kw)
                add_resistor(res, resistor_dict[PACKAGE])

        # TODO add larger packages

    def add_yageo(resistor_dict):
        ###################################################################################
        ### 0201                                                                        ###
        ###################################################################################
        PACKAGE = "0201"

        kw = {
            "package": PACKAGE,
            "tolerance": 1,
            "temp_coefficient": 200,
            "manufacturer": "Yageo",
            "rated_voltage": 30,
        }

        # ### 0R
        # res = Resistor(resistance=0, **kw)
        # add_resistor(res, resistor_dict[PACKAGE])

        # 1R-10M, 1%
        for r in ESeries.get_values(1, 10e6, ESeries.E96):
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])
        # 10R-1M, 0.5%
        kw["tolerance"] = 0.5
        for r in ESeries.get_values(10, 1e6, ESeries.E96):
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

        ###################################################################################
        ### Others                                                                      ###
        ###################################################################################
        for package in ["0402", "0603", "0805", "1206", "2010", "2512"]:
            kw = {
                "package": package,
                "temp_coefficient": 100,
                "manufacturer": "Yageo",
            }

            ### 0R
            res = Resistor(resistance=0, tolerance=1, **kw)
            add_resistor(res, resistor_dict[package])

            # 1R-10M
            for r in ESeries.get_values(1, 10e6, ESeries.E96):
                # 1%
                res = Resistor(resistance=r, tolerance=1, **kw)
                add_resistor(res, resistor_dict[package])
                # 0.5%
                res = Resistor(resistance=r, tolerance=0.5, **kw)
                add_resistor(res, resistor_dict[package])

    def add_koa(resistor_dict):
        ### Add 0R resistors
        for PACKAGE in ["0201", "0402", "0603", "0805", "1206", "2010", "2512"]:
            res = Resistor(
                resistance=0,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=400,
                manufacturer="KOA Speer",
            )
            add_resistor(res, resistor_dict[PACKAGE])

        #########################################################################
        PACKAGE = "0201"
        #########################################################################
        # 10R-10M, 1%
        for r in ESeries.get_values(10, 1e6, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=200,
                manufacturer="KOA Speer",
                rated_voltage=25,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        for r in ESeries.get_values(1.02e6, 10e6, ESeries.E24):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=200,
                manufacturer="KOA Speer",
                rated_voltage=25,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 1R-9.1R, 1%
        for r in ESeries.get_values(1, 9.1, ESeries.E24):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=400,
                manufacturer="KOA Speer",
                rated_voltage=25,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 10R-1M, 0.5%
        for r in ESeries.get_values(10, 1e6, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=0.5,
                temp_coefficient=200,
                manufacturer="KOA Speer",
                rated_voltage=25,
            )
            add_resistor(res, resistor_dict[PACKAGE])

        #########################################################################
        PACKAGE = "0402"
        #########################################################################
        # 10R-10M, 1%
        for r in ESeries.get_values(10, 1e6, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=100,
                manufacturer="KOA Speer",
                rated_voltage=75,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 1R-9.1R, 1.02M-10M 1%
        for r in ESeries.get_values(1, 9.1, ESeries.E24) + ESeries.get_values(1.02e6, 10e6, ESeries.E24):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=200,
                manufacturer="KOA Speer",
                rated_voltage=75,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 10R-1M, 0.5%
        for r in ESeries.get_values(10, 1e6, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=0.5,
                temp_coefficient=200,
                manufacturer="KOA Speer",
                rated_voltage=75,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 10R-1M, 0.5%
        for r in ESeries.get_values(10, 1e6, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=0.5,
                temp_coefficient=100,
                manufacturer="KOA Speer",
                rated_voltage=75,
            )
            add_resistor(res, resistor_dict[PACKAGE])

        #########################################################################
        PACKAGE = "0603"
        #########################################################################
        # 1.02k-1M, 1%
        for r in ESeries.get_values(1.02e3, 1e6, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=100,
                manufacturer="KOA Speer",
                rated_voltage=75,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 1.02M-10M 1%
        for r in ESeries.get_values(1.02e6, 10e6, ESeries.E24):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=200,
                manufacturer="KOA Speer",
                rated_voltage=75,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 10R-1k 1%
        for r in ESeries.get_values(10, 1e3, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=100,
                manufacturer="KOA Speer",
                rated_voltage=75,
                power=0.125,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 1R-9.76k 1%
        for r in ESeries.get_values(1, 9.76, ESeries.E24):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=200,
                manufacturer="KOA Speer",
                rated_voltage=75,
                power=0.125,
            )
            add_resistor(res, resistor_dict[PACKAGE])

        # 1.02k-1M, 0.5%
        for r in ESeries.get_values(1.02e3, 1e6, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=0.5,
                temp_coefficient=100,
                manufacturer="KOA Speer",
                rated_voltage=75,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 10R-1k, 0.5%
        for r in ESeries.get_values(10, 1e3, ESeries.E96):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=0.5,
                temp_coefficient=100,
                manufacturer="KOA Speer",
                rated_voltage=75,
                power=0.125,
            )
            add_resistor(res, resistor_dict[PACKAGE])

        #########################################################################
        PACKAGE = "0805"
        #########################################################################
        # 10-1M
        for r in ESeries.get_values(10, 1e6, ESeries.E96):
            # 1%
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=100,
                manufacturer="KOA Speer",
                rated_voltage=150,
            )
            add_resistor(res, resistor_dict[PACKAGE])
            # 0.5%
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=0.5,
                temp_coefficient=100,
                manufacturer="KOA Speer",
                rated_voltage=150,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 1-9.76 1%
        for r in ESeries.get_values(1, 9.76, ESeries.E24):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=200,
                manufacturer="KOA Speer",
                rated_voltage=150,
            )
            add_resistor(res, resistor_dict[PACKAGE])
        # 1.02M-10M 1%
        for r in ESeries.get_values(1.02e6, 10e6, ESeries.E24):
            res = Resistor(
                resistance=r,
                package=PACKAGE,
                tolerance=1,
                temp_coefficient=400,
                manufacturer="KOA Speer",
                rated_voltage=150,
            )
            add_resistor(res, resistor_dict[PACKAGE])

        #########################################################################
        packages = ["1206", "2010", "2512"]
        #########################################################################
        for PACKAGE in packages:
            # 10-1M
            for r in ESeries.get_values(10, 1e6, ESeries.E96):
                # 1%
                res = Resistor(
                    resistance=r,
                    package=PACKAGE,
                    tolerance=1,
                    temp_coefficient=100,
                    manufacturer="KOA Speer",
                    rated_voltage=200,
                )
                add_resistor(res, resistor_dict[PACKAGE])
                # 0.5%
                res = Resistor(
                    resistance=r,
                    package=PACKAGE,
                    tolerance=0.5,
                    temp_coefficient=100,
                    manufacturer="KOA Speer",
                    rated_voltage=200,
                )
                add_resistor(res, resistor_dict[PACKAGE])
            # 1-9.76 1%
            for r in ESeries.get_values(1, 9.76, ESeries.E24) + ESeries.get_values(1.02e6, 5.6e6, ESeries.E24):
                res = Resistor(
                    resistance=r,
                    package=PACKAGE,
                    tolerance=1,
                    temp_coefficient=200,
                    manufacturer="KOA Speer",
                    rated_voltage=200,
                )
                add_resistor(res, resistor_dict[PACKAGE])
            # 5.62M-10M 1%
            for r in ESeries.get_values(5.62e6, 10e6, ESeries.E24):
                res = Resistor(
                    resistance=r,
                    package=PACKAGE,
                    tolerance=1,
                    temp_coefficient=400,
                    manufacturer="KOA Speer",
                    rated_voltage=200,
                )
                add_resistor(res, resistor_dict[PACKAGE])

    resistors = {
        "0201": {},
        "0402": {},
        "0603": {},
        "0805": {},
        "1206": {},
        "2010": {},
        "2512": {},
    }

    add_vishay(resistors)
    add_yageo(resistors)
    add_koa(resistors)

    # Convert to multisourced
    resistor_sets = {}
    for package, instances in resistors.items():
        resistor_sets[package] = {}
        for name, entry in instances.items():
            resistor_sets[package][name] = ResistorSet(entry)

    return resistor_sets


if __name__ == "__main__":
    resistors = compile_resistor_pn_list()
    print()
