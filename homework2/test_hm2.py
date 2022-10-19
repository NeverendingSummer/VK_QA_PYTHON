from base import BaseCase
from ui.locators import basic_locators
import pytest



class TestTwo(BaseCase):


    @pytest.mark.skip('skip')
    def test_ad_company(self):
        self.base_page.login("blessrng17@gmail.com", "testpass123", timeout=15)

    def test_create_campaing(self):
        ad_url = "https://www.nestle.com/brands/chocolate-confectionery/kitkat"
        video = 'D:/Программирование/ДЗ_сдача/2022-2-VK-QA-PYTHON-ayypeegeepee/homework2/files/ad.mp4'
        self.base_page.login("blessrng17@gmail.com", "testpass123", timeout=15)
        self.ad_page.create_ad_campaign(ad_url, video, timeout=15)
