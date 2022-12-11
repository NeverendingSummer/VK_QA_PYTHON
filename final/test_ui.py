import pytest
from ui.faker_info import create_fake_info
from ui.base import BaseCase
from selenium.common.exceptions import *
import time
import allure


@pytest.mark.UI
@allure.link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", name='Click me')
class TestUI(BaseCase):
    authorize = False

    def test_normal_registry(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture)
        assert self.registry_page.check_registration() == create_fake_info_fixture[2]

    # @pytest.mark.skip("SKIP")
    @pytest.mark.parametrize("name", ['', ' ', '      ', '123123123', '$%^&*?', 'абвгдеёж'])
    def test_name_incorrect(self, create_fake_info_fixture, name):
        self.registry_page.insert_values(name, *create_fake_info_fixture[1:])
        if not self.assert_expected('Некорректное имя'):
            allure.attach(self.registry_page.get_response())
            raise AssertionError
        else:
            pass

    # @pytest.mark.skip("SKIP")
    @pytest.mark.parametrize("surname", ['', ' ', '      ', '123123123', '$%^&*?', 'абвгдеёж'])
    def test_surname_incorrect(self, create_fake_info_fixture, surname):
        self.registry_page.insert_values(create_fake_info_fixture[0], surname, *create_fake_info_fixture[2:])
        if not self.assert_expected('Некорректная фамилия'):
            allure.attach(self.registry_page.get_response())
            raise AssertionError
        else:
            pass

    # @pytest.mark.skip("SKIP")
    @pytest.mark.parametrize("username", ['', ' ', '      ', '123123123', '$%^&*?', 'абвгдеёж'])
    def test_username_incorrect(self, create_fake_info_fixture, username):
        self.registry_page.insert_values(*create_fake_info_fixture[0:2], username, *create_fake_info_fixture[3:])
        if not self.assert_expected('Некорректное имя пользователя'):
            raise AssertionError
        else:
            pass

    # @pytest.mark.skip("SKIP")
    @pytest.mark.parametrize("email", ['@', ' @ ', '@test.com', ' ', '$%^&*?@$%^&*', '@.ru', 'русcкая@почта.ком'])
    def test_email_incorrect(self, create_fake_info_fixture, email):
        self.registry_page.insert_values(*create_fake_info_fixture[0:3], email, *create_fake_info_fixture[4:])
        if not self.assert_expected('Некорректная почта'):
            allure.attach(self.registry_page.get_response())
            raise AssertionError
        else:
            pass

    # @pytest.mark.skip("SKIP")
    @pytest.mark.parametrize("password", ['', ' ', '      ', '123123123', '123123123'])
    def test_password_incorrect(self, create_fake_info_fixture, password):
        self.registry_page.insert_values(*create_fake_info_fixture[0:4], password)
        if not self.assert_expected('Некорректный пароль'):
            allure.attach(self.registry_page.get_response())
            raise AssertionError
        else:
            pass
