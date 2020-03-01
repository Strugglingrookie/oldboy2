# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 15:05
# @File   : 04params_file.py


# 用文件作为参数进行unittest单元测试
import unittest, HTMLTestRunner
from parameterized import parameterized


def redCvs(filename, sep=','):
    lis = []
    # rb模式，在任何操作系统下打开都不会报错，考虑到系统兼容性
    with open(filename, 'rb') as f:
        for line in f:
            # decode是因为上面用了rb模式打开，是bytes类型，需要解码
            lis1 = line.decode().strip().split(',')
            lis.append(lis1)
    return (lis)


def login(username, passwd):
    if username == 'xiaogang' and passwd == '123456':
        return True
    return False


class Login(unittest.TestCase):
    @parameterized.expand(redCvs('params.txt'))
    def testa(self, username, passwd, exception):
        res = login(username, passwd)
        self.assertEqual(bool(exception), res)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Login))
    fw = open('report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fw, title='test测试', description='嘿嘿'
    )
    runner.run(suite)
