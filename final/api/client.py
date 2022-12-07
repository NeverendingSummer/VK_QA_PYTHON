import json

import requests

session = requests.Session()

data = {
    "login": "testuser",
    "password": "test123",
    "submin": "Login"
}

req = session.post(url='http://172.17.0.3:8080/login',json=data)
print(req.status_code)
print(session.cookies.get_dict())
