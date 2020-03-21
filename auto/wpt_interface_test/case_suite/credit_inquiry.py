#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 9:35
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : credit_inquiry.py
# @Software: PyCharm
import sys
import  unittest
from fun import public

class CreditInquiry(unittest.TestCase):
    '''  征信查询'''

    def test_inquiry_credit(self):
        '''  查询征信报告'''

        handel_credit = public.CreditInquiry()

        inquiry_credit = handel_credit.save_to_mongoDB()

        if inquiry_credit:
            public.log_record('查询征信响应数据:', sys._getframe().f_lineno, inquiry_credit)
            self.assertEqual(str(inquiry_credit['code']),'0','查询征信')
        else:
            public.log_record('查询征信失败响应数据:', sys._getframe().f_lineno, inquiry_credit)

    def test_fetch_credit_result(self):
        '''  查询征信结果 '''

        handel_credit_result = public.CreditInquiry(flag=True)

        get_inquiry_credit_result = handel_credit_result.fetch_result()


        if get_inquiry_credit_result:
            public.log_record('获取征信结果响应数据:', sys._getframe().f_lineno, get_inquiry_credit_result)
            self.assertGreater(int(get_inquiry_credit_result['data']['totalCount']), 0, '查询征信结果')
        else:
            public.log_record('获取征信结果失败响应数据:', sys._getframe().f_lineno, get_inquiry_credit_result)


if __name__ == '__main__':
    unittest.main()