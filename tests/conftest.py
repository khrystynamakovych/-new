import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")


#this fixture will be applied to a whole module
@pytest.fixture(scope='class')
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebBrowserInstance()
    lp = LoginPage(driver)
    lp.login("test@mail.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption('--osType', help="Type of OS")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
