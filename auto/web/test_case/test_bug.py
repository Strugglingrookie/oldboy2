# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/13 21:28
# @File   : test_bug.py


from page.page import Page
from lib.tools import Tool
import unittest


class IdTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()
        cls.tool = Tool()
        # 重点！！！ 每次测试之前需要删除报错的截图，不然成功的用例也会将错误图片放进去
        cls.tool.clear_picture()

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