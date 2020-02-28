import sys,os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)


import unittest
import time
from config.setting import CASE_PATH,REPORT_PATH
from utlis.tools import send_mail
from BeautifulReport import BeautifulReport
def run():
    case_suite = unittest.defaultTestLoader.discover(CASE_PATH,'test*.py')
    bf = BeautifulReport(case_suite)
    report_name = time.strftime('%Y%m%d%H%M%S')+'_report.html'
    report_abs_path = os.path.join(REPORT_PATH,report_name)
    bf.report('接口测试报告%s'%time.strftime('%Y%m%d%H%M%S'),filename=report_name,log_path=REPORT_PATH)
    send_mail(bf.success_count,bf.failure_count,report_abs_path)
if __name__ == '__main__':
    run()