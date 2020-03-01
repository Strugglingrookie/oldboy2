# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/1 9:51
# @File   : test_login.py


import unittest
from config.settings import USER_INFO, REPORT_PATH
from lib.request_send import MyRequest
from lib.tools import get_params, json_assert, str_to_dic
from parameterized import parameterized
from BeautifulReport import BeautifulReport


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_params(USER_INFO))
    def test_login(self, name, pwd, expected_data):
        '''test_login...'''
        url = "/my/login"
        method = "post"
        data = {"name": name, "password": pwd}
        headers = {"Content-Type": "application/json"}
        req_obj = MyRequest(url, method, data, headers)
        expected_json = str_to_dic(expected_data)
        self.assertTrue(json_assert(expected_json, req_obj.res),
                        "校验失败！预期结果%s  实际结果%s" % (expected_json, req_obj.res))


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.makeSuite(TestLogin)
    bf = BeautifulReport(suite)
    file_name = "test_report"
    bf.report(description="Login testing", filename=file_name, log_path=REPORT_PATH)
    # print(get_params(USER_INFO))
