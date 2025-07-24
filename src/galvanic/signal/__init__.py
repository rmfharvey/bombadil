from galvanic.signal.schema import (
    DigitalSignal,
    AnalogSignal,
    PwmSignal,
    UartBus,
    I2cBus,
    SpiBus,
    CommsSignal,
    PowerRail,
    Ground,
    DIRECTION,
)

ALL_SIGNALS = {
    cls.__name__: cls for cls in (DigitalSignal, AnalogSignal, PwmSignal, UartBus, I2cBus, SpiBus, PowerRail, Ground)
}


COLORS = {
    DigitalSignal: "#FFFF33",
    AnalogSignal: "#FFCC00",
    PwmSignal: {DIRECTION.INPUT: "#9966FF", DIRECTION.OUTPUT: "#99CCFF"},
    CommsSignal: "#CCCCCC",
}


def determine_signal_type(net_name):
    match_results = []
    for name, cls in ALL_SIGNALS.items():
        direction, is_match = cls.regex_match(cls.REGEX, net_name)
        if is_match:
            match_results.append({"direction": direction, "class": cls})
    # assert len(match_results) <= 1

    if match_results:
        match_results = match_results[0]
    return match_results


if __name__ == "__main__":
    SIGNALS = ["BLEH.AI", "FTANG.AO", "SWITCH.PWM", "ENCODER.PWMIN_DUTY", "SPI.SOMETHING.MOSI", "UART.3.RX"]

    for sig in SIGNALS:
        results = determine_signal_type(sig)
        if results:
            direction = results[0]["direction"]
            cls = results[0]["class"]
            print(direction, cls.__name__)
        else:
            print(f"No match for {sig}")
