# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/27 22:47
# @File   : request_send.py


import requests, traceback, threading
from config.settings import HOST, log
from urllib.parse import urljoin


class MyRequest():
    def __init__(self, url, method, data=None, headers=None, is_json="是"):
        self.tid = threading.get_ident()
        self.url = urljoin(HOST, url)
        self.method = method.lower()
        self.data = data
        self.headers = headers
        self.is_json = is_json
        self.req()

    def req(self):
        log.info("开始发起请求:\nurl:%s\nmethod:%s\nheaders:%s\nreq_data:%s"
                 % (self.url, self.method, self.headers, self.data))
        try:
            if self.is_json == '是':
                res = requests.request(self.method, self.url, params=self.data, json=self.data,
                                       headers=self.headers).json()
            else:
                res = requests.request(self.method, self.url, params=self.data, data=self.data,
                                       headers=self.headers).json()
        except Exception as e:
            log.error('请求 %s的时候出错了，请求参数是：%s，错误信息是 %s' % (self.url, self.data, traceback.format_exc()))
            self.res = {"msg": "请求接口出错了", "error_msg": traceback.format_exc()}
            self.text = ' {"msg":"请求接口出错了","error_msg":%s} ' % traceback.format_exc()
        else:
            self.res = res
            self.text = str(res)
            log.info('请求 %s 成功，响应参数 %s' % (self.url, self.res))


if __name__ == '__main__':
    cases = []
    for case in cases:
        req_obj = MyRequest(*case[:-1])  # 发请求
        req_obj.req()
