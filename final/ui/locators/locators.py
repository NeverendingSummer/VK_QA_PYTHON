from selenium.webdriver.common.by import By


class BasePageLocators:
    login_locator = (By.ID, 'username')
    password_locator = (By.ID, 'password')
    submit_locator = (By.ID, 'submit')
    entered_page_locator = (By.ID, 'content')


class RegistryPageLocators:
    registry_init_locator = (By.XPATH, "//a[@href='/reg]")
    name_locator = (By.ID, 'user_name')
    surname_locator = (By.ID, 'user_surname')
    middlename_locator = (By.ID, 'user_middle_name')
    username_locator = (By.ID, 'username')
    email_locator = (By.ID, 'email')
    password_locator = (By.ID, 'password')
    repeat_password_locator = (By.ID, 'confirm')
    checkbox_locator = (By.ID, 'term')
    submit_locator = (By.ID, 'submit')
    flash_locator = (By.ID, 'flash')


class MainPageLocators:
    logout_locator = (By.ID, 'logout')
    logged_as_user_locator = (By.XPATH, '//*[@id="login-name"]/ul/li[1]')
