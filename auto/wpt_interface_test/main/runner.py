#-*- coding: utf-8 -*-
# @Time    : 2018/6/20 16:00
# @Author  : TangYong
# @File    : runner.py
# @Software: PyCharm
import os
import unittest
from fun import  public
import HTMLTestRunner
from  settings import config
from  case_suite import accept_input



class ExecuteCase(unittest.TestCase):

    def __init__(self):

        #取哪个层级中的测试用例
        # self.suite_case_dir = os.path.join(base_dir,'case_suite','po_manage')

       #执行哪个层级中的测试用例
        self.suite = unittest.TestSuite()

        #打开测试报告
        self.report_dir = open(config.report_info['report_dir'],'wb')

    def execute_suite_case(self):
        #添加需要执行的测试用例
        # self.suite.addTest(order.OrderManage('po_search'))


        # self.suite.addTests([test1.TestOne('test_one'),test1.TestOne('test_one'),test1.TestOne('test_two'),test1.TestOne('test_three'),test1.TestOne('test_four')])


        # 批量添加需执行的测试用例
        # self.suite.addTests([order.OrderManage('verify_login'),order.OrderManage('add1'),order.OrderManage('add2'),order.OrderManage('add3')])

        # 生成测试报告
        self.runner =HTMLTestRunner.HTMLTestRunner(
                                                     stream=self.report_dir,
                                                     verbosity=2,
                                                     title=config.report_info['report_title'],
                                                     description=config.report_info['report_detail']
        )
        self.runner.run(self.suite)
        self.report_dir.close()
        public.send_email()

    def exccute_disvover_case(self):
            self.discover_case_dir = os.path.join(config.base_dir, 'case_suite')
            self.discover = unittest.defaultTestLoader.discover(self.discover_case_dir, pattern='*.py')
             # 生成测试报告
            self.runner = HTMLTestRunner.HTMLTestRunner(stream=self.report_dir,
                                                        verbosity=1,
                                                        title=config.report_info['report_title'],
                                                        description=config.report_info['report_detail']
                                                            )

            result = self.runner.run(self.discover)

            print('测试成功数:',result.success_count)
            print('测试失败数:', result.failure_count)
            print('运行失败数:', result.error_count)


            self.report_dir.close()
            public.send_email()


