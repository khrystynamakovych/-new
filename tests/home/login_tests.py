from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

''' To run the tests: from the project in Terminal
py.test -s -v tests/home/login_tests.py --browser chrome'''


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSeTup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        #self.driver.get(self.baseUrl)
        self.lp.login(password="abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("testValidLogin", result2, "Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("wahrscheinlich@gmail.com", "kklabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

