# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 14:11
# @File   : 03parametric.py


import unittest, HTMLTestRunner
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
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Login))
    fw = open('11report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fw, title='参数化测试数据', description='描述'
    )
    runner.run(suite)
