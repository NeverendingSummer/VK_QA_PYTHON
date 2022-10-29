import requests
# class ApiClient:
#     def __init__(self, base_url: str):
#         self.base_url = base_url
#
#     def get_token(self):
#         headers = requests.get(url=self.base_url).headers
#         pass
#
# c = ApiClient(base_url='https://target-sandbox.my.com/')
# c.get_token()
# pass
#     # def post_login(self):
#     #     token = self.get_token()
#     #     headers = {
#     #         'Cookie': f'csrftoken={token}',
#     #         'X-CSRFToken': f'{token}'
#     #     }
#

class ApiClient:
    def __init__(self, base_url: str, login: str, password: str):
        self.base_url = base_url

        self.login = login
        self.password = password

        self.session = requests.Session()

    def get_token(self):
        headers = requests.get(url=self.base_url).headers['Set-Cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken']
        if not token_header:
            raise Exception('Expected csrftoken in Set-Cookie')
        token_header = token_header[0].split('=')[-1]
        return token_header

    def post_login(self):
        token = self.get_token()
        headers = {
            'Cookie': f'csrftoken={token}',
            'X-CSRFToken': f'{token}'
        }

        data = {
            'login': self.login,
            'password': self.password
        }
        login_request = self.session.post(url='https://education.vk.company/login/', headers=headers, data=data)

        return login_request


c = ApiClient(base_url="https://education.vk.company", login="glowart228@gmail.com", password="!Eq5Bx9!D6dfdfdfxWGTN")
res = c.post_login()


