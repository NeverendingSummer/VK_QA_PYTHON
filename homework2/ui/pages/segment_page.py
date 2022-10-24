import selenium.webdriver.support.expected_conditions as ec
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#        SUCCESS_LOCATOR = (By.XPATH, f"//a[@title= '{campaing_name}']")
#        self.wait_presence(SUCCESS_LOCATOR, timeout=15)

# action = ActionChains(self.driver)
# action_storage = self.find(*basic_locators.FIO_LOCATOR)
# action.double_click(action_storage).send_keys(Keys.DELETE).send_keys(f"newtestfio{now.minute}").perform()


class SegmentPage(BasePage):
    locators = basic_locators.SegmentLocators()

    def wait_and_click(self, what, timeout=None):
        self.wait_clickable(what, timeout=15)
        self.click(what)

    def change_name(self, segment_name):
        action = ActionChains(self.driver)
        actions = self.find(basic_locators.SegmentLocators.SEGMENT_NAME_PLACEHOLDER_LOCATOR)
        action.double_click(actions).double_click(actions).send_keys(Keys.DELETE).send_keys(segment_name).perform()

    def create_segment(self, segment_name, timeout=None):
        self.driver.get("https://target-sandbox.my.com/segments")
        self.wait_and_click(basic_locators.SegmentLocators.CREATE_SEGMENT_LOCATOR)
        self.wait_and_click(basic_locators.SegmentLocators.APPS_GAMES_LOCATOR)
        self.wait_and_click(basic_locators.SegmentLocators.CHECKBOX_LOCATOR)
        self.wait_and_click(basic_locators.SegmentLocators.ADD_SEGMENT_LOCATOR)
        self.change_name(segment_name)
        self.wait_and_click(basic_locators.SegmentLocators.CREATE_SEGMENT_LOCATOR)

    def success_check(self, segment_name, timeout=None):
        self.wait(timeout).until(ec.element_to_be_clickable(self.locators.DISPLAYED_SEGMENTS_LOCATOR))
        SUCCESS_LOCATOR = (By.XPATH, f"//a[@title= '{segment_name}']")
        self.wait_presence(SUCCESS_LOCATOR, timeout=5)