from selenium import webdriver
import pytest


# instead of doing the driver creation multiple times we just created a file like conftest.py and i created one
# fixture so when i call this fixture then it will return the driver for us
# the "fixture method can also return the driver

@pytest.fixture()
def setup(browser):
    print(f"----------------{browser}---------------------------------------")
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching Chrome browser........")
        return driver
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("launching Firefox browser........")
        return driver


def pytest_addoption(parser):  # this will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the Browser value to setup method
    return request.config.getoption("--browser")
