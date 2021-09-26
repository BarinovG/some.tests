import requests
import time

token = ''

uri = 'https://cloud-api.yandex.net'
headers = {
    'Accept': 'application/json',
    'Authorization': 'OAuth {}'.format(token)}


def check_status():
    response = requests.get(uri + '/v1/disk', headers=headers)
    return response.status_code


def check_folder(path):
    params = {'path': path}
    response = requests.get(uri + '/v1/disk/resources', headers=headers, params=params)
    if response.status_code == 200:
        return True
    else:
        return False


def create_folder(path):
    time.sleep(1)
    params = {'path': path}
    if check_folder(path) is True:
        return f'already yet'
    response = requests.put(uri + '/v1/disk/resources', headers=headers, params=params)
    time.sleep(1)
    if response.status_code == 201:
        code_status = response.status_code
        return code_status, check_folder(path)
    return f'check status'
