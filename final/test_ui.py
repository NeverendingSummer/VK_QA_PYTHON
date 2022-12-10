import pytest
from ui.faker_info import create_fake_info
from ui.base import BaseCase
from selenium.common.exceptions import *
import time


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

    def test_(self, create_fake_info_fixture):
        self.registry_page.insert_values(' ', *create_fake_info_fixture[1:])
        print(self.registry_page.get_response())
        print("HERE IN TEST")
        # time.sleep(5)
