# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/26 18:53
# @File   : read_case.py


import xlrd, os, re, traceback
from config.settings import CASE_PATH, PARAMS_MAP,log


class ParamDeal():
    def read_excel(self, file_path):
        case_list = []
        try:
            book = xlrd.open_workbook(file_path)
            sheet = book.sheet_by_index(0)
            log.info("开始读取测试用例 %s" % file_path)
            for row in range(1, sheet.nrows):
                line = sheet.row_values(row)[1:8]
                line[2] = self.params_func(line[2]) # 参数化
                case_list.append(line)
                log.debug("成功读取第%d条用例 %s" % (row, line))
            log.info("测试用例读取完毕 %s" % file_path)
        except Exception as e:
            log.error("读取用例文件出错，文件名是:%s" % file_path)
            log.error("具体的错误信息是%s" % traceback.format_exc())
        return case_list

    def params_func(self, params):
        for map in PARAMS_MAP:
            if map in params:
                params = params.replace(map, PARAMS_MAP[map]())
        return params


if __name__ == "__main__":
    p = ParamDeal()
    for case in os.listdir(CASE_PATH):
        if re.search(r'\.xls$|\.xlsx$', case):
            my_case_path = os.path.join(CASE_PATH, case)
            res = p.read_excel(my_case_path)
    print(res)

