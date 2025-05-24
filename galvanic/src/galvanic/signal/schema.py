from galvanic.utils.enums import DIRECTION, POLARITY, PWM_INPUT_TYPE


class _Signal:
    direction: str  # DIRECTION
    signal_name: str
    polarity: str  # POLARITY

    SEPARATOR = "."
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
        return POLARITY.ACTIVE_LOW if "_n" in self.signal_name else POLARITY.ACTIVE_HIGH

    @property
    def name(self):
        components = [self.signal_name, self.SUFFIX.get(self.direction)]
        name = None
        if all(components):
            name = self.SEPARATOR.join(components)
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
            name = self.SEPARATOR.join(components)
        return name
