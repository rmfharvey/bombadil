import copy
import os
import json
from copy import deepcopy
import pymupdf4llm
from google import genai
import pathlib
from embedded_design_tools.protobuf import PROTOBUF
from galvanic import colored_logger

_root = os.path.dirname(__file__)


def sanitize_raw_output(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        try:
            sanitized = DatasheetConverter.remove_gemini_shittalking(response.text)
        except:
            with open(os.path.join(_root, f"{func.__name__}.txt"), "w") as f:
                f.write(response.text)
            sanitized = False
        return sanitized

    return wrapper


class DatasheetConverter:
    """Class to convert datasheet from PDF to JSON.

    :param str source_path: Path to datasheet.  Either PDF or Markdown
    """

    # _GEMINI_MODEL = 'gemini-1.5-flash', # Misses a lot of info
    # _GEMINI_MODEL = 'gemini-2.0-flash-001', # Gets more info but limits response length due to output token restrictions
    # _GEMINI_MODEL = 'gemini-2.0-flash',
    _GEMINI_MODEL = "gemini-2.5-pro-exp-03-25"
    # _GEMINI_MODEL = "gemini-1.5-pro-latest"

    logger = colored_logger("DatasheetReader")

    def __init__(self, source_path, output_directory):
        self._json = {}
        self.output_directory = output_directory
        self._prompts = self._get_prompts()
        self.output_directory = output_directory

        # Set up LLM API
        self._llm_client = genai.Client(api_key=os.environ["GEMINI_KEY"])
        # self._llm_client = genai.Client(api_key=os.environ["GEMINI_KEY_2"])

        # Load source file
        self.load_source(source_path)

        self.analyze_datasheet()

    def analyze_datasheet(self):
        # AI Model Calls
        # self._json["high_level"] = self.AI_PARSER_get_high_level_info()
        # self._json["pins"] = self.AI_PARSER_get_pin_info()
        #
        # if self.has_serial_bus:
        self._json["serial_bus"] = self.AI_PARSER_get_comms_register_map()

    def load_source(self, source_path):
        ### Get source file, based on input type
        if source_path.endswith(".pdf"):  # If PDF convert to markdown
            md_output_path = os.path.join(self.output_directory, "datasheet.md")
            self.md_datasheet = DatasheetConverter.to_markdown(source_path, output_path=md_output_path)
        elif source_path.endswith(".md"):  # If markdown, read
            self.logger.info(f"Loading previosuly parsed markdown from {source_path}")
            with open(source_path, "r") as f:
                self.md_datasheet = f.read()

    def get_config(self):
        return copy.deepcopy(self._json)

    def save_config(self, output_path):
        """Save JSON config

        :param str output_path: Output path to save json config to
        """
        cfg = self.get_config()
        with open(output_path, "w") as f:
            f.write(json.dumps(cfg, sort_keys=True, separators=(",", ":"), indent=2))

    ####################################################################################################################
    ### AI Parser calls
    ####################################################################################################################
    @sanitize_raw_output
    def AI_PARSER_get_high_level_info(self):
        """Get high level device info

        :return: Dictionary with high level device info.
        :rtype: dict
        """
        self.logger.info("Analyzing markdown datasheet to extract high level device information.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["high_level_ic_info"],
                    "datasheet": self.md_datasheet,
                    "proto1": PROTOBUF.device.high_level,
                    "proto2": PROTOBUF.serial_bus.register,
                }.values()
            ),
            config={
                "response_mime_type": "application/json",
            },
        )
        return response

    @sanitize_raw_output
    def AI_PARSER_get_comms_register_map(self):
        """Get register map for comms bus

        :return: Dictionary with register settings.
        :rtype: dict
        """
        self.logger.info("Analyzing markdown datasheet to extract serial comms register maps.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["register"],
                    "datasheet": self.md_datasheet,
                    "protobuf": PROTOBUF.serial_bus.register,
                }.values()
            ),
            config={
                "response_mime_type": "application/json",
            },
        )
        return response

    @sanitize_raw_output
    def AI_PARSER_get_pin_info(self):
        """Get IC pin info

        :return: Dictionary with pin info.
        :rtype: dict
        """
        self.logger.info("Analyzing markdown datasheet to extract pin info.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["ic_pins"],
                    "datasheet": self.md_datasheet,
                    "protobuf_pin_schema": PROTOBUF.ic_pins.ic_pins,
                    "protobuf_pin_enums": PROTOBUF.misc.pin_enums,
                    "protobuf_pin_pull": PROTOBUF.misc.numbers,
                }.values()
            ),
            config={
                "response_mime_type": "application/json",
            },
        )
        return response

    ####################################################################################################################
    ### Private Functions
    ####################################################################################################################
    def _get_prompts(self):
        """Helper function to load prompts from local directory"""
        prompt_files = {}
        _root = os.path.dirname(__file__)
        for fn in os.listdir(os.path.join(_root, "_prompts")):
            if not fn.endswith(".prompt"):
                continue
            with open(os.path.join(_root, "_prompts", fn), "r") as f:
                prompt_files[fn.replace(".prompt", "")] = f.read()
        return prompt_files

    @staticmethod
    def to_markdown(datasheet_path, output_path=None):
        """Convert PDF datasheet to markdown.

        :param str datasheet_path: Path to local PDF
        :param output_path: Optional output path to save the markdown output to.
        :type output_path: str, NoneType
        :return:
        """
        # # Check if path is a url, if so, download
        # result = urlparse(datasheet_path)
        # is_url = all([result.scheme, result.netloc])
        # try:
        #     if is_url:
        #         response = requests.get(datasheet_path, stream=True)
        #         assert response.status_code == "200", f"Failed to get file from {datasheet_path}"
        #         with tempfile.NamedTemporaryFile() as tmp:
        #             datasheet_path = tempfile.name
        #             for chunk in response.iter_content(chunk_size=1024):
        #                 if chunk:
        #                     tmp.write(chunk)
        # except AssertionError as err:
        #     DatasheetReader.logger.error(err)

        DatasheetConverter.logger.info(f"Converting {datasheet_path} to markdown")
        md_text = pymupdf4llm.to_markdown(datasheet_path)

        if output_path:
            pathlib.Path(output_path).write_bytes(md_text.encode())

        return md_text

    ###
    @staticmethod
    def remove_gemini_shittalking(response_str):
        """Removes weird shit talking that Gemini seems to do for some reason."""
        lines = response_str.split("\n")
        START_KEY = "```json"
        if START_KEY in lines:  # If using markdown formatting
            idx = lines.index(START_KEY)
            sanitized_str = "\n".join(lines[idx + 1 :]).strip("```")
        else:
            sanitized_str = response_str
        d_val = json.loads(sanitized_str)

        # Sometimes this gets returned as a list for some reason
        if isinstance(d_val, list):
            d_val = d_val[0]
        return d_val

    def update_config(self, ds_path):
        """Utility function to append information to an existing datasheet.  This is used mainly for testing where we
        want to test out a new function and add existing information without wiping everything else.

        :param str ds_path: Path to current datasheet
        """
        ds = {}
        if os.path.exists(ds_path):
            with open(ds_path, "r") as f:
                ds = json.load(f)

        cfg = self.get_config()
        ds.update(cfg)

        with open(ds_path, "w") as f:
            f.write(json.dumps(ds, sort_keys=True, separators=(",", ":"), indent=2))

    def save_config(self, ds_path):
        """Utility function to append information to an existing datasheet.  This is used mainly for testing where we
        want to test out a new function and add existing information without wiping everything else.

        :param str ds_path: Path to current datasheet
        """
        cfg = self.get_config()

        with open(ds_path, "w") as f:
            f.write(json.dumps(cfg, sort_keys=True, separators=(",", ":"), indent=2))

    @property
    def has_serial_bus(self):
        return bool(len(self._json.get("high_level", {}).get("serial_busses", [])))


class MicroDatasheetConverter(DatasheetConverter):
    def analyze_datasheet(self):
        self._json["high_level"] = self.AI_PARSER_get_high_level_info()
        self._json["cores"] = self.AI_PARSER_get_cores_and_memory()
        self._json["pads"] = self.AI_PARSER_get_pin_muxing()
        self._json["pin_pad_mapping"] = self.AI_PARSER_get_pin_pad_mapping()

    ####################################################################################################################
    ### AI Parser calls
    ####################################################################################################################
    @sanitize_raw_output
    def AI_PARSER_get_pin_muxing(self):
        self.logger.info("Analyzing markdown datasheet to extract pin muxing info.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["micro_pin_muxing"],
                    "datasheet": self.md_datasheet,
                    "protobuf_pin_schema": PROTOBUF.microcontroller.micro_pin,
                    "protobuf_pin_enums": PROTOBUF.misc.pin_enums,
                }.values()
            ),
            config={
                "response_mime_type": "application/json",
            },
        )
        return response
        # pins = self._remove_gemini_shittalking(response.text)
        # return pins

    @sanitize_raw_output
    def AI_PARSER_get_pin_pad_mapping(self):
        self.logger.info("Analyzing markdown datasheet to extract mapping between pin/pad for each package.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["micro_pin_pad_mapping"],
                    "datasheet": self.md_datasheet,
                }.values()
            ),
            config={
                "response_mime_type": "application/json",
            },
        )
        return response

    @sanitize_raw_output
    def AI_PARSER_get_cores_and_memory(self):
        self.logger.info("Analyzing markdown datasheet to extract core and memory info.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["micro_memory_compute"],
                    "datasheet": self.md_datasheet,
                }.values()
            ),
            config={
                "response_mime_type": "application/json",
            },
        )
        return response

    @property
    def has_serial_bus(self):
        """Override this to always return False since we don't want to"""
        return False
