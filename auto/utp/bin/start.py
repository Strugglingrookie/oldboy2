# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/1 15:36
# @File   : start.py


import os, sys

EVN_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, EVN_PATH)

import unittest, time
from BeautifulReport import BeautifulReport
from config.settings import CASE_PATH, REPORT_PATH
from lib.tools import send_mail


def run():
    case_suite = unittest.defaultTestLoader.discover(CASE_PATH, 'test*.py')
    now = time.strftime('%Y%m%d%H%M%S')
    report_name = 'report_' + now + '.html'
    abs_report_name = os.path.join(REPORT_PATH, report_name)
    bf = BeautifulReport(case_suite)
    bf.report(description='单元测试%s' % now, filename=report_name, log_path=REPORT_PATH)
    send_mail(bf.success_count, bf.failure_count, abs_report_name)


if __name__ == '__main__':
    run()
