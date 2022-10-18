import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.ad_page import AdPage

@pytest.fixture(scope='function')
def driver(configure):
    options = Options()
    url = configure["url"]
    headless = configure["headless"]
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager(version="105.0.5195.19").install(), options=options)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def ad_page(driver):
    return AdPage(driver=driver)