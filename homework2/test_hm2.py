from base import BaseCase
from ui.locators import basic_locators
import pytest
import random


class TestTwo(BaseCase):

    def test_ad_company(self):
        self.base_page.login("blessrng17@gmail.com", "testpass123")
