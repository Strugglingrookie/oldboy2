# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 15:11
# @File   : 05relevance.py


# 接口关联，只是一个思路，并没有结合实际的项目，有兴趣的同学可以尝试下
import unittest, HTMLTestRunner


def login(username, passwd):
    if username == 'xiaogang' and passwd == '123456':
        return '138'
    else:
        return False


def shopping(sign):
    if sign == '138':
        return True
    else:
        return False


class My(unittest.TestCase):
    # 这里不以test开头命名，就是一普通方法
    # 在执行测试用例的时候并不会运行，调用的时候才会
    def login(self):
        res = login('xiaogang', '123456')
        self.assertEqual(res, '138')
        return res

    def test_login_cj(self):
        res = self.login()  # 调用登录方法，获取sign
        self.jp = shopping(res)
        self.assertEqual(self.jp, True)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(My))
    fw = open('report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fw, title='关联接口', description='描述'
    )
    runner.run(suite)
