import subprocess
import os
import json

class AWSLambdaCreator:
	def __init__(self,jsonDict, pythonZipFileLocation):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		rel_bash_path = "../files/lambda_creator"
		rel_output_path = "../files/function_contents.json"

		self.LAMBDA_CREATOR_BATCH = os.path.join(script_dir, rel_bash_path)
		self.LAMBDA_OUTPUT_CONTENTS = os.path.join(script_dir, rel_output_path)
		self.jsonDict = jsonDict
		self.pythonZipFileLocation = pythonZipFileLocation

	def createAWSLambdaFunction(self):
		functionName = self.jsonDict["skillName"] + "_" + self.jsonDict["firstName"] + "_" + self.jsonDict["lastName"]
		cmd = "sudo " + self.LAMBDA_CREATOR_BATCH + " fileb://" + self.pythonZipFileLocation + " " + functionName

		subprocess.check_output(cmd,shell=True)

	def getLambdaARN(self):
		d = {}
		with open(self.LAMBDA_OUTPUT_CONTENTS) as f:
			d = json.load(f)

		return d['Configuration']['FunctionArn']
