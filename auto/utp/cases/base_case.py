# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/1 17:55
# @File   : base_case.py


import unittest
from lib.request_send import MyRequest
from lib.tools import get_value, json_assert


class BaseCase(unittest.TestCase):
    def regist(self, name, pwd, cpwd):
        url = "/my/reg"
        method = "post"
        data = {"name": name, "password": pwd, "cpassword": cpwd}
        headers = {"Content-Type": "application/json"}
        req_obj = MyRequest(url, method, data, headers)
        expected_res = {"code": "000000"}
        self.assertTrue(json_assert(expected_res, req_obj.res),
                        "校验失败！预期结果%s  实际结果%s" % (expected_res, req_obj.res))
        # 如果注册失败，调用这个方法的用例也直接失败

    def login(self, name, pwd):
        '''获取token'''
        url = "/my/login"
        method = "post"
        data = {"name": name, "password": pwd}
        headers = {"Content-Type": "application/json"}
        req_obj = MyRequest(url, method, data, headers)
        token = get_value(req_obj.res, 'token')
        expected_res = {"code": "000000"}
        self.assertTrue(json_assert(expected_res, req_obj.res),
                        "校验失败！预期结果%s  实际结果%s" % (expected_res, req_obj.res))
        return token

    def clear_data(self):
        '''清理数据库'''
        pass


if __name__ == '__main__':
    b = BaseCase()
    b.regist("xg", "123456", "123456")
