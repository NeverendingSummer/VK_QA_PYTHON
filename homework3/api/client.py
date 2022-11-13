import requests
from urllib.parse import urljoin
import uuid
import json
import os

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
        login_session = self._request(method="POST", given_url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0',
                                      headers=headers, data=data, location=None,
                                      allow_redirects=True)

        self.session.get(url='https://target-sandbox.my.com/csrf')
        return login_session

    def _request(self, given_url, method, location, headers, data, params=None, allow_redirects=False):
        url = urljoin(given_url, location)
        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params,
                                        allow_redirects=allow_redirects)
        code = response.status_code

    def post_segment_vk(self, name):
        dict = self.session.cookies.get_dict()
        csrf = dict['csrftoken']
        headers = {
            "X-CSRFToken": f'{csrf}'
        }

        data = self.read_json(filename='post_segment_vk')
        func = self.session.post(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json', json=data,
                                 headers=headers)

    def post_segment_games(self, name):
        dict = self.session.cookies.get_dict()
        csrf = dict['csrftoken']
        headers = {
            "X-CSRFToken": f'{csrf}'
        }
        data = self.read_json(filename='post_segment_games')
        func = self.session.post(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json', json=data,
                                 headers=headers)

    def delete_segment(self, name):
        dict = self.session.cookies.get_dict()
        csrf = dict['csrftoken']
        headers = {
            "X-CSRFToken": f'{csrf}'
        }
        json = self.session.get(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json').json()
        for i in range(len(json['items'])):
            if str(json['items'][i]['name']) == str(name):
                buf = json['items'][i]['id']
                deletion = self.session.delete(
                    url=f'https://target-sandbox.my.com/api/v2/remarketing/segments/{buf}.files',
                    headers=headers)

    def post_campaign(self, name):
        dict = self.session.cookies.get_dict()
        csrf = dict['csrftoken']
        headers = {
            "X-CSRFToken": f'{csrf}'
        }

        data = self.read_json(filename='post_campaing')
        func = self.session.post(url='https://target-sandbox.my.com/api/v2/campaigns.json', json=data,
                                 headers=headers)


    def delete_campaign(self, name):
        dict = self.session.cookies.get_dict()
        csrf = dict['csrftoken']
        headers = {
            "X-CSRFToken": f'{csrf}'
        }
        json = self.session.get(
            url='https://target-sandbox.my.com/api/v2/campaigns.json?fields=id%2Cname&sorting=-id&_status__in=active').json()
        for i in range(len(json['items'])):
            if str(json['items'][i]['name']) == str(name):
                buf = json['items'][i]['id']
                deletion = self.session.delete(url=f'https://target-sandbox.my.com/api/v2/campaigns/{buf}.files',
                                               headers=headers)

    def read_json(self, filename):
        name = uuid.uuid4()
        path = self.repo_root()
        with open(
                f'{path}/files/{filename}.json') as f:
            info = json.load(f)
            info['name'] = f'{name}'
        return info

    def repo_root(self):
        return os.path.abspath(os.path.join(__file__, os.path.pardir))

