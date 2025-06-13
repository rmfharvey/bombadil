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
    def num_to_str(num, units=None):
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
        #
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

        formatted_num = str(best_value).rstrip("0").rstrip(".")

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
        return pasd_str

    @staticmethod
    def str_to_num(metric_string):
        """Accepts a metric formatted string and converts it to a number.

        Supports both standard format (1.23kHz) and prefix-as-decimal format (1K23).

        return_dict = {
            "value": float,
            "units": str,
        }

        :param str metric_string: Metric formatted string.  e.g. 12.3kHz, 88.1pF, 1K00, 4M7
        :return: Dictionary with value and units.
        :rtype: dict
        """
        if not metric_string or not isinstance(metric_string, str):
            return {"value": 0.0, "units": ""}

        # Remove whitespace and fix kilo capitalization
        metric_string = metric_string.strip().replace("K", "k")  # Both are acceptable

        # First try to match prefix-as-decimal format (e.g., 1K00, 4M7, 2k2)
        # Pattern: digits, prefix, digits, optional units
        prefix_decimal_pattern = r"^([+-]?\d+)([fpnumkMGT])(\d*)(.*)$"
        match = re.match(prefix_decimal_pattern, metric_string)

        if match:
            integer_part, prefix, decimal_part, units = match.groups()

            if prefix in MetricValue.PREFIXES:
                try:
                    # Build the decimal number
                    if decimal_part:
                        # Add decimal point between integer and decimal parts
                        combined_number = f"{integer_part}.{decimal_part}"
                    else:
                        combined_number = integer_part

                    base_value = float(combined_number)
                    value = base_value * MetricValue.PREFIXES[prefix]
                    units = units.strip() if units else ""

                    return {"value": value, "units": units}
                except ValueError:
                    pass  # Fall through to standard format parsing

        # Standard format parsing: number, optional prefix, optional units
        # Matches: optional sign, digits with optional decimal, optional prefix, optional units
        standard_pattern = r"^([+-]?\d*\.?\d+)([fpnumkMGT]?)(.*)$"
        match = re.match(standard_pattern, metric_string)

        if not match:
            # If no match, try to parse as plain number
            try:
                value = float(metric_string)
                return {"value": value, "units": ""}
            except ValueError:
                return {"value": 0.0, "units": ""}

        number_str, prefix, units = match.groups()

        try:
            # Parse the base number
            base_value = float(number_str)
        except ValueError:
            return {"value": 0.0, "units": ""}

        # Apply prefix multiplier
        if prefix and prefix in MetricValue.PREFIXES:
            value = base_value * MetricValue.PREFIXES[prefix]
        else:
            value = base_value

        # Clean up units (remove any remaining whitespace)
        units = units.strip() if units else ""

        return {"value": value, "units": units}


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
