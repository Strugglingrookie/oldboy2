# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/27 21:25
# @File   : flask_server.py


import os, sys, flask, json, traceback

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import request, make_response
from config.settings import mysql
from lib.tools import create_token

server = flask.Flask(__name__)
user_token = {}


@server.route('/my/reg', methods=['post'])
def my_reg():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dic = request.json
        print(dic)
        name = dic.get('name').strip()
        pwd = dic.get('password').strip()
        cpwd = dic.get('cpassword').strip()
        if not name or not pwd or not cpwd or pwd != cpwd:
            raise ImportError
        sql = "select * from userinfo where username=%s"
        res = mysql.exec_sql(sql, name)
        print(res)
        if res:
            rs_dic = {"code": "111111", "msg": "username is exist!"}
        else:
            sql = "insert into userinfo(username,password) values(%s,%s)"
            mysql.exec_sql(sql, name, pwd)
            rs_dic = {"code": "000000", "msg": "regist success"}
    except:
        print(traceback.format_exc())
        rs_dic = {"code": "111111", "msg": "regist error"}
    finally:
        rs_json = json.dumps(rs_dic)
        resp.response = rs_json
        return resp


@server.route('/my/login', methods=['post'])
def my_login():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dic = request.json
        name = dic.get('name')
        pwd = dic.get('password')
        sql = "select * from userinfo where username=%s and password=%s"
        res = mysql.exec_sql(sql, name, pwd)
        print(res)
        if res:
            token = create_token()
            user_token[name] = token
            rs_dic = {"code": "000000", "msg": "login success", "token": token}
        else:
            rs_dic = {"code": "111111", "msg": "name or password error"}
    except:
        print(traceback.format_exc())
        rs_dic = {"code": "111111", "msg": "login error"}
    finally:
        rs_json = json.dumps(rs_dic)
        resp.response = rs_json
        print(user_token)
        return resp


@server.route('/my/index', methods=['get', 'post'])
def my_index():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dic = request.json
        name = dic.get('name')
        token = dic.get('token')
        if user_token.get(name) != token:
            raise ImportError
        else:
            rs_dic = {"code": "000000", "msg": "index success!"}
    except:
        print(traceback.format_exc())
        rs_dic = {"code": "111111", "msg": "permission error"}
    finally:
        rs_json = json.dumps(rs_dic)
        resp.response = rs_json
        return resp


server.config['JSON_AS_ASCII'] = False
# 指定host为“0.0.0.0”后，局域网内其他IP就都可以访问了
server.run(port=8080, host='0.0.0.0', debug=True)
