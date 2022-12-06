import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.main_page import MainPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.configure = config
        if self.authorize:
            cookies = (request.getfixturevalue('cookies'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.main_page: MainPage = (request.getfixturevalue('main_page'))
