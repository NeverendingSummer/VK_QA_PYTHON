        # zz = self.session.cookies
        # return zz

# r = ApiClient()
# res = r.login()
# pass

    # def hz(self):
    #     cs = self.login()
    #     token_name = []
    #     token_value = []
    #     for cookie in cs:
    #         token_name.append(f'{cookie}')
    #         token_value.append(cs[f'{cookie}'])
    #     for i in range(len(token_value)):
    #         print(f"{token_name[i]}={token_value[i]}")
    #
    #     headers = {
    #         'Cookie': f"{token_name[0]}={token_value[0]};"
    #                   f"{token_name[1]}={token_value[1]};"
    #                   f"{token_name[2]}={token_value[2]};"
    #                   f"{token_name[3]}={token_value[3]};"
    #                   f"{token_name[4]}={token_value[4]};"
    #                   f"{token_name[5]}={token_value[5]};",
    #
    #     }
    #
    #     data = {
    #         'email': 'blessrng17@gmail.com',
    #         'password': 'testpass123',
    #         'failure': 'https://account.my.com/login/',
    #         'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
    #     }
    #     login_request = self.session.post(url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0', headers=headers, data=data,
    #                       allow_redirects=True)
    #     return login_request


# r = requests.get(url)
# for i, each in enumerate(r.history, 1):
#     print(f'{i} {each.status_code} {each.url}')





# cc = self.session.cookies.values()
# cs = self.session.cookies.get_dict()
# login_cookies = login.cookies
# csrf_token = csrf.cookies
# print(login_cookies, csrf_token)
# print(login.status_code, csrf.status_code, user.status_code)
# test_1 = []
# for cooks in cs:
#     test_1.append({
#         f'{cooks}': cs[f'{cooks}']
#     })
# return login, csrf, user, login_cookies, csrf.cookies, cc, test_1

# import requests
#
# class ApiClientException(Exception):
#     ...
#
# print("sdfsdfsdf")
#
#
# class ApiClient:
#     def __init__(self):
#         self.session = requests.Session()
#
#     def login(self):
#         headers = {
#             'Referer': 'https://target-sandbox.my.com/'
#         }
#
#         data = {
#             'email': 'blessrng17@gmail.com',
#             'password': 'testpass123',
#             'failure': 'https://account.my.com/login/',
#             'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
#         }
#         login = self.session.post(url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0', headers=headers, data=data, allow_redirects=True)
#         csrf = self.session.get(url='https://target-sandbox.my.com/csrf')
#         user = self.session.get(url='https://target-sandbox.my.com/api/v2/ord_user/user.json')
#         cc = self.session.cookies.values()
#
#         for i, each in enumerate(login.history, 1):
#             print(f'{i} {each.status_code} {each.url}')
#
#         login_cookies = login.cookies
#         csrf_token = csrf.cookies
#         print(login_cookies, csrf_token)
#         print(login.status_code, csrf.status_code, user.status_code)
#         cs = self.session.cookies.get_dict()
#         test_1 = []
#         test_2 = []
#         token_name = []
#         token_value = []
#         for cooks in cs:
#             token_name.append(f'{cooks}')
#             token_value.append(cs[f'{cooks}'])
#         for i in range(len(token_value)):
#             print(f"{token_name[i]}={token_value[i]}")
#
#
#         return login, csrf, user, login_cookies, csrf.cookies, cc, token_name, cs, token_value
#
# c = ApiClient()
# res = c.login()
# print(res)
# test = requests.get(url="https://target-sandbox.my.com/dashboard")
# url = 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
# print(test.status_code)
# pass