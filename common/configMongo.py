#coding:utf-8
from pymongo import MongoClient
import readConfig as readConfig
from Log import MyLog as Log
import json


localReadConfig = readConfig.ReadConfig()


class MyMongo:
    global dburl
    dburl = localReadConfig.get_mongo("dburl")

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None

    def connectMongo(self):
        try:
            # connect to DB
            self.db = MongoClient(dburl)
            print("Connect MongoDB successfully!")
        except BaseException as ex:
            self.logger.error(str(ex))

    def closeDB(self):
        self.db.close()
        print("Database closed!")

    def getPhoneCode(self,phone):
        self.connectMongo()
        try:
            # sort()方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序，-1为降序。 .sort([("age",1)]):
            # https://www.cnblogs.com/melonjiang/p/6536876.html
            cursor = self.db['fanbuy']['sys_sms_log'].find({"phone":"0086"+phone}).sort([("cs",-1)]).limit(1)
            for rs in cursor:
                return json.loads(rs['param'])['code']
        except BaseException as ex:
            self.logger.error("查询mongodb 数据失败，"+str(ex))

if __name__ == '__main__':
    mongo = MyMongo()
    print mongo.getPhoneCode('15678787878')
