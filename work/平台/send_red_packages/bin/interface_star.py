import os,sys,flask,random,time,string,json,threading
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from flask import request,make_response,Response, jsonify
# from flask_restful import request
from lib.tools import md5_sign,get_sign,oprate_sql
from conf.config import *

server=flask.Flask(__name__)

# 1. checkSign  sign = md5(key1=value1&key2=value2&key3=value3)  key按自然顺序排序;
# 2. headeSign头部验签  sign = md5(signKey + 请求体json串)  signKey = select sign_key from yyfax_pay.merchant_config where merchant_code = '2000' ;
@server.route('/sign',methods=['get','post'])
def auto_sign():
    try:
        if not request.json.get('fileNames'):
            if "Sign" not in request.headers:
                print("sign = md5(key1=value1&key2=value2&key3=value3)  key按自然顺序排序")
                dict = request.json
                if 'params' in dict:
                    dict = request.json['params']
                sign = md5_sign(dict)
            else:
                print("headeSign头部验签  sign = md5(signKey + 请求体json串)")
                str = request.data.decode()
                print(str)
                new_str=str.replace("\n","").replace("\t","")
                print(new_str)
                sign = get_sign(new_str)
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

@server.route('/')
def index():
    resp = Response('<h2>首页</h2>')
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp

@server.route('/course')
def courses():
    resp = Response(json.dumps({'name':'三儿'}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@server.route('/create/user',methods=['post',])
def create():
    name = request.form.get('name')
    pwd = request.form.get('password')
    user={name:{'password':pwd}}
    with open('user.json','r') as f:
        data = json.load(f)
    print(data)
    data.update(user)
    print(data)
    with open('user.json','w') as f:
        json.dump(data,f)
    resp = Response(json.dumps(data))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print(resp)
    return resp


def req_url(url,data,header,i,res_dic):
    print('开始第 %s 次发送委外邮件' % i)
    send_email_res = requests.post(url, json=data, headers=header).json()
    res_dic['第 %s 次发送委外邮件结果' % i] = send_email_res
    print('结束第 %s 次发送委外邮件' % i)


@server.route('/email',methods=['get','post'])
def sed_email():

    times = int(request.args.get("times"))
    login_url = "https://testplmssit08.yylending.com/plms-um-service/http/user/login"
    data = {"password": "96qyVNn/porDY","userId": "sijl"}
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
              'systemid': 'PLMS', 'content-type': 'application/json;charset=UTF-8'}
    login_res = requests.post(login_url, json=data, headers=header).json()
    token = login_res.get('data').get('accToken') if login_res.get('data') else None

    send_email_url = "https://testplmssit08.yylending.com/plms-urge-service/http/urge/outsource/sendImageMail"
    send_email_data = {"loanNo": "LA20170807000104", "attachmentNos": ["IM2019090400000059"],
                       "companyId": "OS20160718000001",
                       "attachmentTypes": ["A-01", "A-08", "A-10", "A-25", "A-31", "A-99"]}
    header["acctoken"] = token
    res_dic = {}
    t_list = []
    for i in range(1, times+1):
        t = threading.Thread(target=req_url, args=(send_email_url,send_email_data,header,i,res_dic))
        t_list.append(t)
        t.start()
    for t in t_list:
        t.join()
    return jsonify(res_dic)

@server.route('/my/login',methods=['get','post'])
def my_login():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dic = request.json
        print(dic)
        if dic.get('name')!='xg' or dic.get('password')!='123456':
            raise NameError
        rs_json = {"code":"000000","msg":"login success","token":"asdfgh"}
        rs_data = json.dumps(rs_json)
        resp.response = rs_data
        print(rs_data)
        return resp
    except Exception as e:
        print(e)
        rs_json = {"code": "111111", "msg": "login error"}
        rs_data = json.dumps(rs_json)
        return rs_data

@server.route('/my/index',methods=['get','post'])
def my_index():
    resp = make_response()
    resp.headers["Content-Type"] = "application/json"
    resp.headers["charset"] = "UTF-8"
    try:
        dict = request.json
        print(dict)
        token = dict.get('token')
        if not token or token != 'asdfgh':
            raise NameError
        rs_json = {"code":"000000","msg":"index success!"}
        rs_data = json.dumps(rs_json)
        resp.response = rs_data
        print(rs_data)
        return resp
    except Exception as e:
        print(e)
        return "格式不对，请检查json格式，对比小幺鸡请求参数！    http://172.30.3.61:8092/doc/1YaX6ZoSxS"


server.config['JSON_AS_ASCII'] = False
server.run(port=8080, host='0.0.0.0', debug=True)  # 指定host为“0.0.0.0”后，局域网内其他IP就都可以访问了

