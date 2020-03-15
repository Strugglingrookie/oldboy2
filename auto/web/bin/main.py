# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/13 21:13
# @File   : main.py


import unittest,time,os
from config.settings import CASE_PATH,REPORT_PATH,logger
from lib.HTMLTestRunner import HTMLTestRunner


class Main():
    def run(self):
        suite = unittest.TestSuite()
        cases = unittest.defaultTestLoader.discover(CASE_PATH)
        for case in cases:
            suite.addTest(case)
        now = time.strftime('%Y%m%d%H%M%S')
        report_name = 'report_' + now + '.html'
        abs_report_name = os.path.join(REPORT_PATH, report_name)
        f = open(abs_report_name,'wb')
        runner = HTMLTestRunner(f,verbosity=1,title=u'WebUi测试报告',description='测试结果详情')
        runner.run(suite)
        f.flush()
        f.close()


if __name__ == '__main__':
    Main().run()




