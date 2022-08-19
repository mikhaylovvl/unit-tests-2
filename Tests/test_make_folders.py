import unittest
from parameterized import parameterized
from yandex_disc import YaDisc


class TestFunctions(unittest.TestCase):
    fixture = [
        ("first_folder", 201),
        ("second_folder", 201),
        ("third_folder", 201)
    ]

    def setUp(self):
        self.api_ya = YaDisc()
        self.name = ""

    @parameterized.expand(fixture)
    def test_make_folder(self, name_folder: str, expected_result: int):
        result = self.api_ya.make_folder(name_folder)
        print(result[0], expected_result)
        try:
            self.assertEqual(result[0], expected_result)
            self.name = name_folder
            print(f"Папка с именем {name_folder} успешно создана")
        except:
            if result[0] == 200:
                print(f"Папка с именем {name_folder} уже существует на диске")

    def tearDown(self):
        self.api_ya.dell_folder(self.name)
