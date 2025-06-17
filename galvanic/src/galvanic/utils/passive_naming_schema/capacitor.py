import csv
import json
import os
import time
import requests
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
        return f"CAP,{self.package},{self.capacitance_str},{self.rated_voltage}V,{self.dielectric},{self.tolerance}%,"

    @property
    def name_short(self):
        return f"CAP,{self.package},{self.capacitance_str},{self.rated_voltage}V,{self.dielectric}"

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
            "B": 0.1,  # pF
            "C": 0.25,  # pF
            "D": 0.5,  # pF
            "F": 1,
            "G": 2,
            "J": 5,
            "K": 10,
            "M": 20,
            "W": 0.05,  # pF
        },
    }
    absolute_tolerance_code = ["B", "C", "D", "W"]

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

        if tolerance in absolute_tolerance_code:
            if abs(capacitance) == "D" and capacitance >= 10e-12:
                tolerance = mapping["tolerance"][tolerance]
            else:
                tolerance = round(mapping["tolerance"][tolerance] * 1e-12 / capacitance, 2)

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


def create_tdk_cap(cfg):
    print()
    # Package
    idx = cfg["L x W Size"].index("[EIA ") + 5
    package = cfg["L x W Size"][idx:].replace("]", "")

    # Capacitance
    capacitance = MetricValue(cfg["Capacitance"])

    cap = Capacitor(
        package=package,
        capacitance=None,
        rated_voltage=None,
        dielectric=None,
        tolerance=None,
        height=None,
        temp_min=None,
        temp_max=None,
        manufacturer=None,
        part_number=None,
    )
    return cap


# def create_tdk_cap(ref_cap):
#     _mapping = {
#         "package": {
#             "0201": "1",
#             "0402": "2",
#             "0603": "3",
#             "0805": "4",
#             "1206": "5",
#             "1210": "6",
#         }
#     }
#     print()
#
#
# def validate_tdk_cga_pn(part_number):
#     """Poll TDK website to see if a part number is valid
#
#     :param str part_number: TDK Part Number
#     :return: True if part number is valid, False otherwise
#     """
#     init = time.perf_counter()
#     response = requests.get(
#         "https://product.tdk.com/en/search/capacitor/ceramic/mlcc/info",
#         params={"part_no": part_number},
#         headers={
#             "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#             "accept-language": "en-US,en;q=0.9",
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
#             "cookie": 'mnP2JcU=c1298358-0c08-4b0b-a6a0-c78a502dd01c:::2; mnP2Bp=0:::2; _ga_JJX8KLL9VX=GS2.1.s1748907533$o1$g0$t1748907533$j60$l0$h341104586; _ga=GA1.1.1671220868.1748907533; _ga_GZ87R73H9Q=GS2.1.s1748907533$o1$g0$t1748907533$j60$l0$h0; _clck=1a1a1o1%7C2%7Cfwf%7C0%7C1979; FPID=FPID2.2.XnStJBc%2BLukxpJGww66i6AvwKYhoxjhB1wjQtgHcnk8%3D.1748907533; MN73umVg_Z=7f102d6d-6df3-8cb7-e17b-a0b4a972f248:::2; ak_bmsc=EB8ED2D8E49C57872C8417DD09BFADEC~000000000000000000000000000000~YAAQpi0+F3f0tniXAQAARtiKehx2/IxWUdiALMeem6jdFD2XQi3K2xw33Spu+OB9U52iI5hV0AoYNQxDX2dO0aV6eZTSpLVS55e3ZvY1dJ/aYtC1VEbeDteBb1Dy61cTsotG/V5aGGyYKU0CigxWNVPwCX217HygABurRA1R+sf+lBlIG0jrSso79Ogkubc5zgH4Jjh+AXYEwEE36+xSnFw+XzGnyOedJragm7/mTfe8/3KhFdGEC+gl1B+T/sbaekxo+L7WREbT43oZ22LC076RSUxD2JZgWVKdiAUhmZN5VZnquaY7iLTI6DtWaB+mriuFJvmzBF7mcrxJEQcmQh1ySTw10htaSItDyAY07c6QyEMuWr1G6F6a2O6SctvLijq+9hY=; ps_ls=0; wooTracker=fg8FplIcDqYB; __ss=1750107622173; __ss_referrer=https%3A//product.tdk.com/en/search/capacitor/ceramic/mlcc/info%3Fpart_no%3DCGA1A2X7R1E101K030BA; _ugpid=UoJtEDSL6zDdCVMO.2; __ss_tk=202506%7C683e360e3f1bd778817e0164; _gcl_au=1.1.1167356640.1750107625; mh8ciXI-3a7HfloWZ=google.com:::2; mh8oobaIFjn3V=:::2; mh8oobaJ7gi=:::2; mh8oobaC7SeJd=:::2; mhX5qX4=b577905a-9732-452c-ba1e-44e221d61e4a:::2; mhX5qkaIKPnI=1750107626:::2; mhX5ik=0:::2; mhX5qk95=73bb8c76-9ade-4c99-93b7-3a58f33d6ddf:::2; MHD6Ph5HlS=7f102d6d-6df3-8cb7-e17b-a0b4a972f248:::2; FPLC=SK4%2FCedV96d7IjlKSvWBbkLCUc2F0yKkyLR3wYIIUrXCu%2FxDbj3A8A61ehwSxBg7woiCQenfqIxMv3%2F9hP23ZsY9M80n5czfAWAtzA2wtGA6KhxgoP20kdFR%2BXWogQ%3D%3D; ELOQUA=GUID=C4565C7C14A442D3BBE20EB177D410B0; __ss_initial_referrer=https%3A//www.google.com/; bm_sz=D2A0B760F1C608580D78472209CCE91A~YAAQpi0+FwgBt3iXAQAAu0OMehxAU5jfHqeVWxZafXnq2LqS9sn/0fEc+i29LmXv7PCNrwYyf2fxl30LxJQ4Gm+jdnq7zFAPxKopQUXYs87WRObBEzo09fi87rHXTtgzPkfpbeDeGvupiCQY4B+dckIglWKuzS89QEAbAXXjp+ssPa6ROCroSci6ssMoWIegHWIHRiwiruc2WKGw2doix1fCM6fDxk9BKnmTiqAMOce2AaYZN0XqA+sfqp0o7l8GnoTgTS4e32vHHMVElngqkx1GTHRAVwRfBRHh+i09JnYPrEEJtrHklWHeLpNtFt4zgOcHh83iLgcPSFrXeq50bAOu7S3sCfpEAhQAX44/3WFC1aZ+l0KHl3Q5MSVlB1v1YvhTAzukHZpk4Dv1PsHgPvMsbV9ClF36r8I=~4272693~4408880; _uetsid=eb048d704af411f094d2bf628fc3fd1c; _uetvid=eb04bb504af411f0820e450ff86d866f; _ga_L03JBTW2NL=GS2.1.s1750107625$o2$g1$t1750107703$j60$l0$h0; _ga_DEXMV98BYD=GS2.1.s1750107625$o1$g1$t1750107703$j60$l0$h1573566561; mhX5kka4FjjI=2:::2; mhX5kk95=a6d0bde3-7349-4f7e-92af-9883296fb632:::2; mhX5kkaIKPnI=1750107703:::2; product_search_fw=eyJpdiI6ImZEelh1V3BuaXJ1RTRRSmcyRStxTEE9PSIsInZhbHVlIjoiYTJLN1BUODA0ZjBjZGFtTFIvU1BkT3IraXowSmg5aEg3K0hwNlgyYytUVXVVN3Q3RWZ3RHFjMDc0L1VmSngxRGcyU1Avc29md2pHemQrQVlKWGk5VHNFdkJ3VldNQ2lJbGxGWUxDQ3QreDFaVnRrRVNvZGV5aU5ZMDBVYktKZVQiLCJtYWMiOiI1ZjJiODgxNzc2MDc3OTVlMjg5ODUxMDNiNGI2Y2EwMzRiZWIwOGFmNmY1MWZjNTMzYmNjYzgxODNjN2I0YmRhIiwidGFnIjoiIn0%3D; bm_sv=8347407613529CF2162C5D095CBAEB19~YAAQpi0+FygBt3iXAQAAY0iMehxzjjUZIzP1B8J56jo4cAHUwjLTFOYWtUQZtNoJujvfk4gfCCcTPvp+4wxqEIsa0KZ9odUDrZ3xQLyuNe7bwEOJDhATTS70s2przIcIk40A28UYuFgfRYwcHt6IO8tqmtH7DG4tbplVMNIuoWJp9r61dfjA1T8Q19hC+aZ0zaxKhskZbbXyHCKiN1rytBuIK/TU8fvT4GVLR2F/v8LnUh8kh5QcnuvnoAke4A==~1; _abck=DE415CCC93E96E84A6AE008C732E9BB8~-1~YAAQpi0+FzgBt3iXAQAA50uMeg6ULiypILa6+Ds9msHwhCSVD2Wqc/vEddG4uylHiposTDSRbw64ioAomYTowGaILJMyt8nI4I1LjlV9gp00p0judiQWRTZk9W2od+4vOl2C38sO9cy6pWiZ4tc6iKNnkUB6tUPdxYBLTAmpLbcCkLO6S+vefnziMeeT4/YmzQeysHjMvtuKzWhIxvtx1U9keF5pEKPDEuIHlyAN7qDrukQ0OLdOtgUCW/VGHP/UwvfEq1IizN85LR0AWbBuhKdHHQ89nywK/J5oXTJkkyjUR8xzSw9fU2abXzYqGHUyL6x/fSzFKfvuHN5PGUWDKYXIKlCpepZucCZUx2y7sB4ccgXJ4BezwB2KhRLRUq6fZPKGjhUd3DgdBMY7F+ovl7uW7Ml09dUjRFNhI5uEcCqPXiTUP28NoaVmzlutI7iFCL/iKO3fRd8xFvktIehn/4f4wQ0QNwV/ZVjvahjk/Z9Ys57d0k/UMZrfNbHJcRZTjzbvZjwcnWNrNScFe54umcZEznZe3PSQzhYhGo18TWWkq19BzTkQKPQIvwkHx6SkMHP51uqSwY5WPRW8+pTbBOQ5vp3s4OfIR4t+~-1~||0||~-1; _ga_T6392MZC6Z=GS2.1.s1750107625$o1$g1$t1750107715$j46$l0$h193280948; RT="z=1&dm=tdk.com&si=0fc92649-279a-47d7-b03b-0f31c359626b&ss=mbzkw10x&sl=3&tt=93v&bcn=%2F%2F17de4c19.akstat.io%2F&ld=1uwe&ul=234w"',
#         },
#     )
#     final = time.perf_counter() - init
#     result = response.status_code == 200
#     logger.info(f"{part_number}: {result} ({round(final, 2)})s")
#
#     return result


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
        assert all_same("rated_voltage")
        assert all_same("dielectric")
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

        return f"CAP,{self.package},{self.capacitance_str},{self.rated_voltage}V,{self.tolerance}%,"

    @property
    def capacitance_str_prefix_delimited(self):
        return list(self.capacitors.values())[0].capacitance_str_prefix_delimited

    @property
    def tolerance(self):
        vals = self._get_component_vals_dict()
        tolerance = max(vals["tolerance"])
        return tolerance

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
        capacitance = round(vals["capacitance"][0], 14)
        return capacitance

    @property
    def dielectric(self):
        vals = self._get_component_vals_dict()
        dielectric = vals["dielectric"][0]
        return dielectric

    @property
    def capacitance_str(self):
        return MetricValue.num_to_str(self.capacitance, units="F")


def compile_capacitor_pn_list():
    def add_capacitor(capacitor, target):
        key = capacitor.name_short
        # key = capacitor.capacitance
        if key not in target:
            target[key] = {}
        pn = capacitor.part_number
        if pn:
            target[key][pn] = capacitor

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

    def add_tdk(cap_dict):
        _root = os.path.dirname(__file__)

        tdk_ref_list = []
        csv_path = os.path.join(_root, "docs/tdk_csvs")
        ref_files = os.listdir(csv_path)
        for doc in ref_files:
            with open(os.path.join(csv_path, doc), "r") as f:
                temp = csv.DictReader(f)
                tdk_ref_list += list(temp)
        for cap_cfg in tdk_ref_list:
            cap = create_tdk_cap(cap_cfg)
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
    add_tdk(capacitors)

    # for package, cap_options in capacitors.items():
    #     for cap_name, caps in cap_options.items():
    #         for cap in caps.values():
    #             tdk_cap = create_tdk_cap(cap)

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
