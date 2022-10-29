import requests
from urllib.parse import urljoin
import uuid


class DeletionException(Exception):
    ...


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

        data = {
            "name": f"{name}",
            "pass_condition": 1,
            "flags": ["cross_device"],
            "relations": [
                {
                    "object_type": "remarketing_vk_group",
                    "params": {
                        "type": "positive",
                        "source_id": 153502007
                    }
                }
            ]
        }
        func = self.session.post(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json', json=data,
                                 headers=headers)
        print(func.status_code)

    def create_segment_games(self, name):
        dict = self.session.cookies.get_dict()
        csrf = dict['csrftoken']
        headers = {
            "X-CSRFToken": f'{csrf}'
        }
        data = {"name": f"{name}", "pass_condition": 1, "relations": [
            {"object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}}],
                "logicType": "or"}
        func = self.session.post(url='https://target-sandbox.my.com/api/v2/remarketing/segments.json', json=data,
                                 headers=headers)
        print(func.status_code)

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
                    url=f'https://target-sandbox.my.com/api/v2/remarketing/segments/{buf}.json',
                    headers=headers)
                print(deletion.status_code)

    def post_campaign(self, name):
        dict = self.session.cookies.get_dict()
        csrf = dict['csrftoken']
        headers = {
            "X-CSRFToken": f'{csrf}'
        }

        data = {

            "autobidding_mode": "second_price_mean",
            "name": f"{name}",
            "objective": "videoviews",
            "package_id": 863,
            "price": "0.01",
            "status": "active",
            "banners": [
                {"urls": {"primary": {"id": 697053}}, "content": {"video_landscape_30s": {"id": 8515}}, "name": ""}]
        }
        func = self.session.post(url='https://target-sandbox.my.com/api/v2/campaigns.json', json=data,
                                 headers=headers)
        print(func.status_code)
        print(func.text)


r = ApiClient()
r.login()
res = r.post_test()
pass

