import pytest


@pytest.fixture(scope="session")
def browser_name():
    print("Я выполняюсь один раз")
    return "Chrome"
