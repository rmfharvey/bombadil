import json
import logging
from pathlib import Path
from galvanic import colored_logger
from galvanic.ui.base_ui_objects import GWidget


class BaseObject:
    comment: str = None
    logger: logging.Logger = None

    WIDGET_CLASS = None

    def __init__(self, name=None, logging_level=logging.INFO):
        self.name = name

        logger_name = self.name or self.__class__.__name__
        self.logger = colored_logger(name=logger_name, level=logging_level)

    @classmethod
    def from_config(cls, config):
        obj = cls()
        obj.load_config(config)
        return obj

    def create_ui_element(self):
        if self.WIDGET_CLASS and issubclass(self.WIDGET_CLASS, GWidget):
            w = self.WIDGET_CLASS(self)
        else:
            self.logger.warning(f"{self.__class__.__name__} has no assigned WIDGET_CLASS.")
            w = None
        return w

    def load_config(self, config: Path | str | dict):
        # Load config from path or dict
        if isinstance(config, str):
            config = Path(config)
        if isinstance(config, Path):
            with open(config, "r") as f:
                config = json.load(f)
        assert isinstance(config, dict)

        for k, v in config.items():
            has_value = getattr(self, k)
            if has_value:
                self
            setattr(self, k, v)

    def get_config(self, ignore_keys: list = [], partial_config: dict = {}):
        # TODO Get all public members in the object that are not properties, not in ignore_keys, and not in partial_config.  Get their values and add them to partial_config.   The dictionary key should be the member/variable name

        raise NotImplementedError
        return partial_config

    def save_config(self, output_path: Path | str):
        with open(output_path, "w") as f:
            f.write(json.dumps(self.get_config(), indent=2, sort_keys=True, separators=(",", ": ")))
