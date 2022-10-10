from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--url", default="https://target-sandbox.my.com/")
    parser.addoption('--headless', action='store_true')



@pytest.fixture()
def configure(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    return {"url": url, "headless": headless}


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
