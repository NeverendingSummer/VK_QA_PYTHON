from ui.fixtures import *
import docker
import logging
import os, shutil

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
    pass


def pytest_unconfigure(config):
    print('here unconfig')


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def base_temp_dir(config):
    base_dir = './logs'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir, request.node.name)
    os.makedirs(test_dir)
    return test_dir
