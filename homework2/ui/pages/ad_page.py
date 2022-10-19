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
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AdPage(BasePage):
    locators = basic_locators.AdPageLocators()

    def create_ad_campaign(self, url, timeout=None):
        self.click(basic_locators.AdPageLocators.CREATE_COMPAIGN_LOCATOR, timeout)
        self.wait(timeout).until(ec.presence_of_element_located(basic_locators.AdPageLocators.AD_VISIBILITY_LOCATOR))
        self.click(basic_locators.AdPageLocators.AD_WATCH_VIDEO_LOCATOR, timeout)
        self.wait(timeout).until(ec.presence_of_element_located(basic_locators.AdPageLocators.ENTER_URL_LOCATOR))
        self.find(basic_locators.AdPageLocators.ENTER_URL_LOCATOR).send_keys(url)
        self.wait(timeout).until(ec.presence_of_element_located(basic_locators.AdPageLocators.PREROLL_LOCATOR))
        self.click(basic_locators.AdPageLocators.PREROLL_LOCATOR, timeout)

    def drop_video(self, video, timeout=None):
        self.wait(timeout).until(ec.presence_of_element_located(basic_locators.AdPageLocators.SEND_VIDEO_LOCATOR))
        element = self.driver.find_element(*basic_locators.AdPageLocators.SEND_VIDEO_LOCATOR)
        element.send_keys(video)

    def submit(self, timeout=None):
        self.wait(timeout).until(ec.element_to_be_clickable(basic_locators.AdPageLocators.SAVE_CAMPAIGN_LOCATOR))
        self.click(basic_locators.AdPageLocators.SAVE_CAMPAIGN_LOCATOR)
        self.wait(timeout).until(ec.element_to_be_clickable(basic_locators.AdPageLocators.SUBMIT_CAMPAIGN_LOCATOR))
        self.click(basic_locators.AdPageLocators.SUBMIT_CAMPAIGN_LOCATOR)

    def success_check(self, timeout=None):
        self.wait(timeout).until(ec.element_to_be_clickable(basic_locators.AdPageLocators.SUCCESS_LOCATOR))
