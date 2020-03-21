#-*- coding: utf-8 -*-
# @Time    : 2018/6/21 11:21
# @Author  : TangYong
# @File    : execute_case.py
# @Software: PyCharm

import  sys
import time
from  settings import config
from main.runner import ExecuteCase
sys.path.append(config.base_dir)

if __name__  == '__main__':
    runner = ExecuteCase()
    # runner.execute_suite_case()
    runner.exccute_disvover_case()
    #
    # for i in range(2):
    #         print('开始执行...')
    #
    #         runner = ExecuteCase()
    #           # runner.execute_suite_case()
    #         runner.exccute_disvover_case()


    # for i in range(3):
    #     runner = ExecuteCase()
    #     # runner.execute_suite_case()
    #     runner.exccute_disvover_case()
