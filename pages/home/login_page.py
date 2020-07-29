#from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage

class LoginPage(BasePage):
    log = cl.customLogger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        time.sleep(3)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@class='gravatar']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='alert alert-danger']", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")