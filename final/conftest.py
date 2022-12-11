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
    base_logs_dir = './logs'
    base_info_dir = './info'
    if os.path.exists(base_logs_dir):
        shutil.rmtree(base_logs_dir)
    if os.path.exists(base_info_dir):
        shutil.rmtree(base_info_dir)
    os.mkdir('./logs')
    os.mkdir('./info')


def pytest_unconfigure(config):
    print('here unconfig')
