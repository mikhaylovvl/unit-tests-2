import os
import unittest
from parameterized import parameterized
from make_folders import make_folder
from dotenv import load_dotenv


class TestFunctions(unittest.TestCase):
    load_dotenv()
    token = os.getenv("TOKEN")

    fixture = [("https://cloud-api.yandex.net/v1/disk/resources?path=", "first_folder", token, 201),
               ("https://cloud-api.yandex.net/v1/disk/resources?path=", "second_folder", token, 201),
               ("https://cloud-api.yandex.net/v1/disk/resources?path=", "second_folder", token, 409)]

    @parameterized.expand(fixture)
    def test_make_folder(self, url: str, name_folder: str, token, expected_result) -> int:
        result = make_folder(url, name_folder, token)
        self.assertEqual(result, expected_result)
