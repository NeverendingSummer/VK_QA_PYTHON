from ui.pages.login_page import LoginPage
from ui.locators import locators


class RegistryPage(LoginPage):
    def insert_values(self, name, surname, username, email, password, middlename='none'):
        self.driver.get('http://172.18.0.4:8080/reg')
        self.wait_clickable(locators.RegistryPageLocators.name_locator).send_keys(name)
        self.wait_clickable(locators.RegistryPageLocators.surname_locator).send_keys(surname)
        self.wait_clickable(locators.RegistryPageLocators.middlename_locator).send_keys(middlename)
        self.wait_clickable(locators.RegistryPageLocators.username_locator).send_keys(username)
        self.wait_clickable(locators.RegistryPageLocators.email_locator).send_keys(email)
        self.wait_clickable(locators.RegistryPageLocators.password_locator).send_keys(password)
        self.wait_clickable(locators.RegistryPageLocators.repeat_password_locator).send_keys(password)
        self.wait_clickable(locators.RegistryPageLocators.checkbox_locator).click()
        self.wait_clickable(locators.RegistryPageLocators.submit_locator).click()
        self.driver.delete_cookie('session')

    def check_registration(self):
        return self.driver.find_element(*locators.MainPageLocators.logged_as_user_locator).text.split(' ')[2]

    def get_response(self):
        print('here in func')
        print(self.driver.find_element(*locators.RegistryPageLocators.flash_locator).text)
        return self.driver.find_element(*locators.RegistryPageLocators.flash_locator).text
