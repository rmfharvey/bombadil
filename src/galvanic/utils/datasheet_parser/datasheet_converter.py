import copy
import os
import functools
import json
from datetime import datetime
import pathlib
from json import JSONDecodeError

import pymupdf4llm
from google import genai
from google.genai import types

from galvanic_schema.protobuf import PROTOBUF
from galvanic import global_logger

_root = os.path.dirname(__file__)


def log_token_usage(func):
    DeprecationWarning("Moving into LlmCLient")
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = func(*args, **kwargs)

        # Log token usage
        usage_meta = response.usage_metadata
        args[0].log_transaction_tokens(usage_meta)

        return response

    return wrapper


def sanitize_raw_output(external_fault_handler=False):
    def outer_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)

            try:
                sanitized = DatasheetConverter.remove_gemini_shittalking(response.text)
            except:
                if external_fault_handler:
                    sanitized = response
                else:
                    with open(os.path.join(_root, f"{func.__name__}.txt"), "w") as f:
                        f.write(response.text)
                    sanitized = False

            return sanitized

        return wrapper

    return outer_wrapper


class TokenLogger:
    DeprecationWarning("Moving to galvanic_ai")

    def __init__(self):
        self._transactions = []

    def add_transaction(self, usage_meta, timestamp):
        token_info = {
            "timestamp": timestamp,
            "total_tokens": usage_meta.total_token_count,
            "prompt_tokens": usage_meta.prompt_token_count,
            "cached_tokens": usage_meta.cached_content_token_count,
            "output_tokens": usage_meta.thoughts_token_count,
        }
        self._transactions.append(token_info)
        return token_info


class DatasheetConverter:
    """Class to convert datasheet from PDF to JSON.

    :param str source_path: Path to datasheet.  Either PDF or Markdown
    """

    # _GEMINI_MODEL = "gemini-2.5-pro-preview-06-05"
    # _GEMINI_MODEL = "gemini-2.5-pro"
    _GEMINI_MODEL = "gemini-2.5-flash-lite"

    _GEMINI_KEY = api_key = os.environ["GEMINI_KEY"]
    # _GEMINI_KEY = api_key = os.environ["GEMINI_KEY_2"]
    # _GEMINI_KEY = api_key = os.environ["GEMINI_KEY_3"]

    logger = global_logger

    def __init__(self, source_path, output_directory):
        self._json = {}
        self._cache = None
        self._token_logger = TokenLogger()
        self.output_directory = output_directory
        self._prompts = self._get_prompts()
        self.output_directory = output_directory

        # Set up LLM API
        self._llm_client = genai.Client(api_key=self._GEMINI_KEY)

        # Load source file
        self.load_source(source_path)

        self.analyze_datasheet()

    def analyze_datasheet(self):
        # AI Model Calls
        try:
            self._json["high_level"] = self.AI_PARSER_get_high_level_info()
            self._json["pins"] = self.AI_PARSER_get_pin_info()

            for name, pin in self._json["pins"].items():
                response = self.AI_PARSER_get_pin_connectivity_info(name)
                pin['implementation'] = response

            if self.has_serial_bus:
                self._json["serial_bus"] = self.AI_PARSER_get_comms_register_map()
        except Exception as err:
            self.logger.error(f"Failed to analyze datasheet.  Error: {err}")
            self.update_config(os.path.join(self.output_directory, "datasheet_tempfile.json"))

    def log_transaction_tokens(self, usage_meta, timestamp=None):
        """Logs tokens required for a query

        :param GenerateContentResponseUsageMetadata usage_meta:  Usage metadata
        """
        DeprecationWarning("Moving to galvanic_ai")
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        token_info = self._token_logger.add_transaction(usage_meta, timestamp)
        self.logger.info(
            "Total Token Count: {t[total_tokens]}\n\tInput: {t[prompt_tokens]}\n\tOutput: {t[output_tokens]}\n\tCached: {t[cached_tokens]}".format(
                t=token_info
            )
        )

    def load_source(self, source_path):
        ### Get source file, based on input type
        if source_path.endswith(".pdf"):  # If PDF convert to markdown
            md_output_path = os.path.join(self.output_directory, "datasheet.md")
            self.md_datasheet = DatasheetConverter.to_markdown(source_path, output_path=md_output_path)
        elif source_path.endswith(".md"):  # If markdown, read
            self.logger.info(f"Loading previosuly parsed markdown from {source_path}")
            try:
                with open(source_path, "r") as f:
                    self.md_datasheet = f.read()
            except UnicodeDecodeError:
                with open(source_path, "r", encoding='utf-8') as f:
                    self.md_datasheet = f.read()


        # Explicit caching
        self.logger.info("Caching datasheet info")
        self._cache = self._llm_client.caches.create(
            model=self._GEMINI_MODEL,
            config=types.CreateCachedContentConfig(
                display_name="markdown datasheet",  # used to identify the cache
                system_instruction=("Answer subsequent queries using this cached datasheet data"),
                contents=[self.md_datasheet],
                ttl="3600s",  # Cache for 1hr
            ),
        )

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
    @sanitize_raw_output()
    @log_token_usage
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
                    # "datasheet": self.md_datasheet,
                    "proto1": PROTOBUF.device.high_level,
                    "proto2": PROTOBUF.serial_bus.register,
                }.values()
            ),
            config=types.GenerateContentConfig(cached_content=self._cache.name),
            # config = {"response_mime_type": "application/json"},
        )
        return response

    @sanitize_raw_output()
    @log_token_usage
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
                    # "datasheet": self.md_datasheet,
                    "protobuf": PROTOBUF.serial_bus.register,
                }.values()
            ),
            config=types.GenerateContentConfig(cached_content=self._cache.name),
            # config={
            #     "response_mime_type": "application/json",
            # },
        )
        return response

    @sanitize_raw_output()
    @log_token_usage
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
                    # "datasheet": self.md_datasheet,
                    "protobuf_pin_schema": PROTOBUF.ic_pins.ic_pins,
                    "protobuf_pin_enums": PROTOBUF.misc.pin_enums,
                    "protobuf_pin_pull": PROTOBUF.misc.numbers,
                }.values()
            ),
            config=types.GenerateContentConfig(cached_content=self._cache.name),
            # config={
            #     "response_mime_type": "application/json",
            # },
        )
        return response

    @sanitize_raw_output()
    @log_token_usage
    def AI_PARSER_get_pin_connectivity_info(self, pin_name):
        """Get detailed IC pin usage/implementation info

        :return: Dictionary with pin info.
        :rtype: dict
        """
        self.logger.info("Analyzing markdown datasheet to extract pin connectivity info.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["pin_usage"].format(pin_name=pin_name),
                    # "datasheet": self.md_datasheet,
                }.values()
            ),
            config=types.GenerateContentConfig(cached_content=self._cache.name),
            # config={
            #     "response_mime_type": "application/json",
            # },
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

    @staticmethod
    def repair_truncated_json(json_string):
        reconstitute = lambda lines: json.loads("\n".join(lines))

        lines = json_string.split("\n")
        if lines[0] == "```json":
            lines.pop(0)

        # Find last close brackets and truncate to there
        for i in range(len(lines) - 1, 0, -1):
            if lines[i].endswith("}") or lines[i].endswith("},"):
                last_term_idx = i
                break
        lines = lines[: last_term_idx + 1]
        lines[-1] = lines[-1].strip(",")

        # Strip comma and add closing braces
        ll = lines[-1]
        leading_ws = len(ll) - len(ll.lstrip())

        # If in functions
        in_func_lines = copy.deepcopy(lines)
        in_func_lines.append("  " * int(leading_ws / 2 - 1) + "]")
        for i in range(int(leading_ws / 2) - 1, 0, -1):
            in_func_lines.append("  " * (i - 1) + "}")
        try:
            return reconstitute(in_func_lines)
        # Else yolo!
        except:
            for i in range(int(leading_ws / 2), 0, -1):
                lines.append("  " * (i - 1) + "}")
            return reconstitute(lines)

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
            try:
                with open(ds_path, "r") as f:
                    ds = json.load(f)
            except JSONDecodeError as err:
                self.logger.error(f"Failed to load existing datasheet at {ds_path}.  Dumping to datasheet_tempfile.json. \nError: {err}")
                temp_path = f"{os.path.sep}".join(ds_path.split(os.path.sep)[:-1] + ["datasheet_tempfile.json"])

                with open(temp_path, "w") as f:
                    f.write(json.dumps(self._json, sort_keys=True, separators=(",", ":"), indent=2))

                return err

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
        try:
            # self._json["high_level"] = self.AI_PARSER_get_high_level_info()
            # self._json["cores"] = self.AI_PARSER_get_cores_and_memory()
            # self._json["pads"] = self._get_pin_pad_mapping_iteratively()
            self._json["pin_pad_mapping"] = self.AI_PARSER_get_pin_pad_mapping()

            # self._json["pads"] = self.AI_PARSER_get_pin_muxing()
            # self._json['peripherals'] = self.build_peripherals_from_pads(self._json["pads"])
        except Exception as err:
            self.logger.error(f"Failed to analyze datasheet.  Error: {err}")
            self.update_config(os.path.join(self.output_directory, "datasheet_tempfile.json"))

    def _get_pin_pad_mapping_iteratively(self):
        finished = False
        wip_dict = {}
        while not finished:
            response = self.AI_PARSER_get_pin_muxing(list(wip_dict.keys()))

            if isinstance(response, dict):  # Success
                finished = True
                temp_dict = response
            else:  # JSON must've been truncated, repair
                temp_dict = self.repair_truncated_json(response.text)
            wip_dict.update(temp_dict)
        return wip_dict

    ####################################################################################################################
    ### AI Parser calls
    ####################################################################################################################
    @sanitize_raw_output(external_fault_handler=True)
    @log_token_usage
    def AI_PARSER_get_pin_muxing(self, completed_pins=[]):
        self.logger.info("Analyzing markdown datasheet to extract pin muxing info.")

        skip_clause = ""
        if len(completed_pins) > 0:
            skip_clause = "The following pins have already been parsed and should be ignored: {}".format(
                ", ".join(completed_pins)
            )

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["micro_pin_muxing"],
                    "exempt_pins": skip_clause,
                    "protobuf_pin_schema": PROTOBUF.microcontroller.micro_pin,
                    "protobuf_pin_enums": PROTOBUF.misc.pin_enums,
                }.values()
            ),

            config=types.GenerateContentConfig(cached_content=self._cache.name),
        )
        return response

    @sanitize_raw_output()
    @log_token_usage
    def AI_PARSER_get_pin_pad_mapping(self):
        self.logger.info("Analyzing markdown datasheet to extract mapping between pin/pad for each package.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["micro_pin_pad_mapping"],
                }.values()
            ),
            config=types.GenerateContentConfig(cached_content=self._cache.name),
            # config={
            #     "response_mime_type": "application/json",
            # },
        )
        return response

    @sanitize_raw_output()
    @log_token_usage
    def AI_PARSER_get_cores_and_memory(self):
        self.logger.info("Analyzing markdown datasheet to extract core and memory info.")

        response = self._llm_client.models.generate_content(
            model=self._GEMINI_MODEL,
            contents=list(
                {
                    "prompt": self._prompts["micro_memory_compute"],
                    # "datasheet": self.md_datasheet,
                }.values()
            ),
            config=types.GenerateContentConfig(cached_content=self._cache.name),  # config={
            #     "response_mime_type": "application/json",
            # },
        )
        return response

    @staticmethod
    def build_peripherals_from_pads(pads):
        peripherals = {}
        for pad_name, pad in pads.items():
            for f in pad['functions']:
                p_name = f['peripheral_name']
                p_inst = f['peripheral_instance']
                p_sub = f['peripheral_subusage']

                if p_name not in peripherals:   # Add peripheral if it doesn't exist
                    peripherals[p_name] = {}

                if p_inst not in peripherals[p_name]: # Add instance if it doesn't exist
                    peripherals[p_name][p_inst] = {'subusages': {}, 'assignable_pins': []}
                target = peripherals[p_name][p_inst]

                target['assignable_pins'].append(pad_name)

                if p_sub not in target['subusages']:
                    target['subusages'][p_sub] = []
                target['subusages'][p_sub].append(pad_name)

        return peripherals

    @property
    def has_serial_bus(self):
        """Override this to always return False since we don't want to"""
        return False
