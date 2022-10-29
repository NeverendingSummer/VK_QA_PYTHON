from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    USERNAME_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
    BASEPAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'mainPage-module-body')]")
    DISPLAYED_SITE_LOCATOR = (By.XPATH,
                              "//ul[contains(@class, 'instruction-module-list')] | //div[contains(@class, "
                              "'pagination-module-pagination-')]")


class AdPageLocators(BasePageLocators):
    AD_VISIBILITY_LOCATOR = (
    By.XPATH, "//div[contains(@class, 'js-objectives-container')]")  # локатор, для прогрузки раздела создания
    AD_WATCH_VIDEO_LOCATOR = (By.XPATH, "//div[contains(@class,'_videoviews')]")  # локатор "просмотр видео"
    ENTER_URL_LOCATOR = (By.XPATH, "//div/input[contains(@class,'input-module-input')]")  # локатор ввода сссылки
    CREATE_CAMPAIGN_LOCATOR = (
    By.XPATH, "//div[contains(@class, '-createButtonWrap-')]")  # локатор начальной страницы для запуска создания
    PREROLL_LOCATOR = (By.XPATH, "//div[contains(@id, 'patterns_preroll')]")  # локатор преролда
    SEND_VIDEO_LOCATOR = (By.XPATH,
                          "//div[contains(@class, 'roles-module-currentPatternButton')]//input[@type='file']")  # локатор скрытой кнопки отправить видео
    SAVE_CAMPAIGN_LOCATOR = (
    By.XPATH, "//div[contains(@data-test, 'submit_banner_button')]")  # локатор сохранения объявления
    SUBMIT_CAMPAIGN_LOCATOR = (
    By.XPATH, "//div[contains(@class, 'js-save-button-wrap')]")  # локатор конечного сохранения объявления
    COMPANY_NAME_LOCATOR = (By.XPATH, "//div[@class='js-bottom-campaign-name-wrap']//input[@type='text']")
    CLEAR_NAME_LOCATOR = (
    By.XPATH, "//div[@class='js-bottom-campaign-name-wrap']//div[@class='input__clear js-input-clear']")


class SegmentLocators(BasePageLocators):
    CREATE_SEGMENT_LOCATOR = (By.XPATH, "//button[@class='button button_submit']")
    APPS_GAMES_LOCATOR = (By.XPATH, "//div[contains(text(), 'Приложения и игры в соцсетях')]")
    CHECKBOX_LOCATOR = (By.XPATH, "//div/input[@type='checkbox']")
    ADD_SEGMENT_LOCATOR = (By.XPATH, "//div[contains(@class, 'adding-segments-modal__btn-wrap ')]")
    SEGMENT_NAME_PLACEHOLDER_LOCATOR = (By.XPATH, "//div[@class='input input_create-segment-form']//input[@type='text']")
    DISPLAYED_SEGMENTS_LOCATOR = (By.XPATH, "//div/div/div[contains(@class, 'js-viewport-wrapper')]")


class GroupsLocators(BasePageLocators):
    GROUPS_INPUT_PLACEHOLDER_LOCATOR = (By.XPATH, "//input[contains(@class, 'input-module-input-')]")
    SHOW_LOCATOR = (By.XPATH, "//div[@data-test='show']")
    OPTIONS_LOCATOR = (By.XPATH, "//li/span[contains(@class, 'optionsList-module-text-')]")
    SUBMIT_GROUP_LOCATOR = (By.XPATH, "//div[contains(@class, 'bubbleComponent-module-submit-')]")
    CHECK_CREATION_LOCATOR = (By.XPATH, "//a[@href='https://vk.com/vkedu']")
    DELETION_LOCATOR = (By.XPATH, "//span[@class='icon-cross']")
    CONFIRM_DELETION_LOCATOR = (By.XPATH, "//button[@class='button button_confirm-remove button_general']")