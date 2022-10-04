from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.CSS_SELECTOR, ".responseHead-module-button-2yl51i")
USERNAME_LOCATOR = (By.NAME, 'email')
PASSWORD_LOCATOR = (By.NAME, 'password')

LOGOUT_LOCATOR = (By.XPATH, "//a[contains(text(),'Выйти')]")
BASEPAGE_LOCATOR = (By.XPATH, "//div[@class='responseHead-module-content-vnHOWS']")
PROFILE_LOCATOR = (By.XPATH, "//div[contains(@class, 'mail')]")
DISPLAYED_SITE_LOCATOR = (By.CSS_SELECTOR, ".instruction-module-list-yBXqcw")
ENTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
STATISTICS_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-content-wrapper')]")
SUBMIT_LOCATOR = (By.XPATH, "//button[@class='button button_submit']")

KEY_HEADERS = ['segments', 'billing', 'statistics', 'profile', 'tools']
NAVIGATION_LOCATOR = [(By.XPATH, f"//a[contains(@class, '{KEY_HEADERS[0]}')]"),
               (By.XPATH, f"//a[contains(@class, '{KEY_HEADERS[1]}')]"),
               (By.XPATH, f"//a[contains(@class, '{KEY_HEADERS[2]}')]"),
               (By.XPATH, f"//a[contains(@class, '{KEY_HEADERS[3]}')]"),
               (By.XPATH, f"//a[contains(@class, '{KEY_HEADERS[4]}')]"),
               ]
URL_LOCATOR = [(By.XPATH, f"//div[contains(@class, 'page_{KEY_HEADERS[0]}')]"),
               (By.XPATH, f"//body[contains(@class, 'page_{KEY_HEADERS[1]}')]"),
               (By.XPATH, f"//div[contains(@class, 'page_{KEY_HEADERS[2]}')]"),
               (By.XPATH, f"//div[contains(@class, 'page_{KEY_HEADERS[3]}')]"),
               (By.XPATH, f"//div[contains(@class, 'page_{KEY_HEADERS[4]}')]"),
               ]

FIO_LOCATOR = (By.XPATH, "//div[contains(@class, 'field-name')]")
INN_LOCATOR = (By.XPATH, "//div[contains(@class, 'ord-inn')]")
PHONE_LOCATOR = (By.XPATH, "//div[contains(@class, 'field-phone')]")

PROFILE_CONTACTS_LOCATOR = (By.XPATH, "//div[@class='head-module-leftWrap-1wJKQT']")
