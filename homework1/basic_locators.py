from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
USERNAME_LOCATOR = (By.NAME, 'email')
PASSWORD_LOCATOR = (By.NAME, 'password')

LOGOUT_LOCATOR = (By.XPATH, "//a[contains(@href,'/logout')]")
BASEPAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'mainPage-module-body')]")
PROFILE_LOCATOR = (By.XPATH, "//div[contains(@class, 'mail')]")
DISPLAYED_SITE_LOCATOR = (By.XPATH, "//ul[contains(@class, 'instruction-module-list')]")
ENTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
STATISTICS_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-content-wrapper')]")
SUBMIT_LOCATOR = (By.XPATH, "//button[@class='button button_submit']")

#KEY_HEADERS = ['segments', 'billing', 'statistics', 'profile', 'tools']
NAVIGATION_LOCATOR = [(By.XPATH, f"//a[contains(@class, 'segments')]"),
                      (By.XPATH, f"//a[contains(@class, 'billing')]"),
                      (By.XPATH, f"//a[contains(@class, 'statistics')]"),
                      (By.XPATH, f"//a[contains(@class, 'profile')]"),
                      (By.XPATH, f"//a[contains(@class, 'tools')]"),
                      ]

FIO_LOCATOR = (By.XPATH, "//div[contains(@class, 'field-name')]")
INN_LOCATOR = (By.XPATH, "//div[contains(@class, 'ord-inn')]")
PHONE_LOCATOR = (By.XPATH, "//div[contains(@class, 'field-phone')]")

PROFILE_CONTACTS_LOCATOR = (By.XPATH, "//div[contains(@class, 'head-module-leftWrap')]")
