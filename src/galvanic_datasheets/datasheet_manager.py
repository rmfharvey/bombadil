import os
import json
import shutil
import requests
from urllib.parse import urlparse
from pathlib import Path
from galvanic import colored_logger
from galvanic.utils.datasheet_parser import DatasheetConverter

logger = colored_logger(__file__)


class DatasheetStructure:
    _PROMPT = False
    _AUTOCREATE_JSON = True

    def __init__(self, root_path):
        self._root = Path(root_path)
        if not self._root.exists():
            os.mkdir(self._root)
        if not self.has_pdf and self._PROMPT:
            self.download_datasheet()

    def download_datasheet(self, datasheet_path=None):
        if datasheet_path is None:
            datasheet_path = input("Enter datasheet source (URL or path): ")

        # Determine path type
        is_url = bool(urlparse(datasheet_path).scheme)
        if is_url:
            response = requests.get(datasheet_path)
            if response.status_code == 200:
                with open(self._root / "datasheet.pdf", "wb") as f:
                    f.write(response.content)
            else:
                logger.error(f"Failed to download from {datasheet_path}")
        elif os.path.exists(datasheet_path):
            shutil.copyfile(datasheet_path, self._root / "datasheet.pdf")
        else:
            logger.error(f"Path was not a url and no local file not found: {datasheet_path}")

    def create_json(self):
        source = self.pdf_path
        if self.has_md:
            source = self.md_path
        dc = DatasheetConverter(source, str(self._root))
        dc.save_config(self.json_path)

    def load_json_datasheet(self):
        loaded_json = None
        if self.has_json:
            with open(self.json_path, "r") as f:
                loaded_json = json.load(f)
        return loaded_json

    @property
    def has_md(self):
        return os.path.exists(self._root / "datasheet.md")

    @property
    def has_json(self):
        return os.path.exists(self._root / "datasheet.json")

    @property
    def has_pdf(self):
        return os.path.exists(self._root / "datasheet.pdf")

    @property
    def pdf_path(self):
        return str(self._root / "datasheet.pdf")

    @property
    def md_path(self):
        return str(self._root / "datasheet.md")

    @property
    def json_path(self):
        return str(self._root / "datasheet.json")


class _DatasheetManager:
    _ROOT_DIR = Path(__file__).parent / "source_datasheets"

    def __init__(self):
        self.logger = colored_logger(self.__class__.__name__)

        self.datasheets = {}
        for ds_dir in self._ROOT_DIR.iterdir():
            ds = DatasheetStructure(ds_dir)
            # ds = self.load_json_datasheet(ds_dir)
            if ds:
                self.datasheets[ds_dir.parts[-1]] = ds

    def load_json_datasheet(self, datasheet_directory, prompt_for_source=True):
        parsed_ds_present = "datasheet.json" in os.listdir(datasheet_directory)
        if not parsed_ds_present:
            if prompt_for_source:
                ds = self.get_datasheet()
            else:
                self.logger.warning(f"No datasheet found in {datasheet_directory}")
                ds = None
        else:
            with open(datasheet_directory / "datasheet.json", "r") as f:
                ds = json.load(f)
        return ds

    def new_datasheet(self, part_number, datasheet_path=None, autocreate_json=True):
        ds = DatasheetStructure(self._ROOT_DIR / part_number)
        if not ds.has_pdf:
            ds.download_datasheet(datasheet_path)
        if autocreate_json:
            ds.create_json()
        return ds

    def get_datasheet(self, part_number, create_new_if_missing=False):
        part_number = part_number.lower()
        ds = self.datasheets.get(part_number)

        if ds is None:
            if create_new_if_missing:  # TODO confusign logic.  clean up
                json_ds = self.new_datasheet(part_number)
            else:
                json_ds = None
        else:
            json_ds = ds.load_json_datasheet()
        return json_ds

    @property
    def by_manufacturer(self):
        by_mfg = {}
        for part_number, ds in self.datasheets.items():
            manufacturer = ds.get("high_level", {}).get("manufacturer")
            if manufacturer not in by_mfg:
                by_mfg[manufacturer] = {}
            by_mfg[manufacturer][part_number] = ds
        return by_mfg

    @property
    def by_type(self):
        by_mfg = {}
        for part_number, ds in self.datasheets.items():
            dtype = ds.get("high_level", {}).get("device_type")
            if dtype not in by_mfg:
                by_mfg[dtype] = {}
            by_mfg[dtype][part_number] = ds
        return by_mfg


DatasheetManager = _DatasheetManager()
