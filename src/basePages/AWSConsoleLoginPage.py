
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display

from src.utils.BasePage import *
from src.basePages.AWSConsoleHomePage import *

class AWSConsoleLoginPage(BasePage):
    def __init__(self):
        super(AWSConsoleLoginPage, self).__init__()
        self.url = "https://console.aws.amazon.com/console/home"
        self.openPage()

    def enterCredentials(self, email, password):
        self.emailTextBox = self.driver.find_element_by_id("resolving_input")
        self.emailTextBox.send_keys(email)

        self.emailNextButton = self.driver.find_element_by_id("next_button")
        self.emailNextButton.click()

        self.waitPageLoad()

        self.passwordTextBox = self.driver.find_element_by_id("password")
        self.passwordTextBox.click()
        self.passwordTextBox.send_keys(password)

    def gotoAWSConsoleHomePage(self):
        self.signInButton = self.driver.find_element_by_id("signin_button")
        self.signInButton.click()

        awsConsoleHomePage = AWSConsoleHomePage()
        awsConsoleHomePage.driver = self.driver

        return awsConsoleHomePage

    # Helper Methods
    def openPage(self):
        firefoxOptions = Options()
        firefoxOptions.add_argument("--headless")
        self.driver = webdriver.Firefox(options=firefoxOptions,executable_path='/usr/local/bin/geckodriver')
        self.driver.maximize_window()
        self.driver.get(self.url)
