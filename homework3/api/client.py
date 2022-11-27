import requests
from urllib.parse import urljoin
import uuid
import json
import os


def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


class SegmentNotCreated(Exception):
    pass


class CampaignNotCreated(Exception):
    pass


class SegmentNotDeleted(Exception):
    pass


class CampaignNotDeleted(Exception):
    pass


class ApiClient:
    def __init__(self):
        self.session = requests.Session()

    def login(self):
        global token
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

        self.session.get(url='https://target-sandbox.my.com/csrf')
        csrf = self.session.cookies.get_dict()['csrftoken']
        token = {
            "X-CSRFToken": f'{csrf}'
        }
        return token

    def _request(self, given_url, method, location, headers, data, params=None, allow_redirects=False):
        url = urljoin(given_url, location)
        self.session.request(method=method, url=url, headers=headers, data=data, params=params,
                             allow_redirects=allow_redirects)

    def post_segment_vk(self, name):
        data = self.read_json(filename='post_segment_vk', name=name)
        action = self.session.post(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json', json=data,
                                   headers=token)
        return action.json(), action.status_code

    def post_segment_games(self, name):
        data = self.read_json(filename='post_segment_games', name=name)
        action = self.session.post(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json', json=data,
                                   headers=token)
        return action.json(), action.status_code

    def delete_segment(self, id):
        return self.session.delete(
            url=f'https://target-sandbox.my.com/api/v2/remarketing/segments/{id["id"]}.json',
            headers=token).status_code

    def post_campaign(self, name):
        data = self.read_json(filename='post_campaing', name=name)
        data['banners'][0]['content']['video_landscape_30s']['id'] = f'{self.send_video()}'
        data['banners'][0]['urls']['primary']['id'] = f'{self.get_ad_url(url="https://www.nestle.com/brands/chocolate-confectionery/kitkat")}'
        action = self.session.post(url='https://target-sandbox.my.com/api/v2/campaigns.json', json=data,
                                   headers=token)
        return action.json(), action.status_code

    def delete_campaign(self, id):
        return self.session.delete(url=f'https://target-sandbox.my.com/api/v2/campaigns/{id["id"]}.json',
                                   headers=token).status_code

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
                                    headers=token, files=file)
        return request.json()['id']

    def get_ad_url(self,url):
        action = self.session.get(
            url=f'https://target-sandbox.my.com/api/v1/urls/?url={url}',
            headers=token)
        return action.json()["id"]


