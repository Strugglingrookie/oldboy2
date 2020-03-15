# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/13 21:28
# @File   : test_bug.py


from page.page import Page
import unittest


class IdTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

    def test_a_id(self):
        self.page.url()
        self.page.top()
        self.page.test_id()
        result = self.page.check_id(self.test_a_id.__name__)
        self.assertTrue(result,'测试id报错，见截图!')


if __name__ == '__main__':
    unittest.main()