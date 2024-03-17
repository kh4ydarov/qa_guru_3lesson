import pytest


from selenium import webdriver
from selene import browser, be, have


def test_google():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative():
    browser.element('[name="q"]').should(be.blank).type('diudihfdsjfgfdg').press_enter()
    browser.element('[id="botstuff"]').should(
        have.text('diudihfdsjfgfdg ничего не найдено.'))