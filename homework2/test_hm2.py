from base import BaseCase


class TestTwo(BaseCase):

    def test_login(self):
        self.base_page.login("blessrng17@gmail.com", "testpass123", timeout=15)

    def test_create_campaing(self):
        ad_url = "https://www.nestle.com/brands/chocolate-confectionery/kitkat"
        video = 'D:/Программирование/ДЗ_сдача/2022-2-VK-QA-PYTHON-ayypeegeepee/homework2/files/ad.mp4'
        self.base_page.login("blessrng17@gmail.com", "testpass123", timeout=15)
        self.ad_page.create_ad_campaign(ad_url, timeout=15)
        self.ad_page.drop_video(video, timeout=15)
        self.ad_page.submit(timeout=15)
        self.ad_page.success_check(timeout=15)
