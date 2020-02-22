import zipfile
import os

class FileHelper:
	def __init__(self):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		rel_code_path = "../files/code.py"
		rel_zip_path = "../files/zippedcode.zip"

		self.PYTHON_FILE_LOCATION = os.path.join(script_dir, rel_code_path)
		self.PYTHON_ZIP_FILE_LOCATION = os.path.join(script_dir, rel_zip_path)

	def createFileWithContents(self,contents):
		f = open(self.PYTHON_FILE_LOCATION, "w+")
		f.write(contents)
		f.close()

	def zipFile(self,fileLocation):
		print('creating archive')
		zf = zipfile.ZipFile(self.PYTHON_ZIP_FILE_LOCATION, mode='w')
		try:
		    print("Yo", fileLocation)
		    zf.write(fileLocation,"code.py")
		finally:
		    print 'closing'
		    zf.close()







