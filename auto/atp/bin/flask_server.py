# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/27 21:25
# @File   : flask_server.py


import os,sys,flask,json
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import request,make_response

server=flask.Flask(__name__)


@server.route('/my/login',methods=['post'])
def my_login():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dic = request.json
        if dic.get('name')!='xg' or dic.get('password')!='123456':
            raise NameError
        rs_dic = {"code":"000000","msg":"login success","token":"asdfgh"}
    except:
        rs_dic = {"code": "111111", "msg": "login error"}
    finally:
        rs_json = json.dumps(rs_dic)
        resp.response = rs_json
        return resp


@server.route('/my/index',methods=['get','post'])
def my_index():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dic = request.json
        token = dic.get('token')
        if not token or token != 'asdfgh':
            raise NameError
        rs_dic = {"code":"000000","msg":"index success!"}
    except:
        rs_dic = {"code": "111111", "msg": "permission error"}
    finally:
        rs_json = json.dumps(rs_dic)
        resp.response = rs_json
        return resp


server.config['JSON_AS_ASCII'] = False
# 指定host为“0.0.0.0”后，局域网内其他IP就都可以访问了
server.run(port=8080, host='0.0.0.0', debug=True)

