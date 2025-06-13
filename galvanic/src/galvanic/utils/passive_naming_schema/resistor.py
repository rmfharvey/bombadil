import json
import os
from galvanic.utils.passive_naming_schema.series import ESeries
from galvanic.utils.metric_formatting import MetricValue
from galvanic import colored_logger

logger = colored_logger("Resistor Part Numbers")


class VISHAY_CRCW:
    _PN_MAPPING = {
        "type/size": {
            "0201": "CRCW0201",
            "0402": "CRCW0402",
            "0603": "CRCW0603",
            "0805": "CRCW0805",
            "1206": "CRCW01206",
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
    }

    @staticmethod
    def get_pn(resistor):
        series = VISHAY_CRCW._PN_MAPPING["type/size"][resistor.package]

        resistance = resistor.resistance
        if resistance == 0:
            res_str = "0000"
            tol_str = VISHAY_CRCW._PN_MAPPING["tolerance"]["JUMPER"]
            temp_co_str = VISHAY_CRCW._PN_MAPPING["temp_coeff"]["JUMPER"]
        else:
            res_str = MetricValue.num_to_prefix_as_decimal_str(resistance, default_decimal="R", str_length=4)
            tol_str = VISHAY_CRCW._PN_MAPPING["tolerance"][resistor.tolerance]
            temp_co_str = VISHAY_CRCW._PN_MAPPING["temp_coeff"][resistor.temp_coefficient]

        return f"{series}{res_str}{tol_str}{temp_co_str}"  # TODO decide on how to handle packaging

    # @staticmethod
    # def (resistance_string):
    #     resistance = None
    #     return resistance


class Resistor:
    package: str
    power: float
    rated_voltage: float
    resistance: float
    temp_coefficient: float
    tolerance: float

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
    }

    def __init__(self, package, resistance, tolerance, temp_coefficient, manufacturer, power=None, rated_voltage=None):
        self.package = package
        self.resistance = resistance
        self.tolerance = tolerance
        self.temp_coefficient = temp_coefficient
        self.manufacturer = manufacturer
        self.power = power
        self.rated_voltage = rated_voltage

        defaults = self.PACKAGE_DEFAULTS.get(self.package, {})
        if self.power is None:
            self.power = defaults.get("power")
        if self.rated_voltage is None:
            self.rated_voltage = defaults.get("voltage")

    @property
    def name(self):
        return f"RES,{self.package},{self.resistance},{self.power},{self.rated_voltage}"

    @property
    def resistance_str(self):
        return MetricValue.num_to_str(self.resistance, units="Ohm")

    @property
    def part_number(self):
        mfg_mapping = {"Vishay": VISHAY_CRCW.get_pn}
        pn_func = mfg_mapping.get(self.manufacturer)
        if pn_func is None:
            logger.warning("Could not derive a PN")
            return False
        return pn_func(self)


class ResistorSet:
    def __init__(self, resistors={}):
        self.resistors = resistors

    def add_resistor(self, part_number, resistor):
        self.resistors[part_number] = resistor


if __name__ == "__main__":

    def add_resistor(resistor, target):
        if resistor.resistance not in target:
            target[resistor.resistance] = {}
        pn = resistor.part_number
        if pn:
            target[resistor.resistance][pn] = resistor

    def add_vishay(resistor_dict):
        ###################################################################################
        ### 0201                                                                        ###
        ###################################################################################
        PACKAGE = "0201"

        kw = {
            "package": PACKAGE,
            "tolerance": 1,
            "temp_coefficient": 100,
            "manufacturer": "Vishay",
            "rated_voltage": 30,
        }

        ### 0R
        res = Resistor(resistance=0, **kw)
        add_resistor(res, resistor_dict[PACKAGE])

        # 47R-1M
        for r in ESeries.get_values(47, 1e6, ESeries.E96):
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

        ### 10R-47R, 1M-10M
        rvals = ESeries.get_values(10, 46.99, ESeries.E96) + ESeries.get_values(1.0001e6, 10e6, ESeries.E96)
        for r in rvals:
            kw["temp_coefficient"] = 200
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
        ### 1206                                                                        ###
        ###################################################################################
        PACKAGE = "1206"

        kw = {
            "package": PACKAGE,
            "tolerance": 1,
            "temp_coefficient": 100,
            "manufacturer": "Vishay",
            "rated_voltage": 200,
            "power": 0.25,
        }

        ### 0R
        res = Resistor(resistance=0, **kw)
        add_resistor(res, resistor_dict[PACKAGE])

        # 1R-10M
        for r in ESeries.get_values(1, 10e6, ESeries.E96):
            res = Resistor(resistance=r, **kw)
            add_resistor(res, resistor_dict[PACKAGE])

    resistors = {
        "0201": {},
        "0402": {},
        "0603": {},
        "0805": {},
        "1206": {},
    }

    add_vishay(resistors)

    print()
