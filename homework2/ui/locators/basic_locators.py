from selenium.webdriver.common.by import By

LOGOUT_LOCATOR = (By.XPATH, "//a[contains(@href,'/logout')]")
PROFILE_LOCATOR = (By.XPATH, "//div[contains(@class, 'mail')]")
STATISTICS_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-content-wrapper')]")
SUBMIT_LOCATOR = (By.XPATH, "//button[@class='button button_submit']")
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


class BasePageLocators:
    LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    USERNAME_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
    BASEPAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'mainPage-module-body')]")
    DISPLAYED_SITE_LOCATOR = (By.XPATH, "//ul[contains(@class, 'instruction-module-list')] | //div[contains(@class, 'pagination-module-pagination-')]")


class AdPageLocators:

    AD_VISIBILITY_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-objectives-container')]") #локатор, для прогрузки раздела создания
    AD_WATCH_VIDEO_LOCATOR = (By.XPATH, "//div[contains(@class,'_videoviews')]") #локатор "просмотр видео"
    ENTER_URL_LOCATOR = (By.XPATH, "//div/input[contains(@class,'input-module-input')]") #локатор ввода сссылки
    CREATE_COMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@class, '-createButtonWrap-')]") #локатор начальной страницы для запуска создания
    PREROLL_LOCATOR = (By.XPATH, "//div[contains(@id, 'patterns_preroll')]") #локатор преролда
    SEND_VIDEO_LOCATOR = (By.XPATH, "//div[contains(@class, 'roles-module-currentPatternButton')]//input[@type='file']") #локатор скрытой кнопки отправить видео
    SAVE_CAMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@data-test, 'submit_banner_button')]")  # локатор сохранения объявления
    SUBMIT_CAMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]")  # локатор конечного сохранения объявления
    SUCCESS_LOCATOR = (By.XPATH, "//div[contains(@class, 'notify-module-success')]") # локатор успешной работы
