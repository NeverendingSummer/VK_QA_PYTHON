import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.login_page import LoginPage
from ui.pages.registry_page import RegistryPage


def pytest_addoption(parser):
    parser.addoption("--url", default="http://172.17.0.3:8080/")
    parser.addoption('--headless', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    return {"url": url, "headless": headless}


@pytest.fixture(scope="session")
def driver(config):
    options = Options()
    url = config["url"]
    headless = config["headless"]
    if headless:
        options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager(version='107.0.5304.62').install(), options=options)
    else:
        driver = webdriver.Chrome(ChromeDriverManager(version='107.0.5304.62').install(), options=options)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def registry_page(driver):
    return RegistryPage(driver=driver)


@pytest.fixture(scope='session')
def cookies(driver, config):
    driver.get(config['url'])
    base_page = LoginPage(driver)
    base_page.login("testuser", "test123")
    cookies = driver.get_cookies()
    return cookies
