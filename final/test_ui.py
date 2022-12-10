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

    @pytest.mark.skip("SKIP")
    def test_normal_registry(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture)
        assert self.registry_page.check_registration() == create_fake_info_fixture[2]

    def test_name_incorrect(self, create_fake_info_fixture):
        self.registry_page.insert_values(' ', *create_fake_info_fixture[1:])
        # print(self.registry_page.get_response())
        allure.attach(self.registry_page.get_response())
        self.assert_expected('Неверная информация')

    @pytest.mark.skip("SKIP")
    def test_surname_incorrect(self, create_fake_info_fixture):
        self.registry_page.insert_values(create_fake_info_fixture[0], ' ', *create_fake_info_fixture[2:])
        print(self.registry_page.get_response())

    @pytest.mark.skip("SKIP")
    def test_username_incorrect(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture[0:2], '      ', *create_fake_info_fixture[3:])
        print(self.registry_page.get_response())

    @pytest.mark.skip("SKIP")
    def test_email_incorrect(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture[0:3], '      ', *create_fake_info_fixture[4:])
        print(self.registry_page.get_response())

    @pytest.mark.skip("SKIP")
    def test_password_incorrect(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture[0:4], ' ')
        print(self.registry_page.get_response())
