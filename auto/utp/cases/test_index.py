# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/1 17:53
# @File   : test_index.py


import unittest
from config.settings import REPORT_PATH, mysql
from lib.request_send import MyRequest
from lib.tools import json_assert
from BeautifulReport import BeautifulReport
from cases.base_case import BaseCase


class TestIndex(BaseCase):
    name = "xiaogang"
    pwd = "123456"

    @classmethod
    def tearDownClass(cls):
        sql = "delete from userinfo where username=%s"
        print(cls.name)
        mysql.exec_sql(sql, cls.name)

    def test_index(self):
        '''test_index...'''
        self.regist(self.name, self.pwd, self.pwd)
        token = self.login(self.name, self.pwd)
        url = "/my/index"
        method = "post"
        data = {"name": self.name, "token": token}
        headers = {"Content-Type": "application/json"}
        req_obj = MyRequest(url, method, data, headers)
        expected_res = {"code": "000000"}
        self.assertTrue(json_assert(expected_res, req_obj.res),
                        "校验失败！预期结果%s  实际结果%s" % (expected_res, req_obj.res))


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.makeSuite(TestIndex)
    bf = BeautifulReport(suite)
    file_name = "test_report"
    bf.report(description="Login testing", filename=file_name, log_path=REPORT_PATH)
    # print(get_params(USER_INFO))
