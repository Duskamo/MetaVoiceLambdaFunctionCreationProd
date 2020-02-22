
from src.utils.BasePage import *
from src.Helpers.TextEditorHelper import *

class AWSLambdaFunctionPage(BasePage):
    def __init__(self):
        super(AWSLambdaFunctionPage,self).__init__()

    def addAndEnableTrigger(self):
        self.skillTriggerItem = self.driver.find_element_by_xpath("//*[contains(text(),'Alexa Skills Kit')]")
        self.skillTriggerItem.click()

        self.waitPageLoad()

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_xpath(".//span[contains(text(),'Disable')]"))
        self.skillIdDisableRadioButton = self.driver.find_element_by_xpath(".//span[contains(text(),'Disable')]")
        self.skillIdDisableRadioButton.click()

        self.addSkillButton = self.driver.find_element_by_xpath(".//div[@class='awsui-modal-footer']/div/awsui-button[2]/button")
        self.addSkillButton.click()

        self.waitPageLoad()

        self.saveConfiguration()


    def inputPythonCode(self,jsonPythonCode):
        # Click Alexa Skill to bring up text editor pane
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_xpath(".//*[@id='qualifiers']"))
        self.waitPageLoad()

        self.alexaSkillCardInput = self.driver.find_element_by_xpath(".//*[@class='awsui-grid']/div[1]/div[2]/div/div")

        self.waitPageLoad()
        self.alexaSkillCardInput.click()

        # Replace code in text editor with created python code
        textEditorInterface = TextEditorHelper(self.driver)
        textEditorInterface.scrollIntoView()
        textEditorInterface.moveToTextEditor()
        textEditorInterface.deleteCode()
        textEditorInterface.addCode(jsonPythonCode)

        self.waitPageLoad()

    def saveConfiguration(self):
        self.saveConfigurationButton = self.driver.find_element_by_xpath(".//awsui-button[@class='save']/button")
        self.saveConfigurationButton.click()

        self.waitPageLoad()

    def retrieveARN(self):
        self.arnLabel = self.driver.find_element_by_xpath(".//*[@id='header']/span/div/div")
        return self.arnLabel.text[6:]

    def logout(self):
        self.driver.quit()
