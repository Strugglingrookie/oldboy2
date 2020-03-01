# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 15:18
# @File   : 07beautiful_report.py


import unittest
from BeautifulReport import BeautifulReport
from parameterized import parameterized


def login(username, passwd):
    if username == 'xiaogang' and passwd == '123456':
        return True
    else:
        return False

class Login(unittest.TestCase):
    @parameterized.expand(
        [
            # 可以是list，也可以是元祖
            ['xiaogang', '123456', True],
            ['', '123456', True],
            ['xiaogang', '', False],
            ['adgadg', '123456', False]
        ]
    )
    def test_login(self, username, passwd, exception):
        '''登录'''
        # 这里的参数对应上述列表里的元素，
        # 运行的时候会遍历上述列表里的二维列表直到所有元素都调用运行完成
        res = login(username, passwd)
        self.assertEqual(res, exception)


if __name__ == '__main__':
    suite = unittest.makeSuite(Login)
    bf = BeautifulReport(suite)
    bf.report(filename='beautiful_report', description='描述')
