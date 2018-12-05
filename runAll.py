#coding:utf-8
import os
import unittest
from common.Log import MyLog as Log
import readConfig as readConfig
from common.configEmail import MyEmail
import HTMLTestRunner
localReadConfig = readConfig.ReadConfig()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
接口测试框架编写流程
    1、添加配置文件及读取配置文件相关公共类
    2、添加日志插件，记录程序异常信息
    3、集成单元测试组建
    4、集成测试报告输出组建
    5、编写公共类，对数据库操作、mongdb、redis、excel处理等
    6、编写测试用例，组装测试集，集成报告，批量执行
"""
class AllTest:
    def __init__(self):
        global log, logger, resultPath, on_off
        log = Log.get_log()
        logger = log.get_logger()
        resultPath = log.get_report_path()
        on_off = localReadConfig.get_email("on_off")
        self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        self.caseFile = os.path.join(readConfig.proDir, "testCase")
        self.caseList = []
        self.email = MyEmail.get_email()

    def set_case_list(self):
        """
        set case list
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            print(case_name+".py")
            #  defaultTestLoader()类，通过该类下面的discover()方法可自动更具测试目录start_dir匹配查找测试用例文件
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='翻贝花接口测试报告', description='测试详细')
                runner.run(suit)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # send test report by email
            if on_off == 'on':
                self.email.send_email()
            elif on_off == 'off':
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")



if __name__ == '__main__':
    obj = AllTest()
    obj.run()

