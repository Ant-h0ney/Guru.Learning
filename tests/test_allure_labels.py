import allure
from allure_commons.types import Severity
import test_allure_steps


def test_dynamic_labels():
    allure.dynamic.tag('bd')
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.suite('bd_issue')
    allure.dynamic.label('owner', 'Ant-h0ney')
    allure.dynamic.feature('Creating issues')
    allure.dynamic.story('Issue may be created by anyone')
    allure.dynamic.link('https://github.com', name='Git')
    test_allure_steps.open_git()
    test_allure_steps.search_repo('Ant-h0ney/Guru.Learning')
    test_allure_steps.go_to_repo('Ant-h0ney/Guru.Learning')
    test_allure_steps.open_issues_tab()
    test_allure_steps.check_issue_head('Issue for practice Allure')


@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Ant-h0ney')
@allure.feature('Issue visible for anyone')
@allure.story('Issue may see anyone')
@allure.link('https://github.com', name='Git')
def test_decorator_labels():
    test_allure_steps.open_git()
    test_allure_steps.search_repo('Ant-h0ney/Guru.Learning')
    test_allure_steps.go_to_repo('Ant-h0ney/Guru.Learning')
    test_allure_steps.open_issues_tab()
    test_allure_steps.check_issue_head('Issue for practice Allure')
