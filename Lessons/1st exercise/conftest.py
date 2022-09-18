import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def start_browser():
    browser.config.window_height = 800
    browser.config.window_width = 1200
    yield
