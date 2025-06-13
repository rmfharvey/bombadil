import json
import os
from galvanic.utils.metric_formatting import MetricValue


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

        res_str = MetricValue.num_to_prefix_as_decimal_str(resistance, default_decimal="R", str_length=4)
        tol_str = VISHAY_CRCW._PN_MAPPING["tolerance"][resistor.tolerance]
        temp_co_str = VISHAY_CRCW._PN_MAPPING["temp_coeff"][resistor.temp_coeff]

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

    def __init__(self, package, power, rated_voltage, resistance, temp_coefficient, tolerance):
        self.package = package
        self.power = power
        self.rated_voltage = rated_voltage
        self.resistance = resistance
        self.temp_coefficient = temp_coefficient
        self.tolerance = tolerance

    @property
    def name(self):
        return f"RES,{self.package},{self.resistance},{self.power},{self.rated_voltage}"

    @property
    def resistance_str(self):
        return MetricValue.num_to_str(self.resistance, units="Ohm")

    @property
    def PN_VISHAY_CRCW(self):
        return VISHAY_CRCW.get_pn(self)

    # @classmethod
    # def from_part_number(cls, part_number):
    #     return cls


if __name__ == "__main__":
    from galvanic.utils.metric_formatting import MetricValue

    r = Resistor()
