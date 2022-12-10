import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.login_page import LoginPage
from ui.pages.registry_page import RegistryPage
import os
import allure

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
        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        self.registry_page: RegistryPage = (request.getfixturevalue('registry_page'))

    def assert_expected(self, expect):
        if not self.registry_page.get_response() == f'{expect}':
            path = os.path.join('./logs', 'failed.png')
            self.driver.get_screenshot_as_file(filename=path)
            allure.attach.file(path, 'failed.png', allure.attachment_type.PNG)
