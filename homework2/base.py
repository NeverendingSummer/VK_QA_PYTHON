import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.ad_page import AdPage


class BaseCase:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, configure, request: FixtureRequest):
        self.driver = driver
        self.base_page:BasePage = (request.getfixturevalue('base_page'))
        self.ad_page:AdPage = (request.getfixturevalue('ad_page'))