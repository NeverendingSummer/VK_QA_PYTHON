from selenium.webdriver.common.by import By


class BasePageLocators:
    login_locator = (By.ID, 'username')
    password_locator = (By.ID, 'password')
    submit_locator = (By.ID, 'submit')
    entered_page_locator = (By.ID, 'content')


class RegistryPageLocators:
    pass


class MainPageLocators:
    pass
