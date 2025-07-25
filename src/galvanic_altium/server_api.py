import json
import requests
import logging
import os
from galvanic import colored_logger


logger = colored_logger(__file__, level=logging.DEBUG)


class AltiumServerAPI:
    @staticmethod
    def load_urls(base_url, api_url):
        AltiumServerAPI.BASE_URL = base_url
        AltiumServerAPI.API_URL = api_url

    @staticmethod
    def get_project_list(query=""):
        params = {
            "query": query,
            "orderBy": "modified",
            "order": "desc",
            "page": "0",
            "pageSize": "20",
        }
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "app": "Explorer",
            "authorization": f"AFSSessionID {os.environ['ALTIUM_TOKEN']}",
        }
        response = requests.get(
            f"{AltiumServerAPI.BASE_URL}/svc/explorer/api/v1/entities",
            params=params,
            headers=headers,
        )
        return json.loads(response.content)["entities"]

    @staticmethod
    def get_project(guid):
        headers = {"x-auth": os.environ["ALTIUM_TOKEN"]}

        response = requests.get(
            f"{AltiumServerAPI.API_URL}/widget/get/data/{guid}",
            headers=headers,
        )
        return json.loads(response.content)

    @staticmethod
    def get_project_bom(guid, skip_live_data=True):
        headers = {"x-auth": os.environ["ALTIUM_TOKEN"]}

        params = {
            "skipLiveData": str(skip_live_data).lower(),
        }

        response = requests.get(
            f"{AltiumServerAPI.API_URL}/design/bom/{guid}",
            params=params,
            headers=headers,
        )
        return json.loads(response.content)

    @staticmethod
    def download_json_from_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            logger.error(f"Failed to download from {url}")
            return False
