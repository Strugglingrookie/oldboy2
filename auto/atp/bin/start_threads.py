# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/28 22:53
# @File   : start_threads.py


import sys, os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)
from config.settings import CASE_PATH, log, RELEVANCE_DATA
from lib.read_case import ParamDeal
from lib.request_send import MyRequest
from lib.parse_response import ParseResponse
from lib.utils import write_excel, send_mail
import glob, threading


class CaseRun():
    all_counts = 0
    pass_counts = 0
    report_lis = []

    def get_excel(self):
        '''获取excel测试用例列表'''
        excel_lis = []
        excel_path = os.path.join(CASE_PATH, 'test*.xls*')
        for excel_file in glob.glob(excel_path):
            excel_lis.append(excel_file)
        return excel_lis

    def run_case(self, file_name):
        read_obj = ParamDeal()
        case_lis = read_obj.read_excel(file_name)
        response_lis = []
        for case in case_lis:
            self.all_counts += 1
            req_obj = MyRequest(*case[:-1])
            parse_obj = ParseResponse(case[-1], req_obj.res)
            if parse_obj.status == "通过":
                self.pass_counts += 1
            res = [req_obj.data, req_obj.text, parse_obj.status, parse_obj.reason]
            response_lis.append(res)
        report_file = write_excel(file_name, response_lis)
        self.report_lis.append(report_file)

    def main(self):
        excel_lis = self.get_excel()
        for excel in excel_lis:
            t = threading.Thread(target=self.run_case, args=(excel,))
            t.start()

        # 所有子线程运行完才发邮件
        while threading.activeCount() != 1:
            pass

        log.info("全局关联参数池 %s" % (RELEVANCE_DATA))

        if self.all_counts:
            send_mail(self.all_counts, self.pass_counts, self.report_lis)
        log.info('done')


if __name__ == '__main__':
    run = CaseRun()
    run.main()
