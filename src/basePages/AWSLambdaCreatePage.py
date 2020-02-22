
from src.utils.BasePage import *
from src.basePages.AWSLambdaFunctionPage import *

class AWSLambdaCreatePage(BasePage):
    def __init__(self):
        super(AWSLambdaCreatePage,self).__init__()

    def inputFunctionName(self, functionName):
        self.functionNameTextBox = self.driver.find_element_by_id("awsui-input-0")
        self.functionNameTextBox.send_keys(functionName)

        self.waitPageLoad()

    def selectPythonRuntime(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_xpath("//span[@data-reactroot]/awsui-form-field//*[@class='awsui-select-trigger-icon']"))

        self.pythonRuntimeDropdown = self.driver.find_element_by_xpath("//span[@data-reactroot]/awsui-form-field//*[@class='awsui-select-trigger-icon']")

        self.pythonRuntimeDropdown.click()

        self.pythonRuntimeDropdownItem = self.driver.find_element_by_xpath("//*[contains(text(),'Python 2.7')]")
        self.pythonRuntimeDropdownItem.click()

    def selectBasicExecutionRole(self):
        self.existingRoleDropdown = self.driver.find_element_by_xpath(".//*[@id='role-selector']/awsui-form-field[2]//*[@class='awsui-select-keyboard-area']")
        self.existingRoleDropdown.click()

        self.existingRoleDropdownItem = self.driver.find_element_by_xpath("//*[contains(text(),'lambda_basic_execution')]")
        self.existingRoleDropdownItem.click()

    def gotoAWSLambdaFunctionPage(self):
        self.createFunctionButton = self.driver.find_element_by_xpath("//*[@class='awsui-form-actions']//*[contains(text(),'Create function')]")
        self.createFunctionButton.click()

        awsLambdaFunctionPage = AWSLambdaFunctionPage()
        awsLambdaFunctionPage.driver = self.driver

        return awsLambdaFunctionPage
