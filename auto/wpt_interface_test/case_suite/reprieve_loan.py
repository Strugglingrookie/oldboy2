#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 8:23
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : reprieve_loan.py
# @Software: PyCharm


import sys
import requests
import unittest
from settings import config
from fun import public
from fun import  fatp_db_server


class ReprieveLoan(unittest.TestCase):
    '''  暂缓放款 '''

    def test_get_send_info(self):
        ''' 批量获取发标信息'''


        # 未记账/未暂缓状态数据
        putout_status = {
            'defer_pay_status': '0',
            'put_out_status': '0'
        }

        fatp = fatp_db_server.ApplyToContractRepository()

        query_result = fatp.handel_query(('t2.apply_serial_no'),**putout_status)

        if query_result is None:
           public.log_record('当前查询条件【%s】下未存在有效数据'%putout_status, sys._getframe().f_lineno, query_result)
           return None

        public.log_record('当前查询条件【%s】下查询结果数据' % putout_status, sys._getframe().f_lineno, query_result)

         #获取记账状态下的apply_id
        apply_id = query_result['apply_serial_no']

        #批量获取发标信息请求数据
        send_info_req_data = {
           'applyIdList':[apply_id]
        }
        public.log_record('批量获取发标信息请求数据' , sys._getframe().f_lineno, send_info_req_data)

        send_info_res_data = requests.post(
           url=config.wk_send_info_default_url,
           json=send_info_req_data
        )

        if send_info_res_data.json()['code']:
           public.log_record('批量获取发标信息响应数据', sys._getframe().f_lineno, send_info_res_data.text)
           self.assertEqual(send_info_res_data.json()['code'],'000000')
        else:
           public.log_record('批量获取发标信息失败响应数据', sys._getframe().f_lineno, send_info_res_data.text)

    def test_add_reprieve(self):
        ''' 添加暂缓'''

        # # 未记账/未暂缓状态数据
        putout_status = {
            'defer_pay_status':'0',
            'put_out_status':'0'
        }
        fatp = fatp_db_server.LoadApplyRepository()
        query_result = fatp.handel_query('1',('serial_no'),**putout_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下未存在有效数据' % putout_status, sys._getframe().f_lineno, query_result)
            return None

        public.log_record('当前查询条件【%s】下查询结果数据' % putout_status, sys._getframe().f_lineno, query_result)

        # 获取记账状态下的借据编号
        serial_no = query_result['serial_no']

        # 新增暂缓请求数据
        add_reprieve_req_data = {
            'loanNo': serial_no,
            'type':'0'
        }
        public.log_record('新增暂缓请求数据', sys._getframe().f_lineno, add_reprieve_req_data)

        add_reprieve_res_data = requests.post(
            url=config.fatp_notify_default_url,
            json=add_reprieve_req_data
        )

        if add_reprieve_res_data.json():
            public.log_record('新增暂缓响应数据', sys._getframe().f_lineno, add_reprieve_res_data.text)

            #检测资金数据库中暂缓状态是否为0(未暂缓)
            reprieve_status = fatp.handel_query('1',('defer_pay_status'),**{'serial_no':serial_no})

            public.log_record('检测资金数据库中暂缓状态是否为0(未暂缓)', sys._getframe().f_lineno,reprieve_status['defer_pay_status'])

            self.assertEqual(str(reprieve_status['defer_pay_status']),'0')


        else:
            public.log_record('新增暂缓失败响应数据', sys._getframe().f_lineno, add_reprieve_res_data.text)

    def test_submit_reprieve(self):
        ''' 提交暂缓'''

        # # 未记账/未暂缓状态数据
        putout_status = {
            'defer_pay_status': '0',
            'put_out_status': '0'
        }
        fatp = fatp_db_server.LoadApplyRepository()
        query_result = fatp.handel_query('1', ('serial_no'), **putout_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下未存在有效数据' % putout_status, sys._getframe().f_lineno, query_result)
            return None

        public.log_record('当前查询条件【%s】下查询结果数据' % putout_status, sys._getframe().f_lineno, query_result)

        # 获取记账状态下的借据编号
        serial_no = query_result['serial_no']

        # 提交暂缓请求数据
        submit_reprieve_req_data = {
            'loanNo': serial_no,
            'type': '1'
        }
        public.log_record('提交暂缓请求数据', sys._getframe().f_lineno, submit_reprieve_req_data)

        submit_reprieve_res_data = requests.post(
            url=config.fatp_notify_default_url,
            json=submit_reprieve_req_data
        )

        if submit_reprieve_res_data.json():
            public.log_record('提交暂缓响应数据', sys._getframe().f_lineno, submit_reprieve_res_data.text)

            # 检测资金数据库中暂缓状态是否为0(已暂缓)
            reprieve_status = fatp.handel_query('1', ('defer_pay_status'), **{'serial_no': serial_no})

            public.log_record('检测资金数据库中暂缓状态是否为1(已暂缓)', sys._getframe().f_lineno, reprieve_status['defer_pay_status'])

            self.assertEqual(str(reprieve_status['defer_pay_status']), '1')


        else:
            public.log_record('提交暂缓失败响应数据', sys._getframe().f_lineno, submit_reprieve_res_data.text)

    def test_cancel_reprieve(self):
        ''' 取消暂缓'''

         # 未记账/已暂缓状态数据
        putout_status = {
            'defer_pay_status': '1',
            'put_out_status': '0'
        }
        fatp = fatp_db_server.LoadApplyRepository()
        query_result = fatp.handel_query( ('t1.serial_no'), **putout_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下未存在有效数据' % putout_status, sys._getframe().f_lineno, query_result)
            return None

        public.log_record('当前查询条件【%s】下查询结果数据' % putout_status, sys._getframe().f_lineno, query_result)

        # 获取借据编号
        serial_no = query_result['serial_no']

        # 取消暂缓请求数据
        cancel_reprieve_req_data = {
            'loanNo': serial_no,
            'type': '0'
        }
        public.log_record('取消暂缓请求数据', sys._getframe().f_lineno, cancel_reprieve_req_data)

        cancel_reprieve_res_data = requests.post(
            url=config.fatp_notify_default_url,
            json=cancel_reprieve_req_data
        )

        if cancel_reprieve_res_data.json():
            public.log_record('取消暂缓请响应数据', sys._getframe().f_lineno, cancel_reprieve_res_data.text)

            # 检测资金数据库中暂缓状态是否为0(未暂缓)
            reprieve_status = fatp.handel_query('1', ('defer_pay_status'), **{'serial_no': serial_no})

            public.log_record('检测资金数据库中暂缓状态是否为0(未暂缓)', sys._getframe().f_lineno, reprieve_status['defer_pay_status'])

            self.assertEqual(str(reprieve_status['defer_pay_status']), '0')

        else:
            public.log_record('取消暂缓失败响应数据', sys._getframe().f_lineno, cancel_reprieve_res_data.text)

    def test_stop_apply(self):
        ''' 终止申请'''

        # 未记账/未暂缓状态数据
        putout_status = {
            'defer_pay_status': '0',
            'put_out_status': '0'
        }
        fatp = fatp_db_server.LoadApplyRepository()
        query_result = fatp.handel_query('1', ('serial_no'), **putout_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下未存在有效数据' % putout_status, sys._getframe().f_lineno, query_result)
            return None

        public.log_record('当前查询条件【%s】下查询结果数据' % putout_status, sys._getframe().f_lineno, query_result)

        # 获取借据编号
        serial_no = query_result['serial_no']

        # 终止申请请求数据
        stop_apply_req_data = {
            'loanNo': serial_no,
            'type': '1'
        }
        public.log_record('终止申请请求数据', sys._getframe().f_lineno, stop_apply_req_data)

        stop_apply_res_data = requests.post(
            url=config.fatp_notify_default_url,
            json=stop_apply_req_data
        )

        if stop_apply_res_data.json():
            public.log_record('终止申请响应数据', sys._getframe().f_lineno, stop_apply_res_data.text)

            # 检测资金数据库中暂缓状态是否为1(已暂缓)
            reprieve_status = fatp.handel_query('1', ('defer_pay_status'), **{'serial_no': serial_no})

            public.log_record('检测资金数据库中暂缓状态是否为1(已暂缓)', sys._getframe().f_lineno, reprieve_status['defer_pay_status'])

            self.assertEqual(str(reprieve_status['defer_pay_status']), '1')

        else:
            public.log_record('终止申请失败响应数据', sys._getframe().f_lineno, stop_apply_res_data.text)

    def test_cancel_stop_apply(self):
        ''' 取消终止申请'''

        # 未记账/未暂缓状态数据
        putout_status = {
            'defer_pay_status': '1',
            'put_out_status': '0'
        }
        fatp = fatp_db_server.LoadApplyRepository()
        query_result = fatp.handel_query('1', ('serial_no'), **putout_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下未存在有效数据' % putout_status, sys._getframe().f_lineno, query_result)
            return None

        public.log_record('当前查询条件【%s】下查询结果数据' % putout_status, sys._getframe().f_lineno, query_result)

        # 获取借据编号
        serial_no = query_result['serial_no']

        # 取消终止申请请求数据
        cancel_stop_req_data = {
            'loanNo': serial_no,
            'type': '0'
        }
        public.log_record('取消终止申请请求数据', sys._getframe().f_lineno, cancel_stop_req_data)

        cancel_stop_res_data = requests.post(
            url=config.fatp_notify_default_url,
            json=cancel_stop_req_data
        )

        if cancel_stop_res_data.json():
            public.log_record('取消终止申请响应数据', sys._getframe().f_lineno, cancel_stop_res_data.text)

            # 检测资金数据库中暂缓状态是否为0(未暂缓)
            reprieve_status = fatp.handel_query('1', ('defer_pay_status'), **{'serial_no': serial_no})

            public.log_record('检测资金数据库中暂缓状态是否为1(未暂缓)', sys._getframe().f_lineno, reprieve_status['defer_pay_status'])

            self.assertEqual(str(reprieve_status['defer_pay_status']), '0')

        else:
            public.log_record('取消终止申请失败响应数据', sys._getframe().f_lineno, cancel_stop_res_data.text)

    def test_stop_loan(self):
        ''' 终止放款'''

        # 未记账/已暂缓状态数据
        putout_status = {
            'defer_pay_status': '1',
            'put_out_status': '0'
        }
        fatp = fatp_db_server.LoadApplyRepository()
        query_result = fatp.handel_query('1', ('serial_no'), **putout_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下未存在有效数据' % putout_status, sys._getframe().f_lineno, query_result)
            return None

        public.log_record('当前查询条件【%s】下查询结果数据' % putout_status, sys._getframe().f_lineno, query_result)

        # 获取借据编号
        serial_no = query_result['serial_no']

        # 终止放款请求数据
        stop_loan_req_data = {
            'loanNo': serial_no,
            'type': '2'
        }
        public.log_record('终止放款请求数据', sys._getframe().f_lineno, stop_loan_req_data)

        stop_loan_res_data = requests.post(
            url=config.fatp_notify_default_url,
            json=stop_loan_req_data
        )

        if stop_loan_res_data.json():
            public.log_record('终止放款响应数据', sys._getframe().f_lineno, stop_loan_res_data.text)

            # 检测资金数据库中暂缓状态是否为2(已终止)
            reprieve_status = fatp.handel_query('1', ('defer_pay_status'), **{'serial_no': serial_no})

            public.log_record('检测资金数据库中暂缓状态是否为2(已终止)', sys._getframe().f_lineno, reprieve_status['defer_pay_status'])

            self.assertEqual(str(reprieve_status['defer_pay_status']), '2')

        else:
            public.log_record('终止放款失败响应数据', sys._getframe().f_lineno, stop_loan_res_data.text)

    def test_cancel_stop_loan(self):
        ''' 取消终止放款'''

        # 未记账/已暂缓状态数据
        putout_status = {
            'defer_pay_status': '1',
            'put_out_status': '0'
        }
        fatp = fatp_db_server.LoadApplyRepository()
        query_result = fatp.handel_query('1', ('serial_no'), **putout_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下未存在有效数据' % putout_status, sys._getframe().f_lineno, query_result)
            return None

        public.log_record('当前查询条件【%s】下查询结果数据' % putout_status, sys._getframe().f_lineno, query_result)

        # 获取借据编号
        serial_no = query_result['serial_no']

        # 取消终止放款请求数据
        cancel_stop_req_data = {
            'loanNo': serial_no,
            'type': '1'
        }
        public.log_record('取消终止放款请求数据', sys._getframe().f_lineno, cancel_stop_req_data)

        stop_loan_res_data = requests.post(
            url=config.fatp_notify_default_url,
            json=cancel_stop_req_data
        )

        if stop_loan_res_data.json():
            public.log_record('取消终止放款响应数据', sys._getframe().f_lineno, stop_loan_res_data.text)

            # 检测资金数据库中暂缓状态是否为1(已暂缓)
            reprieve_status = fatp.handel_query('1', ('defer_pay_status'), **{'serial_no': serial_no})

            public.log_record('检测资金数据库中暂缓状态是否为1(已暂缓)', sys._getframe().f_lineno, reprieve_status['defer_pay_status'])

            self.assertEqual(str(reprieve_status['defer_pay_status']), '1')

        else:
            public.log_record('取消终止放款失败响应数据', sys._getframe().f_lineno, stop_loan_res_data.text)


if __name__ == '__main__':
    unittest.main()