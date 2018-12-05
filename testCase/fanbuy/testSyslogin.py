#coding:utf-8
import unittest
import paramunittest
from common import Log as Log
from common import configHttp
from common import common

localConfigHttp = configHttp.ConfigHttp()
login_xls = common.get_xls("fanbuyCase.xlsx", "login")

@paramunittest.parametrized(*login_xls)
class Syslogin(unittest.TestCase):

	def setParameters(self, case_name, method, username, password, result, code, msg):
		self.case_name = str(case_name)
		self.method = str(method)
		self.username = str(username)
		self.password = str(password)
		self.result = str(result)
		self.code = int(code)
		self.msg = str(msg)
		self.response = None
		self.info = None

	def setUp(self):
		 self.log = Log.MyLog.get_log()
		 self.logger = self.log.get_logger()

	def testsyslogin(self):
		self.url ="http://10.0.5.245:8060/v2.0/user/auser/pwdLogin"
		localConfigHttp.set_url(self.url)
		hdata = {"Content-Type":"application/json","charset":"UTF-8"}
		localConfigHttp.set_headers(hdata)
		data = {"username":self.username,"password":self.password}
		localConfigHttp.set_data(data)
		self.response = localConfigHttp.postWithJson()
		self.checkResult()

	def checkResult(self):
		common.show_return_msg(self.response)
		self.info = self.response.json()
		self.assertEqual(self.info['code'],self.code)
		if self.info['code'] == self.code:
			self.assertEqual(self.info['msg'],self.msg)

