from ui.locators import basic_locators
from ui.pages.base_page import BasePage
import allure

class GroupsPage(BasePage):
    locators = basic_locators.GroupsLocators()

    @allure.step("Функция creating_groups создаёт сегмент с испочником данных VK образовние с типом Группы OK и VK")
    def creating_groups(self):
        self.driver.get("https://target-sandbox.my.com/segments/groups_list")
        self.find(basic_locators.GroupsLocators.GROUPS_INPUT_PLACEHOLDER_LOCATOR).send_keys("https://vk.com/vkedu")
        self.wait_and_click(basic_locators.GroupsLocators.SHOW_LOCATOR)
        self.wait_and_click(basic_locators.GroupsLocators.OPTIONS_LOCATOR)
        self.wait_and_click(basic_locators.GroupsLocators.SUBMIT_GROUP_LOCATOR)
        self.wait_and_click(basic_locators.GroupsLocators.CHECK_CREATION_LOCATOR)
        self.wait_and_click(basic_locators.GroupsLocators.DELETION_LOCATOR)
        self.wait_and_click(basic_locators.GroupsLocators.CONFIRM_DELETION_LOCATOR)
