import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.ad_page import AdPage
from ui.pages.segment_page import SegmentPage
from ui.pages.groups_page import GroupsPage
import os, sys, shutil


def pytest_configure(config):
    base_dir = './info'
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@pytest.fixture(scope="session")
def driver(config):
    options = Options()
    url = config["url"]
    headless = config["headless"]
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
#version="105.0.5195.19" - хардкод версии ломает код

@pytest.fixture(scope='session')
def cookies(driver, config, api_client):
    api_client.login()
    all_cookies = api_client.session.cookies
    buffer = []
    for cookies in all_cookies:
        buffer.append({
            'name': cookies.name,
            'value': cookies.value
        })
    return buffer

@pytest.fixture()
def file_path(repo_root):
    return os.path.join(repo_root, 'files', 'ad.mp4')


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def ad_page(driver):
    return AdPage(driver=driver)


@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)


@pytest.fixture
def groups_page(driver):
    return GroupsPage(driver=driver)

