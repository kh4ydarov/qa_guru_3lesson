import pytest
from selenium import webdriver
from selene import browser, be, have


@pytest.fixture(autouse=True)
def config_browser_window():
    browser.open()
    yield # dalshe teardown
    print('Закрываем браузер')
    browser.quit()