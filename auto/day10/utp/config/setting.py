import os
import nnlog

EMAIL_INFO = {
    'user':'uitestp4p@163.com',
    'host':'smtp.163.com',
    'password':'houyafan123'
}

MYSQL_INFO = {
    'host':'118.24.3.40',
    'db':'jxz',
    'user':'jxz',
    'password':'123456',
    'charset':'utf8',
    'port':3306,
    'autocommit':True,
}

TO = ['511402865@qq.com','525586735@qq.com','526962645@qq.com']

CC = ['540493450@qq.com','945968766@qq.com']

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASE_PATH = os.path.join(BASE_PATH,'cases')#查找用例的目录

DATA_PATH = os.path.join(BASE_PATH,'data') #用例数据的目录

LOG_PATH = os.path.join(BASE_PATH,'logs','utp.log')

REPORT_PATH = os.path.join(BASE_PATH,'report')


ENV = 'test' #默认使用测试环境

host_map = {
    "test":"http://api.nnzhp.cn",
    "dev":"http://118.24.3.40:81/",
    "pre":"http://api.nnzhp.cn/",
}

HOST = host_map.get(ENV)

log = nnlog.Logger(LOG_PATH) #

CASE_FILE_START = 'test' #这个找用例的规则，以什么开头就运行