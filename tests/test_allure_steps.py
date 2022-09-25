import allure
from selene import by, be
from selene.support.shared import browser


def test_with_allure():
    with allure.step('Opening main page'):
        browser.open('https://github.com')
    with allure.step('Search repository'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('Ant-h0ney/Guru.Learning')
        browser.element('.header-search-input').submit()
    with allure.step('Follow inside repo'):
        browser.element(by.link_text('Ant-h0ney/Guru.Learning')).click()
    with allure.step('Open tab Issues'):
        browser.element('#issues-tab').click()
    with allure.step('Check issue head'):
        browser.element(by.partial_text('Issue for practice Allure')).should(be.visible)


def test_with_step_decorators():
    open_git()
    search_repo('Ant-h0ney/Guru.Learning')
    go_to_repo('Ant-h0ney/Guru.Learning')
    open_issues_tab()
    check_issue_head('Issue for practice Allure')


@allure.step('Opening main page')
def open_git():
    browser.open('https://github.com')


@allure.step('Search repository {repo}')
def search_repo(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Follow inside repo {repo}')
def go_to_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Open tab Issues')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Check issue head {head}')
def check_issue_head(head):
    browser.element(by.partial_text(head)).should(be.visible)
