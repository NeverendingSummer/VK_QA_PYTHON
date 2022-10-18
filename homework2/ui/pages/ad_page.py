from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import selenium.common.exceptions
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class AdPage(BasePage):
    locators = basic_locators.AdPageLocators()

