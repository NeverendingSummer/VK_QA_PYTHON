import selenium.webdriver.support.expected_conditions as ec
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class AdPage(BasePage):
    locators = basic_locators.AdPageLocators()

    @allure.step("Функция create_ad_campaign выполняет последовательно все шаги до загрузки видео")
    def create_ad_campaign(self, url, timeout=None):
        self.click(basic_locators.AdPageLocators.CREATE_CAMPAIGN_LOCATOR)
        self.wait_presence(basic_locators.AdPageLocators.AD_VISIBILITY_LOCATOR, timeout=15)
        self.click(basic_locators.AdPageLocators.AD_WATCH_VIDEO_LOCATOR)
        self.wait_presence(basic_locators.AdPageLocators.ENTER_URL_LOCATOR, timeout=15)
        self.find(basic_locators.AdPageLocators.ENTER_URL_LOCATOR).send_keys(url)
        self.wait_presence(basic_locators.AdPageLocators.PREROLL_LOCATOR, timeout=15)
        self.click(basic_locators.AdPageLocators.PREROLL_LOCATOR)

    @allure.step("Функция drop_video выполняет отправку видео файла из папки files")
    def drop_video(self, file_path, timeout=None):
        self.wait_presence(basic_locators.AdPageLocators.SEND_VIDEO_LOCATOR, timeout=15)
        element = self.driver.find_element(*basic_locators.AdPageLocators.SEND_VIDEO_LOCATOR)
        element.send_keys(file_path)

    @allure.step("Функция submit меняет имя на сгенерированный UUID")
    def submit(self, campaing_name, timeout=None):
        self.wait_clickable(basic_locators.AdPageLocators.COMPANY_NAME_LOCATOR, timeout=15)
        self.click(basic_locators.AdPageLocators.CLEAR_NAME_LOCATOR)
        self.find(basic_locators.AdPageLocators.COMPANY_NAME_LOCATOR).send_keys(campaing_name)
        self.wait_clickable(basic_locators.AdPageLocators.SAVE_CAMPAIGN_LOCATOR, timeout=15)
        self.click(basic_locators.AdPageLocators.SAVE_CAMPAIGN_LOCATOR)
        self.wait_clickable(basic_locators.AdPageLocators.SUBMIT_CAMPAIGN_LOCATOR, timeout=15)
        self.click(basic_locators.AdPageLocators.SUBMIT_CAMPAIGN_LOCATOR)

    @allure.step("Функция success_check проверяет создание кампании с таким же UUID")
    def success_check(self, campaing_name, timeout=None):
        self.wait(timeout).until(ec.element_to_be_clickable(self.locators.DISPLAYED_SITE_LOCATOR))
        SUCCESS_LOCATOR = (By.XPATH, f"//a[@title= '{campaing_name}']")
        self.wait_presence(SUCCESS_LOCATOR, timeout=15)
