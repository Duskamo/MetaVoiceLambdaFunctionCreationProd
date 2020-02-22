
from src.utils.AWSLambdaAutomator import *
from test.TestData import *
	
awsLambdaAutomator = AWSLambdaAutomator(jsonDict)
awsLambdaAutomator.automateTasks()
