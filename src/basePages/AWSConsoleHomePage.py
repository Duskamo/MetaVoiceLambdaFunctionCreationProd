
from src.basePages.AWSLambdaFunctionsPage import *
from src.utils.BasePage import *

class AWSConsoleHomePage(BasePage):
    def __init__(self):
        super(AWSConsoleHomePage, self).__init__()

    def gotoAWSLambdaFunctionsPage(self):
        self.searchInputBox = self.driver.find_element_by_id("search-box-input")
        self.searchInputBox.send_keys("lambda")

        self.firstSearchBoxItem = self.driver.find_element_by_id("search-box-item-0")
        self.firstSearchBoxItem.click()

        awsLambdaFunctionsPage = AWSLambdaFunctionsPage()
        awsLambdaFunctionsPage.driver = self.driver

        return awsLambdaFunctionsPage