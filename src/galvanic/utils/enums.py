class DIRECTION:
    INPUT = "Input"
    OUTPUT = "Output"
    IO = "IO"
    NONE = "None"


class POLARITY:
    ACTIVE_LOW = "Active Low"
    ACTIVE_HIGH = "Active High"


class PWM_INPUT_TYPE:
    DUTY = "Duty Dycle"
    FREQ = "Frequency"
    COUNT = "Pulse Counting"


class BUS_TYPES:
    UART = "UART"
    I2C = "I2C"
    I2S = "I2S"
    SPI = "SPI"
    JTAG = "JTAG"


class RAIL_REGULATION:
    REGULATED = "PWR"
    UNREGULATED = "VBUS"
