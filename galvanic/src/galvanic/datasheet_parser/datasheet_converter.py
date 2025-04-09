import os
import json
import pymupdf4llm
from google import genai
import pathlib
from embedded_design_tools.protobuf import PROTOBUF
from galvanic import colored_logger


class DatasheetConverter:
    """Class to convert datasheet from PDF to JSON.

    :param str source_path: Path to datasheet.  Either PDF or Markdown
    """

    # _GEMINI_MODEL = 'gemini-1.5-flash', # Misses a lot of info
    # _GEMINI_MODEL = 'gemini-2.0-flash-001', # Gets more info but limits response length due to output token restrictions
    # _GEMINI_MODEL = 'gemini-2.0-flash',
    _GEMINI_MODEL = "gemini-2.5-pro-exp-03-25"

    logger = colored_logger("DatasheetReader")

    def __init__(self, source_path, output_directory):
        self._json = {}
        self.output_directory = output_directory
        self._prompts = self._get_prompts()
        self.output_directory = output_directory

        # Set up LLM API
        self._llm = genai.Client(api_key=os.environ["GEMINI_KEY"])

        # Load source file
        self.load_source(source_path)

        #
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

    def save_config(self, output_path):
        """Save JSON config

        :param str output_path: Output path to save json config to
        """
        with open(output_path, "w") as f:
            f.write(json.dumps(self._json, sort_keys=True, separators=(",", ":"), indent=2))

    ####################################################################################################################
    ### AI Parser calls
    ####################################################################################################################
    def AI_PARSER_get_comms_register_map(self):
        """Get register map for comms bus

        :return: Dictionary with register settings.
        :rtype: dict
        """
        self.logger.info("Analyzing markdown datasheet to extract serial comms register maps.")

        response = self._llm.models.generate_content(
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
        registers = self._remove_gemini_shittalking(response.text)
        return registers

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
    def _remove_gemini_shittalking(self, response_str):
        """Removes weird shit talking that Gemini seems to do for some reason."""
        lines = response_str.split("\n")
        idx = lines.index("```json")
        sanitized_str = "\n".join(lines[idx + 1 :]).strip("```")
        d_val = json.loads(sanitized_str)

        # Sometimes this gets returned as a list for some reason
        if isinstance(d_val, list):
            d_val = d_val[0]
        return d_val
