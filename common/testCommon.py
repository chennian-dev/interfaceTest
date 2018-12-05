#coding:utf-8
import requests
import  time
from Log import MyLog as Log


class testCommon:

	def __init__(self):
		self.log = Log.get_log()
		self.logger = self.log.get_logger()
		self.host = ''
		self.timeout='30'
		self.params={}
		self.headers={}
		self.res =''

	def get(self):
		try:
			response = requests.get(url=self.host, headers=self.headers, params=self.params, timeout=float(self.timeout))
			print response.text
			return response.json()
		except:
			self.logger.error(self.res)
			return None


	def post(self):
		try:
			response = requests.post(url=self.host, headers=self.headers, params=self.params, timeout=float(self.timeout))
			print response.text
			return response.json()
		except Exception:
			self.logger.error("Time out!")
			return None

	def postJson(self):
		try:
			print self.params
			response = requests.post(url=self.host, headers=self.headers, json=self.params, timeout=float(self.timeout))
			print response.text
			return response.json()
		except:
			self.logger.error("Time out!")
			return None

	def busUser(self):
		# 1、登录获取token http://10.0.5.245:8060/v2.0/user/auser/pwdLogin
		t = testCommon()
		t.host = 'http://10.0.5.245:8060/v2.0/user/auser/pwdLogin'
		t.params ={"username":"admin","password":"123456"}
		response = t.postJson()
		tokenVal =  response.get('data').get('accessToken').get('value')

		#2、 创建商家用户
		t.host='http://10.0.5.245:8060/v2.0/user/shopusers/createAccount'
		val ="Bearer "+tokenVal
		t.headers={"Authorization":val}
		teleph = '15012341234'
		t.params={"id":"","realName":"陈宝国","sex":1,"birthday":"2018-10-31T16:00:00.000Z","mobile":teleph,"email":"15099999991@qq.com","province":1,"city":1,"district":1,"certType":"1","certNo":"429006198008150702","registerSource":"PC","certFrontPhoto":"http://img.fbh-china.com/certs/1541147741385.png","certBackPhoto":"http://img.fbh-china.com/certs/1541147747894.png"}
		response = t.postJson()
		response.get('status')
		# 3、实名认证  15678787878

	def busUserLogin(self):
		t=testCommon()
		t.host='http://10.0.5.245:8060/v2.0/user/buser/pwdLogin'
		t.params={"loginPwd":"4CfJvm60Btlokx9zwGIhWQ==","userName":"15099999997"}
		response = t.postJson()
		tokenVal =  response.get('data').get('accessToken').get('value')
		# 实名认证
		t.host='http://10.0.5.245:8060/v2.0/user/shopusers/applyBindBankCard'
		t.headers={"Authorization":"Bearer " + tokenVal}
		t.params={"identityNo":"429006198008150702","bankCard":"6228481200290314552","mobile":"15099999997","bankCardType":1,"name":"陈宝国","userID":840,"indentityType":1}
		response = t.postJson()
		response.get('status')

	def cusUser(self,phone,code):
		t=testCommon()
		t.host='http://10.0.5.245:8060/v2.0/user/cuser/register'
		t.params={"password":"4CfJvm60Btlokx9zwGIhWQ==","phone":phone,"zone":"0086","againPassword":"4CfJvm60Btlokx9zwGIhWQ==","acode":code,"type":"0"}
		response = t.postJson()

	def getRegCode(self,phone):
		t=testCommon()
		t.host='http://10.0.5.245:8060/v2.0/user/cuser/smsCode'
		t.params={"cs":1541397399763,"phone":phone,"zone":"0086","type":"0"}
		t.postJson()
		time.sleep(1)

if __name__ == '__main__':
	t = testCommon()
	phone='15012124545'
	t.getRegCode(phone)

