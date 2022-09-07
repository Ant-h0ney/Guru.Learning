from selene.support.shared import browser
from selene import be, have
import pytest
browser.config.hold_browser_open = True

@pytest.fixture(scope="function", autouse=True)
def start_browser():
    browser.config.window_height = 1024
    browser.config.window_width = 1920
    browser.open('https://google.com')


def test_google_successfull_search():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

query='byldiga online kek zapros'
def test_google_unsuccessfull_search():
    browser.element('[name="q"]').should(be.blank).type(query).press_enter()
    browser.element('#res').should(have.text('ничего не найдено.'))