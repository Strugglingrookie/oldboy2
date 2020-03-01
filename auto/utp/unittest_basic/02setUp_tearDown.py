# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 14:07
# @File   : 02setUp_tearDown.py


# setUp和tearDown的运用
import unittest


class MyTest(unittest.TestCase):
    # 类开始前运行，比如在执行这些用例之前需要备份数据库
    @classmethod
    def setUpClass(cls):
        print('this is setUpClass')

    # 类结束后运行，比如在执行这些用例之后需要还原数据库
    @classmethod
    def tearDownClass(cls):
        print('this is tearDownClass')

    def setUp(self):  # 每条测试用例执行前运行
        print('this is setUp')

    def tearDown(self):  # 每条测试用例执行后运行
        print('this is tearDown')

    def testa(self):
        print('测试用例1')
        self.assertEqual(1, 1)

    def testb(self):
        print('测试用例2')
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
