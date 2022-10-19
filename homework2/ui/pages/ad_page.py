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

    def create_ad_campaign(self, url, video, timeout=None):
        action = ActionChains(self.driver)
        self.click(basic_locators.AdPageLocators.CREATE_COMPAIGN_LOCATOR, timeout)
        self.wait(timeout).until(ec.presence_of_element_located(basic_locators.AdPageLocators.AD_VISIBILITY_LOCATOR))
        self.click(basic_locators.AdPageLocators.AD_WATCH_VIDEO_LOCATOR, timeout)
        self.wait(timeout).until(ec.presence_of_element_located(basic_locators.AdPageLocators.ENTER_URL_LOCATOR))
        self.find(basic_locators.AdPageLocators.ENTER_URL_LOCATOR).send_keys(url)
        self.wait(timeout).until(ec.presence_of_element_located(basic_locators.AdPageLocators.PREROLL_LOCATOR))
        self.click(basic_locators.AdPageLocators.PREROLL_LOCATOR, timeout)
        self.wait(timeout).until(ec.presence_of_element_located(basic_locators.AdPageLocators.DROP_AREA_LOCATOR))
        self.wait(timeout).until(ec.element_to_be_clickable(basic_locators.AdPageLocators.DRAG_LOCATOR))
        time.sleep(2)
        # # self.d
        # #action.drag_and_drop(basic_locators.AdPageLocators.DRAG_LOCATOR, basic_locators.AdPageLocators.DROP_AREA_LOCATOR).perform()
        # test = action.drag_and_drop(self.driver.find_element(By.XPATH, "//div[contains(@class, '-module-imageContainer-')]"),
        #                             (self.driver.find_element(By.XPATH, "//div[@class='videoPreview-module-audio-pLGsdk videoPreview-module-emptyWrap-2u_UGe']")))
        # test.perform()
        # time.sleep(15)
        action.click_and_hold(self.driver.find_element(By.XPATH, "//div[contains(@class, '-module-imageContainer-')]")).perform()
        action.move_to_element((self.driver.find_element(By.XPATH, "//div[@class='videoPreview-module-audio-pLGsdk videoPreview-module-emptyWrap-2u_UGe']"))).perform()
        action.release().perform()
        time.sleep(2)
        # self.find(basic_locators.AdPageLocators.SEND_VIDEO_LOCATOR).send_keys(video)
        self.wait(timeout).until(ec.element_to_be_clickable(basic_locators.AdPageLocators.SUBMIT_CAMPAIGN_LOCATOR))
        self.click(basic_locators.AdPageLocators.SUBMIT_CAMPAIGN_LOCATOR)
        time.sleep(15)