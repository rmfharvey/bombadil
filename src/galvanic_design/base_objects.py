import json
import logging
from pathlib import Path
from galvanic import colored_logger, global_logger
from galvanic.ui.base_ui_objects import GWidget


class BaseObject:
    WIDGET_CLASS = None

    def __init__(self, name=None, logging_level=logging.INFO, create_ui: bool = False):
        self.name = name

        logger_name = self.name or self.__class__.__name__
        self.logger = colored_logger(name=logger_name, level=logging_level)

        if create_ui:
            self.ui_object = self.create_ui_element()

    @classmethod
    def from_config(cls, config):
        obj = cls(create_ui=False)
        obj.load_config(config)
        return obj

    def create_ui_element(self):
        if self.WIDGET_CLASS and issubclass(self.WIDGET_CLASS, GWidget):
            w = self.WIDGET_CLASS(self)
        else:
            self.logger.warning(f"{self.__class__.__name__} has no assigned WIDGET_CLASS.")
            w = None
        return w

    def load_config(self, config: Path | str | dict, create_ui: bool = False):
        # Load config from path or dict
        config = self._resolve_config_path(config)
        self._load_dict_values(config, overwrite=True)

        if create_ui:
            self.ui_object = self.create_ui_element()

    def get_config(self, partial_config: dict = {}, ignore_keys: list = []):
        # TODO Get all public members in the object that are not properties, not in ignore_keys, and not in partial_config.  Get their values and add them to partial_config.   The dictionary key should be the member/variable name

        raise NotImplementedError
        return partial_config

    def save_config(self, output_path: Path | str):
        with open(output_path, "w") as f:
            f.write(json.dumps(self.get_config(), indent=2, sort_keys=True, separators=(",", ": ")))

    ####################################################################################################################
    ### Private Functions
    ####################################################################################################################

    def _resolve_config_path(self, config: Path | str | dict):
        """Accepts arbitrary config path or dict and converts to dict"""
        # Load config from path or dict
        if isinstance(config, str):
            config = Path(config)
        if isinstance(config, Path):
            with open(config, "r") as f:
                config = json.load(f)
        assert isinstance(config, dict)

        return config

    def _load_dict_values(self, config: dict, overwrite: bool = True):
        """Load values from a dictionary into the class

        :param dict config: Dictionary to load
        :param bool overwrite: Overwrite existing values if True
        :return:
        """
        for k, v in config.items():
            has_attribute = hasattr(self, k)
            has_attrvalue = getattr(self, k, None) is not None

            if has_attribute:
                if has_attrvalue:
                    if not overwrite:
                        self.logger.warning(f"{k} is already assigned a value of {v}.  Skipping.")
                        continue
                    else:
                        self.logger.warning(f"Overwriting existing value for {k}")
            setattr(self, k, v)
