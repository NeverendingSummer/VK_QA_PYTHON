import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from ui.locators import locators


class LoginPage(object):
    locators = locators.BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 3
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_located(self, locator, timeout=None):
        return self.wait(timeout).until(ec.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.wait_located(locator, timeout=timeout)
        self.wait(timeout).until(ec.element_to_be_clickable(locator)).click()

    def wait_clickable(self, locator, timeout=None):
        return self.wait(timeout).until(ec.element_to_be_clickable(locator))

    def wait_and_click(self, what, timeout=None):
        self.wait_clickable(what, timeout=3)
        self.click(what)

    def insert_login_info(self, username, password):
        self.wait_clickable(self.locators.login_locator).send_keys(username)
        self.wait_clickable(self.locators.password_locator).send_keys(password)

    def login(self, username, password, timeout=None):
        self.insert_login_info(username, password)
        self.wait_clickable(self.locators.submit_locator).click()
        self.wait_located(self.locators.entered_page_locator)
