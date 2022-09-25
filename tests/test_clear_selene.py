from selene import by, be
from selene.support.shared import browser


def test_just_selene():
    browser.open('https://github.com')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('Ant-h0ney/Guru.Learning')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('Ant-h0ney/Guru.Learning')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('Issue for practice Allure')).should(be.visible)


