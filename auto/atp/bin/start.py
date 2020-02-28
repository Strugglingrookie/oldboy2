# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/28 18:46
# @File   : start.py


import sys, os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)
from config.settings import CASE_PATH, log
from lib.read_case import ParamDeal
from lib.request_send import MyRequest
from lib.parse_response import ParseResponse
from lib.utils import write_excel, send_mail
import glob


class CaseRun():
    all_counts = 0
    pass_counts = 0

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
        return write_excel(file_name, response_lis)

    def main(self):
        report_lis = []
        excel_lis = self.get_excel()
        for excel in excel_lis:
            report_name = self.run_case(excel)
            report_lis.append(report_name)
        if self.all_counts:
            send_mail(self.all_counts, self.pass_counts, report_lis)
        log.info('done')


if __name__ == '__main__':
    run = CaseRun()
    run.main()
