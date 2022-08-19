import requests
from dotenv import load_dotenv
import os

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources?path="


class YaDisc:
    load_dotenv()

    def __init__(self):
        self.token = os.getenv("TOKEN")
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _check_folder(self, name_folder: str):
        response = requests.get(url=BASE_URL + name_folder, headers=self.headers)
        return response.status_code

    def make_folder(self, name_folder: str):
        temp_status_code = self._check_folder(name_folder)
        if temp_status_code != 200:
            response_put = requests.put(url=BASE_URL + name_folder, headers=self.headers)
            return response_put.status_code, name_folder
        return temp_status_code, name_folder

    def dell_folder(self, name_folder):
        requests.delete(url=BASE_URL + name_folder, headers=self.headers)

