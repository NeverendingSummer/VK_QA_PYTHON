import pytest
from faker import Faker
from random_username.generate import generate_username
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from ui.pages.login_page import LoginPage
from ui.pages.registry_page import RegistryPage

fake = Faker()


@pytest.fixture
def create_fake_info_fixture():
    name = fake.name().split(' ')
    email = fake.email()
    username = generate_username(1)[0]
    password = fake.password()
    return name[0], name[1], username, email, password


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def registry_page(driver):
    return RegistryPage(driver=driver)


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


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


@pytest.fixture(scope='session')
def cookies(driver, config):
    driver.get(config['url'])
    base_page = LoginPage(driver)
    base_page.login("temeka", "testpassword")
    cookies = driver.get_cookies()
    return cookies
