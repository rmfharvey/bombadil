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
    PROMPT = True
    AUTOCREATE_JSON = True

    def __init__(self, root_path):
        self.root = Path(root_path.lower())
        if not self.root.exists():
            os.mkdir(self.root)
        if not self.has_pdf and self.PROMPT:
            self.download_datasheet()

    def download_datasheet(self, datasheet_path=None):
        if datasheet_path is None:
            datasheet_path = input("Enter datasheet source (URL or path): ")

        # Determine path type
        is_url = bool(urlparse(datasheet_path).scheme)
        if is_url:
            response = requests.get(datasheet_path)
            if response.status_code == 200:
                with open(self.root/'datasheet.pdf', 'wb') as f:
                    f.write(response.content)
            else:
                logger.error(f"Failed to download from {datasheet_path}")
        elif os.path.exists(datasheet_path):
            shutil.copyfile(datasheet_path, self.root/'datasheet.pdf')
        else:
            logger.error(f"Path was not a url and no local file not found: {datasheet_path}")

    def create_json(self):
        DatasheetConverter(self.root/'datasheet.pdf', self.root)

    @property
    def has_md(self):
        return os.path.exists(self.root/'datasheet.md')

    @property
    def has_json(self):
        return os.path.exists(self.root/'datasheet.md')

    @property
    def has_pdf(self):
        return os.path.exists(self.root/'datasheet.pdf')

class DatasheetManager:
    _ROOT_DIR = Path(__file__).parent/"source_datasheets"


    def __init__(self):
        self.logger = colored_logger(self.__class__.__name__)

        self.datasheets = {}
        for ds_dir in self._ROOT_DIR.iterdir():
            ds = self.load_json_datasheet(ds_dir)
            if ds:
                self.datasheets[ds_dir.parts[-1]] = ds


    def load_json_datasheet(self, datasheet_directory, prompt_for_source=True):
        parsed_ds_present = 'datasheet.json' in os.listdir(datasheet_directory)
        if not parsed_ds_present:
            if prompt_for_source:
                ds = self.get_datasheet()
            else:
                self.logger.warning(f"No datasheet found in {datasheet_directory}")
                ds = None
        else:
            with open(datasheet_directory/'datasheet.json', 'r') as f:
                ds = json.load(f)
        return ds

    def get_datasheet(self):
        ds_path = input("Enter datasheet source (URL or path): ")

        parsed_url = urlparse(ds_path)
        is_url = bool(parsed_url.scheme)

        return self.load_json_datasheet(self._ROOT_DIR/ds)


    @property
    def by_manufacturer(self):
        by_mfg = {}
        for part_number, ds in self.datasheets.items():
            manufacturer = ds.get("high_level", {}).get('manufacturer')
            if manufacturer not in by_mfg:
                by_mfg[manufacturer] = {}
            by_mfg[manufacturer][part_number] = ds
        return by_mfg

    @property
    def by_type(self):
        by_mfg = {}
        for part_number, ds in self.datasheets.items():
            dtype = ds.get("high_level", {}).get('device_type')
            if dtype not in by_mfg:
                by_mfg[dtype] = {}
            by_mfg[dtype][part_number] = ds
        return by_mfg


if __name__ == "__main__":
    manager = DatasheetManager()
    ds = DatasheetStructure(str(manager._ROOT_DIR/'tps23730'))
    ds.create_json()
    print()