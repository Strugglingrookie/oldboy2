# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 20:17
# @Author  : Xiao


from tools import Mysql
from urllib.parse import parse_qs

def op_file(filename):
    with open(filename,'rb') as f:
        data = f.read()
    return data

def favicon(environ):
    data = op_file('./templates/favicon.ico')
    return data

def index(environ):
    data = op_file('./templates/index1.html')
    return data

def regist(environ):
    method = environ.get('REQUEST_METHOD').lower()
    if method == 'post':
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH',0))
        except (ValueError):
            request_body_size = 0
        request_body = environ['wsgi.input'].read(request_body_size)
        data = parse_qs(request_body)
        user = data.get(b'user')[0].decode('utf8')
        pwd = data.get(b'pwd')[0].decode('utf8')
        if user.strip() and pwd.strip():
            mysql_check = Mysql('localhost', 3306, 'root', 'root',dbname='oldboy', charset="utf8")
            sql = "select * from user_info WHERE  name=%s"
            res = mysql_check.exec_sql(sql, user, pwd)
            if res and isinstance(res, list):
                data = b'username is already exits!'
            else:
                data = op_file('./templates/index1.html')
                sql_reg = "insert into user_info(name,password) values(%s,%s);"
                mysql_check.exec_sql(sql_reg,user,pwd)
        else:
            data = b'username and password can not be empty!'
    else:
        data = op_file('./templates/register.html')
    return data

def login(environ):
    method = environ.get('REQUEST_METHOD').lower()
    if method == 'post':
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        request_body = environ['wsgi.input'].read(request_body_size)
        data = parse_qs(request_body)
        user = data.get(b'user')[0].decode('utf8')
        pwd = data.get(b'pwd')[0].decode('utf8')
        mysql_check = Mysql('localhost', 3306, 'root', 'root', dbname='oldboy', charset="utf8")
        sql = "select * from user_info WHERE  name=%s and password=%s"
        res = mysql_check.exec_sql(sql, user, pwd)
        if res and isinstance(res,list):
            data = op_file('./templates/index1.html')
        else:
            data = b'username or password is wrong!'
    else:
        data = op_file('./templates/login.html')
    return data

