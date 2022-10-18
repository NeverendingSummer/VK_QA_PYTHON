from base import BaseCase
from ui.locators import basic_locators
import pytest
import random


class TestOne(BaseCase):

    # Тест открытия окна авторизации с последующим вводом корректных данных
    #@pytest.mark.skip('skip')
    def test_login(self, driver):
        self.base_page.login("blessrng17@gmail.com", "testpass123")

    # Параметризованный негативный тест на авторизацию
    @pytest.mark.skip('skip')
    @pytest.mark.parametrize("email, password", [("blessrng17@gmail.com", "testsas123"),
                                                 ("random_email@kek.com", "testpass123")])
    def test_authorize(self, email, password):
        self.base_page.authorization(email, password)

    # Тест выхода из профиля
    @pytest.mark.skip('skip')
    def test_logout(self):
        self.base_page.login("blessrng17@gmail.com", "testpass123")
        self.base_page.logout()

    # # Параметризованный тест на переход по навигационному полю. Правда из пула убран PRO, потому что он по кд ломается
    # @pytest.mark.skip('skip')
    # @pytest.mark.parametrize("nav", [(random.randint(0, 4)),
    #                                  (random.randint(0, 4))])
    # def test_navigation(self, driver, nav):
    #     self.base_page.login("blessrng17@gmail.com", "testpass123")
    #     self.base_page.find(*basic_locators.NAVIGATION_LOCATOR[nav]).click()

    # Тест на изменение информации
    @pytest.mark.skip('skip')
    def test_change_info(self, driver):
        self.base_page.login("blessrng17@gmail.com", "testpass123")
        self.base_page.change()


