from galvanic.utils.metric_formatting import METRIC_PREFIX


class VISHAY_CRCW:
    _PN_MAPPING = {
        "type/size": {
            "0201": "CRCW0201",
            "0402": "CRCW0402",
            "0603": "CRCW0603",
            "0805": "CRCW0805",
            "1206": "CRCW01206",
        },
    }

    @staticmethod
    def get_pn(resistor):
        VISHAY_CRCW._PN

    @staticmethod
    def parse_resistance_string(resistance_string):
        resistance = None
        return resistance


class Resistor:
    package: str
    power: float
    rated_voltage: float
    resistance: float
    temp_coefficient: float
    tolerance: float

    def __init__(self, name, package, power, rated_voltage, resistance, temp_coefficient, tolerance):
        self.package = package
        self.power = power
        self.rated_voltage = rated_voltage
        self.resistance = resistance
        self.temp_coefficient = temp_coefficient
        self.tolerance = tolerance

    @property
    def name(self):

        return f"RES,{self.package},{self.power},{self.rated_voltage},{self.resistance},{self.temp_coefficient}"

    @property
    def resistance_str(self):
        return

    @property
    def PN_VISHAY_CRCW(self):
        return VISHAY_CRCW.get_pn(self)

    # @classmethod
    # def from_part_number(cls, part_number):
    #     return cls


if __name__ == "__main__":
    r = Resistor()
