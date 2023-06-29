import json
from pprint import pprint
import requests


class YandexDisk:
    def __init__(self, token: str):
        self.token = TOKEN
        self.yandex_url = 'https://cloud-api.yandex.net/'

    def get_headers(self):

        return {'Content-Type': 'application\\json',
                'Authorization': f'OAuth {self.token}'
                }

    def get_file_list(self):
        files_url = f'{self.yandex_url}v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=files_url, headers=headers)
        # pprint(response.json())
        return response.json()

    def get_upload_link(self, disk_file_path):
        upload_url = f'{self.yandex_url}v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def get_upload_file(self, disk_file_path, file_name):
        href_response = self.get_upload_link(disk_file_path=disk_file_path)
        href = href_response.get("href", "")
        href_response = requests.put(url=href, data=open(file_name, 'rb'))
        if href_response.status_code == 201:
            print(file_name + " " + "Загружен")


TOKEN = ' '
# if __name__ == '__Yandex_disk__':
ya = YandexDisk(token=TOKEN)
# работает когда файл находиттся в директории проекта
ya.get_upload_file("1.txt", "1.txt")
# pprint(ya.get_file_list())
