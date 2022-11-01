import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from ui.locators import basic_locators


class BasePage(object):
    locators = basic_locators.BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(ec.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(ec.element_to_be_clickable(locator))
        elem.click()

    def insert(self, email, password):
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(self.locators.LOGIN_LOCATOR))
        self.find(self.locators.LOGIN_LOCATOR).click()
        self.find(self.locators.USERNAME_LOCATOR).send_keys(email)
        self.find(self.locators.PASSWORD_LOCATOR).send_keys(password)

    def wait_clickable(self, locator, timeout=None):
        return self.wait(timeout).until(ec.element_to_be_clickable(locator))

    def login(self, email, password, timeout=None):
        self.insert(email, password)
        self.find(self.locators.ENTER_LOCATOR).click()
        # self.wait(timeout).until(ec.element_to_be_clickable(self.locators.DISPLAYED_SITE_LOCATOR))

    def wait_and_click(self, what, timeout=None):
        self.wait_clickable(what, timeout=15)
        self.click(what)