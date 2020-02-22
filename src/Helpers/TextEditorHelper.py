from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class TextEditorHelper:
    def __init__(self,driver):
        self.driver = driver

        self.environmentSelectorDropdownItem = self.driver.find_element_by_xpath(".//span[contains(text(),'Python 2.7')]")
        self.actions = ActionChains(self.driver)

    def scrollIntoView(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_id("codeSection"))

    def moveToTextEditor(self):
        self.actions.move_to_element_with_offset(self.environmentSelectorDropdownItem, 0, 200)
        self.actions.click()
        self.actions.perform()

    def deleteCode(self):
        self.actions.key_down(Keys.LEFT_CONTROL).send_keys('a').key_up(Keys.LEFT_CONTROL).perform()
        self.actions.send_keys(Keys.DELETE).perform()

    def addCode(self,code):
        self.actions.send_keys(code)
        self.actions.perform()