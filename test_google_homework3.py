import pytest
from selene import browser, be, have


@pytest.fixture()
def open_browser():
    browser.driver.set_window_size(1920, 1080)
    browser.open('https://google.com')


def test_google(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('diudihfdsjfgfdg').press_enter()
    browser.element('[id="botstuff"]').should(
        have.text('diudihfdsjfgfdg ничего не найдено.'))
