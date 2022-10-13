import pytest
from selene import be, have
from selene.support.shared import browser


@pytest.fixture(scope='function')
def desktop_size():
    browser.config.window_width = 1200
    browser.config.window_height = 1000


@pytest.fixture(scope='function')
def mobile_size():
    browser.config.window_width = 600
    browser.config.window_height = 800


desktop = pytest.mark.usefixtures('desktop_size')
mobile = pytest.mark.usefixtures('mobile_size')


@desktop
def test_login_desktop():
    browser.open('')
    browser.element('[class*="sign-in"]').click()
    browser.element('[class*="auth-form-header"]').should(be.visible).should(have.text('Sign in to GitHub'))


@mobile
def test_login_mobile():
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('[class*="sign-in"]').click()
    browser.element('[class*="auth-form-header"]').should(be.visible).should(have.text('Sign in to GitHub'))
