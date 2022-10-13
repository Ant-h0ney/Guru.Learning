import pytest
from selene.support.conditions import have, be
from selene.support.shared import browser

from tests.Size_data import desktop_size, mobile_size


@pytest.fixture(params=[desktop_size], ids=repr)
def params(request):
    browser.config.window_width = request.param.width
    browser.config.window_height = request.param.height


def test_login_desktop(params):
    browser.open('')
    browser.element('[class*="sign-in"]').click()
    browser.element('[class*="auth-form-header"]').should(be.visible).should(have.text('Sign in to GitHub'))


mobile = (pytest.mark.parametrize('params', [mobile_size],
                                  indirect=True, ids=repr))


@mobile
def test_login_mobile(params):
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('[class*="sign-in"]').click()
    browser.element('[class*="auth-form-header"]').should(be.visible).should(have.text('Sign in to GitHub'))
