import os,sys,flask,random,time,string,json
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import request,make_response
from flask_restful import request
from lib.tools import md5_sign,get_sign,oprate_sql
from conf.config import *

server=flask.Flask(__name__)

# 1. checkSign  sign = md5(key1=value1&key2=value2&key3=value3)  key按自然顺序排序;
# 2. headeSign头部验签  sign = md5(signKey + 请求体json串)  signKey = select sign_key from yyfax_pay.merchant_config where merchant_code = '2000' ;
@server.route('/sign',methods=['get','post'])
def auto_sign():
    try:
        if not request.json.get('fileNames'):
            # if "Sign" not in request.headers:
                print("sign = md5(key1=value1&key2=value2&key3=value3)  key按自然顺序排序")
                dict = request.json
                if 'params' in dict:
                    dict = request.json['params']
                sign = md5_sign(dict)
            # else:
            #     print("headeSign头部验签  sign = md5(signKey + 请求体json串)")
            #     str = request.data.decode()
            #     print(str)
            #     new_str=str.replace("\n","").replace("\t","")
            #     print(new_str)
            #     sign = get_sign(new_str)
        else:
            dict = request.data.decode()
            sign= get_sign(dict)
        print(sign)
        return '{"sign:":"%s"}'%(sign)
    except Exception as e:
        print(e)
        return "格式不对，请检查json格式，对比小幺鸡请求参数！"

# 生成还款代扣的批量跑批数据，王超专用
@server.route('/create',methods=['get','post'])
def create_data():
    try:
        src=set(string.digits)
        serial1=''.join(random.sample(src, 10))
        serial2=''.join(random.sample(src, 7))
        serial_abc=str(serial1)+str(serial2)
        dict=request.json
        number = int(dict["number"])
        user_id =dict["user_id"]
        loan_no =dict["loan_no"]
        amount =dict["amount"]
        pay_type =dict["pay_type"]
        pay_channel =dict["pay_channel"]
        notify_url =dict["notify_url"]
        for i in range(number):
            serial_no=serial_abc+str(i)
            sql='''insert into S62.withhold_info(serial_no,user_id,loan_no,amount,state,create_time,update_time,pay_type,pay_channel,notify_url) values ("{serial_no}","{user_id}","{loan_no}",{amount},1,NOW(),NOW(),{pay_type},{pay_channel},"{notify_url}");'''.format(serial_no=serial_no,user_id=user_id,loan_no=loan_no,amount=amount,pay_type=pay_type,pay_channel=pay_channel,notify_url=notify_url)
            res = oprate_sql(sql, SETTLE_HOST, USER, PASSWD, port=SETTLE_PORT)
            print(res)
        return "成功插入%s条记录"%number
    except Exception as e:
        print(e)
        return "参数有误，请核查json参数！"

# CMA_U046 投资平台用户注册
@server.route('/cma/user/partner/register',methods=['get','post'])
def rs_identify():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dict = request.json
        print(dict)
        rs_json = {"code":"000000","msg":"","content":{"recommendedLinks":"123","registerMethod":0,"invitationCode":123456}}
        if dict["registerMethod"] == 0 or dict["registerMethod"] == "0":
            rs_json["content"]["registerMethod"] = 0
            rs_json["content"].pop("recommendedLinks")
        else:
            rs_json["content"]["registerMethod"] = 1
            rs_json["content"].pop("invitationCode")
        rs_data = json.dumps(rs_json)
        resp.response = rs_data
        print(rs_data)
        time.sleep(120)
        return resp
    except Exception as e:
        print(e)
        return "格式不对，请检查json格式，对比小幺鸡请求参数！    http://172.30.3.61:8092/doc/1YaX6ZoSxS"

# CMA_E039 荐客校验准入
@server.route('/cma/entry/partner/investor/check',methods=['get','post'])
def investor_check():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dict = request.json
        print(dict)
        rs_json = {"code":"000000","msg":""}
        rs_data = json.dumps(rs_json)
        resp.response = rs_data
        print(rs_data)
        time.sleep(120)
        return resp
    except Exception as e:
        print(e)
        return "格式不对，请检查json格式，对比小幺鸡请求参数！    http://172.30.3.61:8092/doc/1YZJu09s7Z"

# CMA_U046 CMA_E038 荐客推荐列表
@server.route('/cma/entry/partner/investor/list',methods=['get','post'])
def investor_list():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dict = request.json
        # phone = dict["phone"]
        print(dict)
        rs_json = {"code":"000000","msg":"","content":{"rcmdId":"123","status":1,"statusName":123456,"loanCount":123456,"phone":13537738880}}
        rs_data = json.dumps(rs_json)
        resp.response = rs_data
        print(rs_data)
        time.sleep(120)
        return resp
    except Exception as e:
        print(e)
        return "格式不对，请检查json格式，对比小幺鸡请求参数！    http://172.30.3.61:8092/doc/1YaX6ZoSxS"

# mock核心返回通知放款成功接口  {"retCode":'000000',"retMsg":""}
@server.route('/BS/rest/dispatch/forward',methods=['get','post'])
def loan_sucess():
    return "D5RwV3kqqLSxduwLNFPd0QfVNaSwQ65CSFhoPmVJzUiamkmq5vuDvzIBvu6RWvIJ"

server.run(port=8080, host='0.0.0.0', debug=True)  # 指定host为“0.0.0.0”后，局域网内其他IP就都可以访问了




