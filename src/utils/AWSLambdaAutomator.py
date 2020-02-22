import json
from selenium import webdriver

from src.basePages.AWSConsoleLoginPage import *
from src.utils.Config import *

class AWSLambdaAutomator:
    def __init__(self,jsonDict):
        self.json = jsonDict

    def automateTasks(self):
	isAutomationComplete = False

	# While end-to-end automation process did not finish	
	while (isAutomationComplete == False):
		# Open browser, navigate and login to AWS Console
        	awsConsoleLoginPage = AWSConsoleLoginPage()
        	awsConsoleLoginPage.waitPageLoad()
	        awsConsoleLoginPage.enterCredentials(email, password)

		# Navigate AWS Lambda creation page
        	awsConsoleHomePage = awsConsoleLoginPage.gotoAWSConsoleHomePage()
	        awsConsoleHomePage.waitPageLoad()

	        awsLambdaFunctionsPage = awsConsoleHomePage.gotoAWSLambdaFunctionsPage()
        	awsLambdaFunctionsPage.waitPageLoad()

	        functionName = str(self.json['firstName']) + "_" + str(self.json["lastName"]) + "_" + str(self.json["skillName"])
	
		# Create AWS Lambda function
        	awsLambdaCreatePage = awsLambdaFunctionsPage.gotoAWSLambdaCreatePage()
	        awsLambdaCreatePage.waitPageLoad()
        	awsLambdaCreatePage.inputFunctionName(functionName)
	        awsLambdaCreatePage.selectPythonRuntime()
       		awsLambdaCreatePage.selectBasicExecutionRole()
	
		# Configure lambda function trigger, input python code, and retrieve function arn 
        	awsLambdaFunctionPage = awsLambdaCreatePage.gotoAWSLambdaFunctionPage()
        	awsLambdaFunctionPage.waitPageLoad()
        	awsLambdaFunctionPage.addAndEnableTrigger()
        	awsLambdaFunctionPage.inputPythonCode(self.json['code'])
        	awsLambdaFunctionPage.saveConfiguration()
        	arn = awsLambdaFunctionPage.retrieveARN()
        	
		# Function ending phase
		awsLambdaFunctionPage.logout()
		isAutomationComplete = True

        	print arn
        	return arn
	return "Service 3 Exception"
