import os
import json
import requests
from urllib.parse import urlparse
from pathlib import Path
from galvanic import colored_logger

logger = colored_logger(__file__)

class DatasheetComponents:
    def __init__(self, root_path):
        self.root = Path(root_path)
        if not self.root.exists():
            os.mkdir(self.root)

    def download_json_from_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            logger.error(f"Failed to download from {url}")
            return False

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

    # def get_datasheet(self):
    #     ds_path = input("Enter datasheet source (URL or path): ")
    #
    #     parsed_url = urlparse(ds_path)
    #     is_url = bool(parsed_url.scheme)
    #
    #
    #     return self.load_json_datasheet(self._ROOT_DIR/ds)


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
    print()