import sys,os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)

from lib.read_case import ParamDeal
from lib.request import MyRequest
from lib.parse_response import ParseResponse
from lib.util import write_excel,send_mail
from config.setting import CASE_PATH,log,CASE_FILE_START
import os

class CaseRun:
    all_count = 0
    pass_count = 0
    def get_case(self):
        '''获取excel测试用例'''
        excel_list = []
        for file in os.listdir(CASE_PATH):  # 获取excel用例
            if file.startswith(CASE_FILE_START) and (file.endswith('.xls') or file.endswith('.xlsx')):
                abs_path = os.path.join(CASE_PATH, file)  # 拼成绝对路径
                excel_list.append(abs_path)
        return excel_list

    def run_case(self,file_name):
        read_case_obj = ParamDeal()#实例化
        case_list = read_case_obj.read_excel(file_name) #读取excel里面的测试用例
        response_list = [] #存放所有的结果
        for case in case_list:
            self.all_count+=1#统计用例的总数
            req_obj = MyRequest(*case[:5])#发请求
            response_obj = ParseResponse(case[-1],req_obj.result)#校验结果
            if response_obj.status == '通过':
                self.pass_count+=1#统计通过次数
            response_list.append([str(req_obj.data),req_obj.text,response_obj.reason,response_obj.status])
        return write_excel(file_name,response_list)#写结果

    def main(self):
        report_list = [] #存放的就是所有的报告
        excel_list = self.get_case()
        for excel in excel_list:
            report_name = self.run_case(excel)
            report_list.append(report_name)
        send_mail(self.all_count,self.pass_count,report_list)
        log.debug('运行完成')



if __name__ == '__main__':
    run = CaseRun()
    run.main()










