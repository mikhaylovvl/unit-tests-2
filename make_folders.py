import requests


def make_folder(url: str, name_folder: str, token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    response = requests.put(url=url+name_folder, headers=headers)
    return response.status_code
