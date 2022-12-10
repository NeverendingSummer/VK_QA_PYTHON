import pytest
from ui.faker_info import create_fake_info
from ui.base import BaseCase
from selenium.common.exceptions import *
import time


def logging(info):
    time.sleep(1)
    log = open('logs/logs.txt', 'w')
    log.write(f"{info}\n")
    log.close()


class TestTwo(BaseCase):
    authorize = False

    @pytest.mark.skip("SKIP")
    def test_normal_registry(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture)
        assert self.registry_page.check_registration() == create_fake_info_fixture[2]

    @pytest.mark.skip("SKIP")
    def test_overextended_name(self, create_fake_info_fixture):
        self.registry_page.insert_values(' ', *create_fake_info_fixture[1:])
        time.sleep(5)
        with pytest.raises(NoSuchElementException):
            self.registry_page.check_registration()

    def test_name(self, create_fake_info_fixture):
        self.registry_page.insert_values(' ', *create_fake_info_fixture[1:])
        print(self.registry_page.get_response())
        logging(self.registry_page.get_response())

    def test_surname(self, create_fake_info_fixture):
        self.registry_page.insert_values(create_fake_info_fixture[0], ' ', *create_fake_info_fixture[2:])
        print(self.registry_page.get_response())
        logging(self.registry_page.get_response())

    def test_username(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture[0:2], '      ', *create_fake_info_fixture[3:])
        print(self.registry_page.get_response())
        logging(self.registry_page.get_response())

    def test_email(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture[0:3], '      ', *create_fake_info_fixture[4:])
        print(self.registry_page.get_response())
        logging(self.registry_page.get_response())

    def test_password(self, create_fake_info_fixture):
        self.registry_page.insert_values(*create_fake_info_fixture[0:4], ' ')
        print(self.registry_page.get_response())
        logging(self.registry_page.get_response())
