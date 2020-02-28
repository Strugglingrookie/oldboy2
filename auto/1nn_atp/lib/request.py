import requests,nnlog,traceback
from config.setting import HOST,log
from urllib.parse import urljoin

class MyRequest:
    def __init__(self,url,method,data=None,headers=None,is_json='否'):
        self.url = urljoin(HOST,url)
        self.data = data
        self.headers = headers
        self.is_json = is_json
        self.method = method.lower()
        self.req()

    def req(self):
        try:
            if self.is_json=='是':
                response = requests.request(self.method,self.url,params=self.data,json=self.data,headers=self.headers).json()
            else:
                response = requests.request(self.method,self.url,params=self.data,data=self.data,headers=self.headers).json()
        except Exception as e:
            log.error('请求 %s的时候出错了，请求参数是：%s，错误信息是 %s' % (self.url,self.data,traceback.format_exc()))
            self.result = {"msg":"请求接口出错了","error_msg":traceback.format_exc()}
            self.text = ' {"msg":"请求接口出错了","error_msg":%s} '%traceback.format_exc()
        else:
            self.result = response
            self.text = str(response)


