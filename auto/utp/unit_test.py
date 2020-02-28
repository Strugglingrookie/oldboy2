# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/28 23:49
# @File   : unit_test.py


import unittest

def calc(a,b):
    return a+b


class CalcTest(unittest.TestCase):
    def test_normal(self):
        a = 1
        b = 2
        res = calc(a,b)
        self.assertEqual(3,res)

    def test_unusual(self):
        a = 2
        b = 2
        res = calc(a, b)
        self.assertEqual(4, res, "执行出错了！")


unittest.main()