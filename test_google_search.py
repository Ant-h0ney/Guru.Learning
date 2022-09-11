import pytest
from selene.support.shared import browser
from selene import be, have
browser.config.hold_browser_open = False

@pytest.fixture()
def open_google():
    browser.open('https://google.com')
    yield
    browser.close()


def test_google_successfull_search(open_google):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_unsuccessfull_search(open_google):
    query = 'byldiga online kek zapros'
    browser.element('[name="q"]').should(be.blank).type(query).press_enter()
    browser.element('#res').should(have.text('ничего не найдено.'))
