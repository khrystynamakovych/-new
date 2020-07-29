from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebBrowserInstance(self):
        baseUrl = "https://learn.letskodeit.com/"
        if self.browser == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(6)
        driver.get(baseUrl)
        return driver