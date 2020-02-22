
from src.utils.BasePage import *
from src.basePages.AWSLambdaCreatePage import *

class AWSLambdaFunctionsPage(BasePage):
    def __init__(self):
        super(AWSLambdaFunctionsPage, self).__init__()

    def gotoAWSLambdaCreatePage(self):
        self.createFunctionButton = self.driver.find_element_by_xpath("//*[contains(text(),'Create function')]")
        self.createFunctionButton.click()

        awsLambdaCreatePage = AWSLambdaCreatePage()
        awsLambdaCreatePage.driver = self.driver

        return awsLambdaCreatePage
