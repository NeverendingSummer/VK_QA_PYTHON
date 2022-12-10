import json

import requests

session = requests.Session()
headers = {
    "Origin": "http://172.17.0.3:8080/",
    "Referer": "http://172.17.0.3:8080/login"
}
data = {
    "username": "testuser",
    "password": "test123",
}

req = session.post(url='http://172.17.0.3:8080/login', json=data,
                   )
print(req.status_code)
print(session.cookies.get_dict())
