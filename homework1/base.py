import pytest
import basic_locators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import selenium.common.exceptions
from selenium.common.exceptions import *



class BaseCase:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver

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
        try:
            WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable(basic_locators.test_locator))
            self.find(*basic_locators.LOGOUT_LOCATOR).click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable(basic_locators.test_locator))
            self.find(*basic_locators.LOGOUT_LOCATOR).click()

    def change(self):
        now = datetime.datetime.now()
        self.driver.get("https://target-sandbox.my.com/profile/contacts")
        WebDriverWait(self.driver, 1).until(ec.element_to_be_clickable(basic_locators.FIO_LOCATOR))
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
            self.find(*basic_locators.ENTER_LOCATOR).click()
            assert self.driver.current_url == "https://target-sandbox.my.com/dashboard"
        except AssertionError:
            print("Введены неверные данные")
