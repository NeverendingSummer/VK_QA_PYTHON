import requests

r = requests.get('https://auth-ac.my.com/auth?lang=ru&nosavelogin=0')

test = r.history
r = requests.get('https://target-sandbox.my.com/auth/mycom?state=target_login=1&ignore_opener=1')
test3 = r.history
test2 = r.url
print(test, test3)