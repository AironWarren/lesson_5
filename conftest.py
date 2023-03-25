import pytest
from selene import browser, have, be


@pytest.fixture(scope="session")
def open_browser():
    browser.config.browser_name = "firefox"
    browser.config.hold_browser_open = True
    browser.open("https://demoqa.com/automation-practice-form")

    yield

    browser.quit()
