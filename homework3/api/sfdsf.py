import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_token(self):
        headers = requests.get(url=self.base_url).headers
        token_header = [h for h in headers if 'csrftoken']
        return token_header

urls  = ('https://target-sandbox.my.com/', 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0',
         'https://target-sandbox.my.com/auth/mycom?state=target_login=1&ignore_opener=1')

for i in range(len(urls)):
    c = ApiClient(base_url=urls[i])
    res = c.get_token()

headers = requests.get(url='https://target-sandbox.my.com/auth/mycom?state=target_login=1&ignore_opener=1').headers['set-cookie']

pass

# auth?lang=ru&nosavelogin=0
# https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1
# https://auth-ac.my.com/sdc?from=http%3A%2F%2Ftarget-sandbox.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526ignore_opener%253D1
#
#
#
#