import requests
from urllib.parse import urljoin
import uuid
import json
import os


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


class ApiClient:
    def __init__(self):
        self.session = requests.Session()

    def login(self):
        headers = {
            'Referer': 'https://target-sandbox.my.com/'
        }

        data = {
            'email': 'blessrng17@gmail.com',
            'password': 'testpass123',
            'failure': 'https://account.my.com/login/',
            'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
        }
        self._request(method="POST", given_url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0',
                      headers=headers, data=data, location=None,
                      allow_redirects=True)

    def get_crsf_header(self):
        self.session.get(url='https://target-sandbox.my.com/csrf')
        csrf = self.session.cookies.get_dict()['csrftoken']
        headers = {
            "X-CSRFToken": f'{csrf}'
        }
        return headers

    def _request(self, given_url, method, location, headers, data, params=None, allow_redirects=False):
        url = urljoin(given_url, location)
        self.session.request(method=method, url=url, headers=headers, data=data, params=params,
                             allow_redirects=allow_redirects)

    def post_segment_vk(self, name):
        data = self.read_json(filename='post_segment_vk', name=name)
        self.session.post(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json', json=data,
                          headers=self.get_crsf_header())

    def post_segment_games(self, name):
        data = self.read_json(filename='post_segment_games', name=name)
        self.session.post(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json', json=data,
                          headers=self.get_crsf_header())

    def delete_segment(self, name):
        json = self.session.get(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json').json()
        for i in range(len(json['items'])):
            if str(json['items'][i]['name']) == str(name):
                self.session.delete(
                    url=f'https://target-sandbox.my.com/api/v2/remarketing/segments/{json["items"][i]["id"]}.json',
                    headers=self.get_crsf_header())

    def post_campaign(self, name):
        data = self.read_json(filename='post_campaing', name=name)
        data['banners'][0]['content']['video_landscape_30s']['id'] = f'{self.send_video()}'
        self.session.post(url='https://target-sandbox.my.com/api/v2/campaigns.json', json=data,
                          headers=self.get_crsf_header())

    def delete_campaign(self, name):
        json = self.session.get(
            url='https://target-sandbox.my.com/api/v2/campaigns.json?fields=id%2Cname&sorting=-id&_status__in=active').json()
        for i in range(len(json['items'])):
            if str(json['items'][i]['name']) == str(name):
                self.session.delete(url=f'https://target-sandbox.my.com/api/v2/campaigns/{json["items"][i]["id"]}.json',
                                    headers=self.get_crsf_header())

    def read_json(self, filename, name):
        with open(
                f'{repo_root()}/files/{filename}.json') as f:
            info = json.load(f)
            info['name'] = f'{name}'
        return info

    def send_video(self):
        video = open(f'{repo_root()}/files/ad.mp4', 'rb')
        file = {
            "Content-Type": "multipart/form-data",
            "file": video
        }
        request = self.session.post(url='https://target-sandbox.my.com/api/v2/content/video.json',
                                    headers=self.get_crsf_header(), files=file)
        return request.json()['id']
