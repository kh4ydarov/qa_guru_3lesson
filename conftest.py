import pytest
from selene import browser, be, have


@pytest.fixture(autouse=True)
def config_browser_window():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    yield # dalshe teardown
    browser.quit()