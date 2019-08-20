# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 18:53
# @Author  : Xiao
import requests
from requests_toolbelt import MultipartEncoder
# file = {'file_name':['report.docx',open(r'D:\report.docx','rb')],}
file = {'file_name':open(r'D:\report.docx','rb')}
me = MultipartEncoder(file)


response = requests.post(
   url='http://172.30.0.21:8080/InnerEval/api/pbcc/report/fileUpload',
   data={
       'multiple':'',
       'filetype':'77',
       'uploadBy':'XIAOWD'
   },
   headers={
       'source':'WPT',
       'Content-Type':me.content_type
   },
    files=file
)
print('请求状态:%s\n响应结果:%s'%(response.status_code,response.text))


# def post(self,url,param_dict,param_header,file = '',param_type = 'x-www-form-urlencode'):
#     '''
# 　　@功能：封装post方式
# 　　@paramType:指传入参数类型，可以是form-data、x-www-form-urlencode、json
# 　　'''
#     respone_code = None
#     respone = None
#     try:
#         if param_type == 'x-www-form-urlencode':
#             params = param_dict
#         elif param_type == 'json':
#             params = json.dumps(param_dict)
#         if file == '' :
#             ret = requests.post(self.Server+url, data=params, headers=param_header)
#         else:
#             files = {'file':open(file,'rb')}
#             ret = requests.post(self.Server+url, data=params, headers=param_header,files = files)
#         respone_code = ret.status_code
#         respone = ret.text
#         except Exception as e:
#             respone_code = e.getcode()
#             respone = e.read().decode("utf-8")
#
#         return respone_code,respone
