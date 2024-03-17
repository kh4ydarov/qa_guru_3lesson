import pytest


#фикстура
@pytest.fixture
def browser(scope="session"):
    print('Brauzer')

    yield

    print('Закрываем браузер !')  #Teardown после yield
#фикстура
@pytest.fixture
def login_page(browser):
    print("Login Page")


@pytest.fixture
def user():
    print('Юзер')
    return "username", "password"

def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"

