import os
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser, Browser, Config
from dotenv import load_dotenv
from selenium.webdriver.remote.file_detector import LocalFileDetector

from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


# def pytest_addoption(parser):
#     parser.addoption(
#         '--browser_version',
#         default='100.0'
#     )
#
#
# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()


@allure.step('Open registration form')
@pytest.fixture(scope="session")
def open_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
        file_detector=LocalFileDetector())

    browser.config.driver = driver
    # browser.config.browser_name = "firefox"
    browser.config.hold_browser_open = True
    browser.open("https://demoqa.com/automation-practice-form")

    yield
    # browser_version = request.config.getoption('--browser_version')
    # browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    #
    # options = Options()
    #
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": browser_version,
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # options.capabilities.update(selenoid_capabilities)
    #
    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    #
    # driver = webdriver.Remote(
    #     command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
    #     options=options
    # )
    #
    # browser = Browser(Config(driver))

    # yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    # attach.add_video(browser)
    browser.quit()
