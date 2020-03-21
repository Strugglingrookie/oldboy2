#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 18:25
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : schedule_query.py
# @Software: PyCharm

import sys
import unittest
import requests
from fun import public
from fun import wk_db_server
from fun import bms_db_server
from settings import config


class ScheduleQuery(unittest.TestCase):
    '''  进度查询 '''

    def test_query_schedule(self):
        ''' 查询进度结果'''

        #查询进度请求参数
        query_data = {
            "operateOrgId": [config.default_operate_org_id],
            "operator": config.default_operation_name,
            "pageSize": 10,
            "pageNum": 1
        }
        public.log_record('查询进度请求数据',sys._getframe().f_lineno,query_data)

        try:
            query_result = requests.post(
                url=config.wk_schedule_default_url,
                json=query_data
            )

            if query_result.json()['data']:
                schedule_result = query_result.json()
                public.log_record('查询进度响应结果',sys._getframe().f_lineno,query_result.text)
                self.assertGreater(int(schedule_result['data']['count']), 0, '进度查询结果')

            else:
                public.log_record('查询进度响应结果', sys._getframe().f_lineno, query_result.text)
                return None

        except Exception as e:
            public.log_record('查询进度',sys._getframe().f_lineno,e)

    def test_examine_schedule_detail(self):
        ''' 进度详情'''

        wk = wk_db_server.ApplyRepository()

        # 申请中状态的数据
        query_data = {'apply_status': '001',  'operate_org_id': config.default_operate_org_id}

        # 获取待补件apply_id
        query_result = wk.handel_query(1, ('apply_id'), **query_data)

        # 查看进度详情请求参数
        detail_data = {
            "operator": config.default_operation_name,
            "applyId": query_result['apply_id'],
            "systemId": "05",
        }

        public.log_record('查看进度详情请求数据', sys._getframe().f_lineno, detail_data)

        try:
            query_result = requests.post(
                url=config.wk_detail_default_url,
                json=detail_data
            )

            if query_result.json()['code']:
                schedule_detail_result = query_result.json()
                public.log_record('查询进度详情响应结果', sys._getframe().f_lineno, query_result.text)
                self.assertEqual(schedule_detail_result['code'], '000000', '查询进度详情结果')

            else:
                public.log_record('查询进度详情响应结果', sys._getframe().f_lineno, query_result.text)
                return None

        except Exception as e:
            public.log_record('查看进度详情', sys._getframe().f_lineno, e)

    def test_cancel(self):
        '''  取消任务'''

        wk = wk_db_server.ApplyRepository()

        #查询预审面签数据  visa_interview
        query_data = {
            'state': '0017',
            'apply_status': '001',
            'sub_state': '0001',
            'prev_state':'0010',
            'apply_source':'B_PROJECT_INLET',
            'operate_org_id': config.default_operate_org_id
        }
        query_result = wk.handel_query('1',('apply_id'),**query_data)

        if query_result is None:
            public.log_record('当前环境下不存在预审面签数据', sys._getframe().f_lineno, query_result)
            return None

        #取消面签请求数据
        visa_interview_req_data = {
            'applyId':query_result['apply_id'],
            'operatorId':config.wind_control
        }
        public.log_record('取消面签请求数据', sys._getframe().f_lineno, visa_interview_req_data)

        visa_interview_res_data = requests.post(
            url=config.wk_cancel_default_url,
            json=visa_interview_req_data
        )
        if visa_interview_res_data.json()['code']:
            public.log_record('取消面签响应数据', sys._getframe().f_lineno, visa_interview_res_data.text)
            self.assertEqual(visa_interview_res_data.json()['code'],'000000')

        else:
            public.log_record('取消面签响应数据', sys._getframe().f_lineno, visa_interview_res_data.text)
            return None

    def test_task_adjust(self):
        ''' 任务调整'''

        wk = wk_db_server.ApplyRepository()
        bms = bms_db_server.SellerRepository()

        # 查询现场调查状态的数据
        query_data = {
            'state':'0060',
            'apply_status': '001',
            'sub_state':'0016',
            'operate_org_id': config.default_operate_org_id
        }

        # 获取现调apply_id和现调人员姓名
        query_result = wk.handel_query(1, ('apply_id','operate_user_id'), **query_data)

        if query_result is  None:

            #查找贷款审批阶段的申请
            approve_req_data = {
                'apply_status':'001',
                'state':'0060',
                'prev_state':'0050',
                'sub_state':'0001',
                'operate_org_id':config.default_operate_org_id
            }
            approve_res_data = wk.handel_query('1',('apply_id','state_operator','operate_user_id'),**approve_req_data)


            #获取当前流程节点操作人和apply_id
            apply_id = approve_res_data['apply_id']
            operate_user_id = approve_res_data['operate_user_id']
            state_operator = approve_res_data['state_operator']

            # 悟空内部审批任务调整(默认给sunyui)
            if state_operator == 'virtualuser':
                state_operator = 'SUNYUI'
                requests.post(
                    url=config.wk_approval_task_adjust_default_url,
                    json={
                        "adjustTasks":[
                            {
                                "applyId":apply_id,
                                "operatorId":"LUZHONG",
                                "state":"0060",
                                "subState":"0001",
                                "adjustToUserId":"SUNYUI",
                                "adjustToUserName":"孙雨",
                                "operatorName":"卢仲"
                            }
                        ]
                    }
                )

            #使用当前流程节点人登录,获取token,然后分发现场调查
            login_req_data = {
                'username':state_operator,
                'password':'96qyVNn/porDY',
                'socketId':'ERf8Ij6boKiKeF3gAAAC',
            }
            public.log_record('登录WK请求信息', sys._getframe().f_lineno, login_req_data)

            login_res_data = requests.post(
                url=config.wk_login_default_url,
                json=login_req_data
            )

            if login_res_data.json():
                public.log_record('登录WK结果信息', sys._getframe().f_lineno, login_res_data.text)
                login_token = login_res_data.json()['data']['accToken']

            else:
                public.log_record('登录WK失败', sys._getframe().f_lineno, login_res_data.text)
                return None

            # 下发现调
            signal_req_data = {
                'applyId': apply_id,
                'state': "0060",
                'toState': '0016',
                'applyType': "NormalApply",
                'actionDetail': "SITE_SURVEY",
                'token': login_token
            }
            public.log_record('WK下发现调请求数据', sys._getframe().f_lineno, signal_req_data)

            signal_res_data = requests.post(
                url=config.wk_signal_default_url,
                data=signal_req_data
            )

            if signal_res_data.json():
                if signal_res_data.json()['code'] == '000000':
                    public.log_record('WK下发现调响应数据', sys._getframe().f_lineno, signal_res_data.text)

                else:
                    public.log_record('WK下发现调失败', sys._getframe().f_lineno, signal_res_data.text)
                    return None

            else:
                public.log_record('WK下发现调失败', sys._getframe().f_lineno, signal_res_data.text)
                return  None

        else:
            apply_id = query_result['apply_id']
            operate_user_id = query_result['operate_user_id']

        #查看现调人员是否有现调权,如果有(1),将其修改为无(0)
        scene = bms.handel_query(operate_user_id)
        if scene['is_scene'] == '1':
            bms.handel_update(operate_user_id,'0')

        #查看并获取指定机构下具有现调权限人员信息
        seller_info = bms.query_seller_depart_unit(config.default_org_id)

        #作业平台任务调整请求参数
        task_adjust_req_data = {
            'applyId':apply_id,
            'operatorId':scene['user_id'],
            'adjustToUserId':seller_info['user_id']
        }
        public.log_record('作业平台任务调整请求数据', sys._getframe().f_lineno, task_adjust_req_data)

        task_adjust_res_data = requests.post(
            url=config.wk_task_adjust_default_url,
            json=task_adjust_req_data
        )

        if task_adjust_res_data.json()['code']:
            public.log_record('作业平台任务调整响应数据', sys._getframe().f_lineno, task_adjust_res_data.text)

            self.assertEqual(task_adjust_res_data.json()['code'],'000000')

        else:
            public.log_record('作业平台任务调整响应数据', sys._getframe().f_lineno, task_adjust_res_data.text)
            return None


if __name__ == '__main__':
    unittest.main()

