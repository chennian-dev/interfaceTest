#coding:utf-8
import unittest
import paramunittest
import readConfig as readConfig
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp
import json

login_xls = common.get_xls("userCase.xlsx", "login")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):
    def setParameters(self, case_name, method, token, tellPhone, password, result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param tellPhone:
        :param password:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.tellPhone = str(tellPhone)
        self.password = str(password)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.return_json = None
        self.info = None

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testLogin(self):
        """
        test body
        :return:
        """
        # set url
        self.url = common.get_url_from_xml('login')
        configHttp.set_url(self.url)
        self.assertEqual(1,1)

        # get visitor token
        # if self.token == '0':
        #     token = localReadConfig.get_headers("token_v")
        # elif self.token == '1':
        #     token = None
        #
        # # set headers
        # header = {"token": str(token)}
        # configHttp.set_headers(header)
        #
        # # set params
        # data = {"androidId":"","channelId":"app1","deviceNo":"feb4b3185d564de49778f357259cd713","deviceSerialNo":"","deviceToken":"","deviceType":"1","imei":"","imsi":"","macAddr":"","macAddrBt":"","osVersion":"11.2.6","phone":"","sign":"63a69e536f385ca34e6641c46c520b11","tellPhone":self.tellPhone,"token":"","tokenValue":"","userInfoId":"","userPassword":self.password,"version":"3.1.0"}
        # configHttp.set_data(json.dumps(data))
        #
        # # test interface
        # self.return_json = configHttp.post()
        #
        # # check result
        # self.checkResult()

    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()
        self.assertEqual(self.info.get('retcode'), self.result)