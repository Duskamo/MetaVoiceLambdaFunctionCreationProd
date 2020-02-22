from flask import Flask, session, redirect, url_for, escape, request, render_template
import json
import requests
import os
from src.utils.AWSLambdaCreator import *
from src.Helpers.FileHelper import *

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>welcome</h1>'

#simple post method that takes in a JSON object from service 2 and creates an AWS lambda function using selenium
@app.route('/post', methods = ['POST'])
def get_post_json_data():
	# Load the json
	jsonRaw = request.get_json(silent=True)
	jsonDict = json.loads(jsonRaw)

	print(jsonDict)

	# Save python code to internal zip file
	fileHelper = FileHelper()
	fileHelper.createFileWithContents(jsonDict["code"])
	fileHelper.zipFile(fileHelper.PYTHON_FILE_LOCATION)

	# Create lambda function using passed-in json object and python zip file
	awsLambdaFunctionCreator = AWSLambdaCreator(jsonDict, fileHelper.PYTHON_ZIP_FILE_LOCATION)
	awsLambdaFunctionCreator.createAWSLambdaFunction()
	arn = awsLambdaFunctionCreator.getLambdaARN()

	# Append arn to JSON object
	jsonDict['arn'] = arn

	# Send POST with JSON object in body to service 4
	url = 'http://localhost:5003/post'
	requests.post(url, json=json.dumps(jsonDict))

	return jsonDict

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5001.
	port = int(os.environ.get('PORT', 5002))
	app.run(host='0.0.0.0', port=port)
