from galvanic.utils.enums import DIRECTION, POLARITY, PWM_INPUT_TYPE, BUS_TYPES


class _Signal:
    direction: str  # DIRECTION
    signal_name: str
    polarity: str  # POLARITY

    _SEPARATOR = "."
    SUFFIX = {}
    SUFFIX_MAPPING = {}

    def __init__(self, signal_name, direction):
        self.signal_name = signal_name
        self.direction = direction

    @staticmethod
    def get_suffix_mapping(suffixes):
        "Returns a mapping of suffixes to directions"
        mapping = {}
        for dir, sfxs in suffixes.items():
            if isinstance(sfxs, str):
                mapping[sfxs] = dir
            else:
                for sfx in sfxs.values():
                    mapping[sfx] = dir
        return mapping

    @property
    def polarity(self):
        return POLARITY.ACTIVE_LOW if "_n" in self.name else POLARITY.ACTIVE_HIGH

    @property
    def name(self):
        components = [self.signal_name, self.SUFFIX.get(self.direction)]
        name = None
        if all(components):
            name = self._SEPARATOR.join(components)
        return name


class DigitalSignal(_Signal):
    SUFFIX = {
        DIRECTION.OUTPUT: "DO",
        DIRECTION.INPUT: "DI",
    }
    SUFFIX_MAPPING = _Signal.get_suffix_mapping(SUFFIX)


class AnalogSignal(_Signal):
    SUFFIX = {
        DIRECTION.OUTPUT: "AO",
        DIRECTION.INPUT: "AI",
    }
    SUFFIX_MAPPING = _Signal.get_suffix_mapping(SUFFIX)


class PwmSignal(_Signal):
    pwm_in_type = str  # PWM_INPUT_TYPE

    SUFFIX = {
        DIRECTION.OUTPUT: "PWM",
        DIRECTION.INPUT: {
            PWM_INPUT_TYPE.DUTY: "PWMIN_DUTY",
            PWM_INPUT_TYPE.FREQ: "PWMIN_FREQ",
            PWM_INPUT_TYPE.COUNT: "PWMIN_COUNT",
        },
    }
    SUFFIX_MAPPING = _Signal.get_suffix_mapping(SUFFIX)

    def __init__(self, signal_name, direction, pwm_in_type=None):
        super().__init__(signal_name=signal_name, direction=direction)
        self.pwm_in_type = pwm_in_type

    @property
    def name(self):
        components = [self.signal_name]
        if self.direction == DIRECTION.OUTPUT:
            components.append(self.SUFFIX.get(self.direction))
        else:
            components.append(self.SUFFIX.get(self.direction, {}).get(self.pwm_in_type))

        name = None
        if all(components):
            name = self._SEPARATOR.join(components)
        return name


class _SignalBus:
    bus_name: str
    bus_type: str  # BUS_TYPE
    _SIGNALS = []
    child_signals: dict[str]

    def __init__(self, bus_name):
        self.bus_name = bus_name
        self.child_signals = {subusage: CommsSignal(subusage, self) for subusage in self._SIGNALS}


class CommsSignal(_Signal):
    subusage: str
    parent_bus: _SignalBus
    signal_name: str

    def __init__(self, subusage, parent_bus, signal_name=None):
        self.signal_name = signal_name
        self.subusage = subusage
        self.parent_bus = parent_bus

    @property
    def name(self):
        signame = self.parent_bus.bus_name
        if self.signal_name:
            signame = f"{signame}_{self.signal_name}"
        components = [self.parent_bus.bus_type, signame, self.subusage]

        name = None
        if all(components):
            name = self._SEPARATOR.join(components)
        return name


class UartBus(_SignalBus):
    _SIGNALS = ["RX", "TX"]
    bus_type = BUS_TYPES.UART


class I2cBus(_SignalBus):
    _SIGNALS = ["SCL", "SDA"]
    bus_type = BUS_TYPES.I2C


class SpiBus(_SignalBus):
    _SIGNALS = ["SCK", "MOSI", "MISO"]
    bus_type = BUS_TYPES.SPI

    def add_cs(self, signal_name=None):
        if signal_name is None:
            signal_name = f"CS{self.cs_count+1}"
        self.child_signals[f"CS_{signal_name}"] = CommsSignal("CS", self, signal_name)

    @property
    def cs_count(self):
        c = 0
        for name in self.child_signals:
            if name not in self._SIGNALS:
                c += 1
        return c


COLORS = {
    DigitalSignal: "#FFFF33",
    AnalogSignal: "#FFCC00",
    PwmSignal: {DIRECTION.INPUT: "#9966FF", DIRECTION.OUTPUT: "#99CCFF"},
    CommsSignal: "#CCCCCC",
}
