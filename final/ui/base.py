import time

import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.login_page import LoginPage
from ui.pages.registry_page import RegistryPage
import os
import allure
import shortuuid


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
        uniq = shortuuid.uuid()[::-4]
        if not self.registry_page.get_response() == f'{expect}':
            path = os.path.join('./info', f'failed-{uniq}.png')
            self.driver.get_screenshot_as_file(filename=path)
            allure.attach.file(path, f'failed-{uniq}.png', allure.attachment_type.PNG)
            browser_logs = os.path.join('./info', 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in self.driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n{time.ctime()}")
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'browser.log', allure.attachment_type.TEXT)
            return False
        else:
            return True
