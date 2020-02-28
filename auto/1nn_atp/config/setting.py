import os
import faker
from .utli import random_password
import nnlog

EMAIL_INFO = {
    'user':'uitestp4p@163.com',
    'host':'smtp.163.com',
    'password':'houyafan123'
}

TO = ['511402865@qq.com','525586735@qq.com','526962645@qq.com']

CC = ['540493450@qq.com','945968766@qq.com']

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASE_PATH = os.path.join(BASE_PATH,'cases')

LOG_PATH = os.path.join(BASE_PATH,'logs','atp.log')

REPORT_PATH = os.path.join(BASE_PATH,'report')

f = faker.Faker(locale='zh-CN')

ENV = 'test' #默认使用测试环境

host_map = {
    "test":"http://api.nnzhp.cn",
    "dev":"http://118.24.3.40:81/",
    "pre":"http://api.nnzhp.cn/",
}

HOST = host_map.get(ENV)

func_map ={
    "<phone>":f.phone_number,
    "<id_card>":f.ssn,
    "<email>":f.email,
    "<name>":f.name,
    "<addr>":f.address,
    "<password>":random_password
} #这个是支持的参数化，如果要加其他的参数化，在这里继续加就行了。

log = nnlog.Logger(LOG_PATH) #

CASE_FILE_START = 'test' #这个找用例的规则，以什么开头就运行