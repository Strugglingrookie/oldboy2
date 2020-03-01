# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 15:15
# @File   : 06case_batchs.py


import unittest, HTMLTestRunner

suite = unittest.TestSuite()  # 定义测试集合
all_case = unittest.defaultTestLoader.discover(
    r'E:\szg\bestTest\day11\AUTO\case', 'test_*.py'
)  # 找到case目录下所以的.py文件

for case in all_case:
    # 循环添加case到测试集合里面
    suite.addTests(case)

if __name__ == '__main__':
    fw = open('report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fw, title='多个文件运行'
    )
    runner.run(suite)
