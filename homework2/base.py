import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.ad_page import AdPage
from ui.pages.groups_page import GroupsPage
from ui.pages.segment_page import SegmentPage
import os
import allure


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, configure, logger, request: FixtureRequest):
        self.driver = driver
        self.logger = logger
        self.configure = configure
        if self.authorize:
            cookies = (request.getfixturevalue('cookies'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.ad_page: AdPage = (request.getfixturevalue('ad_page'))
        self.segment_page: SegmentPage = (request.getfixturevalue('segment_page'))
        self.groups_page: GroupsPage = (request.getfixturevalue('groups_page'))


    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            self.driver.save_screenshot(filename=screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)