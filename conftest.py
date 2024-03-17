import pytest


from selenium import webdriver
from selene import browser, be, have


@pytest.fixture(autouse=True)
def config_browser_window():
    browser.open()
    browser.config.window_size = (1920, 1080)
    browser.config.start_maximized = True
    browser.open('https://google.com')
    yield # dalshe teardown
    print('Закрываем браузер')
    browser.quit()