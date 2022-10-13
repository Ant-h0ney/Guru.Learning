import pytest
from selene import be, have
from selene.support.shared import browser

from tests.Size_data import mobile_size, desktop_size


@pytest.fixture(params=[mobile_size, desktop_size], ids=repr)
def params(request):
    browser.config.window_width = request.param.width
    browser.config.window_height = request.param.height


# @pytest.mark.xfail('browser.config.window_width == mobile_size.width', reason='Test for desktop only')
def test_login_desktop(params):
    if browser.config.window_width == mobile_size.width:
        pytest.xfail('Test for desktop only')
    browser.open('')
    browser.element('[class*="sign-in"]').click()
    browser.element('[class*="auth-form-header"]').should(be.visible).should(have.text('Sign in to GitHub'))


# @pytest.mark.skipif('browser.config.window_width == desktop_size.width', reason='Test for mobile only')
def test_login_mobile(params):
    if browser.config.window_width == desktop_size.width:
        pytest.skip('Test for desktop only')
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('[class*="sign-in"]').click()
    browser.element('[class*="auth-form-header"]').should(be.visible).should(have.text('Sign in to GitHub'))
