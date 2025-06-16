import re
from sys import prefix


# TODO check some returns on units


class MetricValue:
    PREFIXES = {
        "f": 1e-15,
        "p": 1e-12,
        "n": 1e-9,
        "u": 1e-6,
        "m": 1e-3,
        "k": 1e3,
        "M": 1e6,
        "G": 1e9,
        "T": 1e12,
    }

    @staticmethod
    def num_to_str(num, units=None, ndigits=3):
        """Convert a number to a human readable string with metric prefixes and units if provided.

        :param float num: Number to convert to human readable string.
        :param units: Units, e.g. F, H, Ohm, etc
        :type units: str, NoneType
        :return: String representation of the number.
        :rtype: str
        """
        if num == 0:
            return f"0{units if units else ''}"

        # Handle negative numbers
        sign = "-" if num < 0 else ""
        abs_num = abs(num)

        # # Sort prefixes by their values for easier comparison
        # sorted_prefixes = sorted(MetricValue.PREFIXES.items(), key=lambda x: x[1])

        # Find the most appropriate prefix
        best_prefix = ""
        best_value = abs_num

        for prefix, scale in MetricValue.PREFIXES.items():  # Assumes these are sorted
            scaled_value = abs_num / scale
            # Use prefix if it results in a value between 1 and 999.999
            if 1 <= scaled_value < 1000:
                best_prefix = prefix
                best_value = scaled_value
                break

        formatted_num = str(round(best_value, ndigits)).rstrip("0").rstrip(".")

        # Construct the final string
        result = f"{sign}{formatted_num}{best_prefix}"
        if units:
            result += units

        return result

    @staticmethod
    def num_to_prefix_as_decimal_str(num, default_decimal=".", str_length=4):
        """Convert number to a string that uses the metric prefix as decimal.

        :param float num: Number to convert
        :param str default_decimal: Default decimal value to use if no metric prefix is present
        :param ndigits: Number of decimal digits to use
        :return: Prefix-as-Decimal formatted string.
        """
        # Get the standard metric string representation
        base_str = MetricValue.num_to_str(num)
        if base_str[-1].isalpha():
            decimal = base_str[-1]
            base_str = base_str[:-1]
        else:
            decimal = default_decimal

        # Split number string into before and after decimal
        match = re.match(r"^([^.]*)(\.(.*))?$", base_str)
        before = match.group(1)
        after = match.group(3) or "0"

        pasd_str = f"{before}{decimal}{after}"[:str_length].upper()
        # Pad with trailing zeros if needed
        padding = str_length - len(pasd_str)
        if padding:
            pasd_str += "0" * padding
        return pasd_str


if __name__ == "__main__":
    print(MetricValue.num_to_prefix_as_decimal_str(10266))  # "10K3
    # test_strings = [
    #     "1uF",
    #     "1.5kHz",
    #     "4.7mF",
    #     "2.2MHz",
    #     "0V",
    #     "-50mV",
    #     "1000Ohm",
    #     "12.3",
    #     "88.1pF",
    #     "47nH",
    #     "2.7GHz",
    #     "100",
    #     "",
    #     "invalid",
    #     # Test prefix-as-decimal format
    #     "1k00",  # 1.00k = 1000
    #     "1K00",  # 1.00k = 1000
    #     "4M7",  # 4.7M = 4700000
    #     "2k2",  # 2.2k = 2200
    #     "2K2",  # 2.2k = 2200
    #     "10k0",  # 10.0k = 10000
    #     "1M0Ohm",  # 1.0MOhm = 1000000
    #     "470pF",  # Standard format for comparison
    #     "47p0F",  # 47.0p = 47e-12
    #     "3n3H",  # 3.3nH = 3.3e-9
    #     "22uF",  # Standard format
    #     "22u0F",  # 22.0u = 22e-6
    # ]
    # for t in test_strings:
    #     num = MetricValue.str_to_num(t)
    #     str = MetricValue.num_to_str(num['value'], units=num['units'])
    #     print(t, str, num)
