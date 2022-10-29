import requests


s = requests.session()


data = {
    "email": "blessrng17@gmail.com",
    "password": "testpass123",
    "failure": "https://account.my.com/login/",
    "continue": "https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email"
}

headers = {
    "Referer": "https://target-sandbox.my.com/"
}

login = s.post("https://auth-ac.my.com/auth?lang=ru&nosavelogin=0", data=data, headers=headers, allow_redirects=True)
print(login.status_code)
print(login.cookies)
print(login.__dict__)


r = s.get("https://target-sandbox.my.com/api/v2/ord_user/user.json")
print(r.status_code)
print(r.text)


print(s.cookies)

csrf = s.get("https://target-sandbox.my.com/csrf")
print(csrf.status_code)
print(csrf.text)
print(s.cookies)
data = {
            "age_restrictions": None,
            "autobidding_mode": "second_price_mean",
            "budget_limit": None,
            "budget_limit_day": None,
            "created": "2022-10-31 03:20:29",
            "delivery": "pending",
            "enable_utm": True,
            "id": 2092092,
            "interface_read_only": False,
            "issues": [
                {
                    "arguments": {},
                    "code": "NO_ALLOWED_BANNERS",
                    "message": "The campaign has no banners, approved by moderation."
                }
            ],
            "name": "Новая кампания 31.10.2022 03:19:59",
            "objective": "videoviews",
            "package_id": 863,
            "package_priced_event_type": 1013,
            "pads_ots_limits": [],
            "price": "0.01",
            "prices": {
                "additional": {
                    "marketplace_app": "0.00",
                    "moat": "0.00",
                    "pricelist": "0.00",
                    "segments": "0.00",
                    "targetings": "0.00"
                },
                "final": "0.01",
                "origin": "0.01",
                "revenue_share": {
                    "pricelist": "0.0000"
                }
            },
            "read_only": False,
            "status": "active",
            "targetings": {
                "pads": [
                    106790,
                    106791
                ],
                "split_audience": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10
                ]
            },
            "user_id": 1856536,
            "utm": None
        }