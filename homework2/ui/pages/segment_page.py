import selenium.webdriver.support.expected_conditions as ec
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import allure

class SegmentPage(BasePage):
    locators = basic_locators.SegmentLocators()

    @allure.step("Функция change_name присваивает сегменту имя с UUID")
    def change_name(self, segment_name):
        action = ActionChains(self.driver)
        actions = self.find(basic_locators.SegmentLocators.SEGMENT_NAME_PLACEHOLDER_LOCATOR)
        action.double_click(actions).double_click(actions).send_keys(Keys.DELETE).send_keys(segment_name).perform()

    @allure.step("Функция create_segment создает сегмент")
    def create_segment(self, segment_name, timeout=None):
        self.driver.get("https://target-sandbox.my.com/segments/segments_list/new")
        self.wait_and_click(basic_locators.SegmentLocators.CHECKBOX_LOCATOR)
        self.wait_and_click(basic_locators.SegmentLocators.ADD_SEGMENT_LOCATOR)
        self.change_name(segment_name)
        self.wait_and_click(basic_locators.SegmentLocators.CREATE_SEGMENT_LOCATOR)

    @allure.step("Функция success_check проверяет создание сегмента с таким же UUID")
    def success_check(self, segment_name, timeout=None):
        self.wait(timeout).until(ec.element_to_be_clickable(self.locators.DISPLAYED_SEGMENTS_LOCATOR))
        SUCCESS_LOCATOR = (By.XPATH, f"//a[@title= '{segment_name}']")
        self.find(SUCCESS_LOCATOR, timeout=5)