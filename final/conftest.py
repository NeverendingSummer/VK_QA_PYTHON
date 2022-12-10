from ui.fixtures import *
import docker

client = docker.from_env()
def pytest_addoption(parser):
    parser.addoption("--url", default="http://172.18.0.4:8080/")
    parser.addoption('--headless', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    return {"url": url, "headless": headless}


def pytest_configure(config):
    print('here config')


def pytest_unconfigure(config):
    print('here unconfig')
