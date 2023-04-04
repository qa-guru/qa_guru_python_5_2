import pytest


@pytest.fixture(scope="function")
def user(browser_name):
    print("Получаем User ID")
    yield 123
    print("Теперь удаляем пользователя")


def test_addition(browser_name, user):
    assert browser_name == "Chrome"
    assert user == 123
    a = 1 + 2
    assert a == 3


def test_second(browser_name, user):
    pass
