from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import selenium.common.exceptions
from ui.locators import basic_locators

class BasePage(object):
    locators = basic_locators

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(ec.presence_of_element_located(locator))

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(ec.element_to_be_clickable(locator))
        elem.click()

    def insert(self, email, password):
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(basic_locators.LOGIN_LOCATOR))
        self.find(*basic_locators.LOGIN_LOCATOR).click()
        self.find(*basic_locators.USERNAME_LOCATOR).send_keys(email)
        self.find(*basic_locators.PASSWORD_LOCATOR).send_keys(password)

    def find(self, by, what):
        return self.driver.find_element(by, what)

    def login(self, email, password):
        self.insert(email, password)
        self.find(*basic_locators.ENTER_LOCATOR).click()
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(basic_locators.DISPLAYED_SITE_LOCATOR))

    def logout(self):
        self.find(*basic_locators.PROFILE_LOCATOR).click()
        time.sleep(1)  # работает только он, я без понятия как фиксить
        self.find(*basic_locators.LOGOUT_LOCATOR).click()
        WebDriverWait(self.driver, 15).until(ec.presence_of_element_located(basic_locators.BASEPAGE_LOCATOR))

    def change(self):
        now = datetime.datetime.now()
        self.driver.get("https://target-sandbox.my.com/profile/contacts")
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(basic_locators.FIO_LOCATOR))
        action = ActionChains(self.driver)
        action_storage = self.find(*basic_locators.FIO_LOCATOR)
        action.double_click(action_storage).send_keys(Keys.DELETE).send_keys(f"newtestfio{now.minute}").perform()
        action_storage = self.find(*basic_locators.SUBMIT_LOCATOR)
        action.click(action_storage).perform()
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(basic_locators.SUBMIT_LOCATOR))
        self.find(*basic_locators.SUBMIT_LOCATOR).click()

    def authorization(self, email, password):
        self.insert(email, password)
        try:
            self.find(*basic_locators.DISPLAYED_SITE_LOCATOR)
        except selenium.common.exceptions.NoSuchElementException:
            print("Введены неверные данные")
