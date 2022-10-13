import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def chrome():
    browser.config.browser_name = 'chrome'


@pytest.fixture(scope='function', autouse=True)
def main_page():
    browser.config.base_url = 'https://github.com/'
