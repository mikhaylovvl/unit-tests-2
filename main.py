import os
from dotenv import load_dotenv
from make_folders import make_folder

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources?path="

if __name__ == '__main__':
    load_dotenv()
    token = os.getenv("TOKEN")

    print(make_folder(BASE_URL, "new_folder", token))


