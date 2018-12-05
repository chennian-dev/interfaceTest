#coding:utf-8\
import os
class eqlfun:

    # 对象判断：1、值相等 2、类型一样 3、身份一样,引用同一个对象

    def __init__(self):
        self.a = 5
        self._msg =''

    def eqlTrue(self,a,b):
        if a == b:
            return True
        elif type(a) == type(b):
            return False
        elif a is b :
            return False

    def str2list(self,str):
        lists = list(str)
        if len(lists) > 0:
            for i in lists:
                print '列表元素为： %s' % i

    def list2str(self,lists):
        strs = str(lists)
        print '字符串数据显示为： %s' % strs

    def strUtil(self):
        # 测试字符串相关处理方法  切片
        # 索引号可以是正数由0开始从左向右，也可以是负数由-1开始从右向左
        # 通常一个切片操作要提供三个参数 [start_index:  stop_index:  step]
        # start_index是切片的起始位置
        # stop_index是切片的结束位置（不包括）
        # step可以不提供，默认值是1，步长值不能为0，不然会报错ValueError。
        str ='www.baidu.com'
        print str[0:]
        print str[0:1]
        print str[1:]
        print str[1:2]
        print str[6:-1]
        print str[:2]
        for i in range(1,100)[6::7]:
            print '取数组里7的倍数 %s' % i

    def fileUtil(self,num,_msg):
        realDir = os.path.split(os.path.realpath(__file__))[0]
        fileName = 'a.txt'
        realPath = os.path.join(realDir,fileName)
        try:
            if(num == 0):
                if(os._exists(realPath)):
                    os.remove(realPath)
                file_object = open(realPath,'w')
                file_object.write(_msg)
            elif(num == 1):
                file_object = open(realPath,'r')
                res = file_object.readline()
                print _msg +' : %s' % res
        except Exception:
            print Exception
            file_object.close()








if __name__ == '__main__':
    print  os.path.realpath(__file__)
    b=5
    t=eqlfun()
    print t.eqlTrue(t.a,b)
    print t.a is b
    print type(t.a) == type(b)
    t.str2list('chennian')
    lists = (1,2,3)
    t.list2str(lists)
    t.strUtil()
    listval = range(1,100,2)
    for m in listval:
        print 'lists数据的值为： %s' % m
    str1 = '2'
    str2 = 'worldrww'
    print str1.join(str2)
    print str2.replace('w','W')
    print str2.replace('w','W',1)
    print str2.split('w',2)
    str3 = ' 123a '
    print str3.strip()
    list  =[1,2,3,4,5]
    print list.index(1)
    print list.pop(1)
    print list
    dicDemo = {'x':12,'y':[11,32,44]}
    print dicDemo['y'][1]
    listDemo=[1,[1,2,3]]
    print listDemo[1][2]
    dicDemo2 = dicDemo.copy()
    t1,t2 = dicDemo2.items()
    print t1
    print t2
    t.fileUtil(0,'EveryThing is ok! Just do it!!!')
    t.fileUtil(1,'the message is ')
