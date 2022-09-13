# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
def print_func_name_and_argues(func, *args, **kwargs):
    print(f'Function name: {func.__name__.capitalize().replace("_", " ")}')
    if len(kwargs) == 0 and len(args) == 0:
        print('Argues does not exist')
    if len(kwargs) != 0 or len(args) != 0:
        print('The arguments:', end=' ')
    if len(args) != 0:
        print(f'{args}')
    if len(kwargs) != 0:
        print(f'{kwargs}')
    print()


def open_browser(browser_name):
    print_func_name_and_argues(open_browser, browser_name=browser_name)
    pass


def go_to_companyname_homepage(page_url):
    print_func_name_and_argues(go_to_companyname_homepage, page_url=page_url)
    pass


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name_and_argues(find_registration_button_on_login_page, page_url=page_url, button_text=button_text)
    pass


def empty():
    print_func_name_and_argues(empty)
    pass

open_browser('Edge')
go_to_companyname_homepage('google.com')
find_registration_button_on_login_page('google.com/login','sign up')
empty()