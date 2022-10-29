import requests


s = requests.session()


data = {
    'email': 'blessrng17@gmail.com',
    'password': 'testpass123',
    'failure': 'https://account.my.com/login/',
    'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
}

headers = {
    'Referer': 'https://target-sandbox.my.com/'
}

login = s.post("https://auth-ac.my.com/auth?lang=ru&nosavelogin=0", data=data, headers=headers, allow_redirects=True)
print(login.status_code)
print(login.cookies)
print(login.__dict__)


r = s.get("https://target-sandbox.my.com/api/v2/ord_user/user.json")
print(r.status_code)
print(r.text)
# #
# #
# # print(s.cookies)
#
# csrf = s.get("https://target-sandbox.my.com/csrf")
# print(csrf.status_code)
# print(csrf.text)
# print(s.cookies)