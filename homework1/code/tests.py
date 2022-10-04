from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from base import BaseCase
from ui.locators import basic_locators
import pytest
import random


class TestOne(BaseCase):

    # Тест открытия окна авторизации с последующим вводом корректных данных
    def test_login(self, driver):
        self.login("blessrng17@gmail.com", "testpass123")

    # Параметризованный негативный тест на авторизацию
    @pytest.mark.parametrize("email, password", [("blessrng17@gmail.com", "testsas123"),
                                                 ("random_email@kek.com", "testpass123")])
    def test_autorize(self, email, password):
        self.autorization(email, password)

    # Тест выхода из профиля
    def test_logout(self):
        self.login("blessrng17@gmail.com", "testpass123")
        self.logout()

    # Параметризованный тест на переход по навигационному полю. Правда из пула убран PRO, потому что он по кд ломается
    @pytest.mark.parametrize("nav", [(random.randint(0, 4)),
                                     (random.randint(0, 4))])
    def test_navigation(self, driver, nav):
        self.login("blessrng17@gmail.com", "testpass123")
        self.find(*basic_locators.NAVIGATION_LOCATOR[nav]).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(basic_locators.URL_LOCATOR[nav]))
        self.find(*basic_locators.URL_LOCATOR[nav])

    # Тест на изменение информации
    def test_change_info(self, driver):
        self.login("blessrng17@gmail.com", "testpass123")
        self.change()


