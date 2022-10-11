from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from base import BaseCase
import basic_locators
import pytest
import random


class TestOne(BaseCase):

    # Тест открытия окна авторизации с последующим вводом корректных данных
    @pytest.mark.skip('skip')
    def test_login(self, driver):
        self.login("blessrng17@gmail.com", "testpass123")

    # Параметризованный негативный тест на авторизацию
    @pytest.mark.skip('skip')
    @pytest.mark.parametrize("email, password", [("blessrng17@gmail.com", "testsas123"),
                                                 ("random_email@kek.com", "testpass123")])
    def test_authorize(self, email, password):
        self.authorization(email, password)

    # Тест выхода из профиля
    #@pytest.mark.skip('skip')
    def test_logout(self):
        self.login("blessrng17@gmail.com", "testpass123")
        self.logout()

    # Параметризованный тест на переход по навигационному полю.
    @pytest.mark.skip('skip')
    @pytest.mark.parametrize("nav", [(random.randint(0, 4)),
                                     (random.randint(0, 4))])
    def test_navigation(self, driver, nav):
        self.login("blessrng17@gmail.com", "testpass123")
        self.find(*basic_locators.NAVIGATION_LOCATOR[nav]).click()

    # Тест на изменение информации
    @pytest.mark.skip('skip')
    def test_change_info(self, driver):
        self.login("blessrng17@gmail.com", "testpass123")
        self.change()


