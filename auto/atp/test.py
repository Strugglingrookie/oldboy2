# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/26 18:56
# @File   : jsonpath_test.py


# test jsonpath module
# api 地址 https://api.apiopen.top/getJoke?page=1&couont=2&type=video
import jsonpath, faker,threading,re

dic = {
	"code": 200,
	"message": "成功!",
	"result": [
		{
			"sid": "30372629",
			"text": "活跃一下气氛",
			"type": "video",
			"thumbnail": "http://wimg.spriteapp.cn/picture/2020/0224/5e53d5374e79c_wpd.jpg",
			"video": "http://uvideo.spriteapp.cn/video/2020/0224/5e53d5374e79c_wpd.mp4"
		},
		{
			"sid": "30368620",
			"text": "忍无可忍的时候该怎么办？",
			"type": "video",
			"thumbnail": "http://wimg.spriteapp.cn/picture/2020/0224/5e53660811d4f__b.jpg",
			"video": "http://uvideo.spriteapp.cn/video/2020/0224/5e5366082ab36_wpd.mp4"
		}
	]
}
#
# print(dic["result"][0]["video"])
print(jsonpath.jsonpath(dic, '$..%s'%'video')) # 模糊匹配key为video的value，返回的是列表
# print(jsonpath.jsonpath(dic, '$.student')) # 没有值返回false
# print(jsonpath.jsonpath(dic, '$.result[0].text'))


# faker 生成 phone,card_id,name,email,bankcard_id
# 可以生成的数据类型 https://www.jianshu.com/p/6bd6869631d9
f = faker.Faker(locale='zh-CN') #指定国内
#
# print(f.ssn())# 身份证号码
# print(f.phone_number())# 手机号
# print(f.email())# 邮箱
# print(f.address())# 地址
# print(f.name())# 名字
# print(f.company())# 公司名称
# print(f.credit_card_number())# 信用卡号

params_map = {
	"<card>":f.ssn,
	"<phone>":f.phone_number,
	"<email>":f.email,
	"<name>":f.name,
	"<password>":f.password,
	"<bankcard>":f.credit_card_number,
	"<money>":f.random_int,
	"<address>":f.address
}


def params_func(params):
	for map in params_map:
		if map in params:
			params = params.replace(map, params_map[map]())
	return params

s = "phone=<phone>&user=&name=<name>&token=${token}"
s=''
s = params_func(s)
print(s)


def str_to_dic(s):
	if s:
		dic = {}
		for var in s.split("&"):
			k, v = var.split("=")
			dic[k] = v
		return dic
	return s

print(str_to_dic(s))

print(threading.get_ident())

s = "phone={phone}&token={user_token}"

lis = re.findall(r'\{(.*?)\)', s)
print(lis)

# s2 = "name=123"
# print(s2.split("$"))
#
# dic2 = {1:'a'}
# dic2.setdefault(1,{})
# print(dic2[1])
#
# res={'code': '000000', 'msg': 'login success', 'token': 'asdfgh'}
# print(jsonpath.jsonpath(res, '$..token'))

n1 = 'xg'
n2 = 'xg'
print(eval("n1==n2"))

import os
filename = r'D:\oldboy\auto\atp\readme.md'
print(os.path.basename(filename))
