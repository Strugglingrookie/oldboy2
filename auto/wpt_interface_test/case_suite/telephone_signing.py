#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 16:56
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : telephone_signing.py
# @Software: PyCharm

import sys
import requests
import unittest
from settings import config
from fun import public
from fun import  wk_db_server

get_time = public.GetCurrentTime()

class TelephoneSigning(unittest.TestCase):
    '''  电话签约'''

    def test_tel_sign_admission(self):
        '''  电话签约准入 '''

        #当前电话签约条件下数据
        signing_data = { 'apply_status':'001','state': '0070', 'sub_state': '0001'} #,'operate_org_id':config.default_operate_org_id

        #请求准入数据
        signing_admission_data = {'operator': config.default_operation_name, 'systemId': '05', 'applyId': None}


        wk = wk_db_server.ApplyRepository()
        query_result = wk.handel_query('1',('apply_id','business_type'),**signing_data)

        if query_result is None:
            public.log_record('当前查询条件下没有待补件的数据',sys._getframe().f_lineno,query_result)
            return None

        signing_admission_data['applyId'] = query_result['apply_id']

        public.log_record('电话签约准入',sys._getframe().f_lineno,signing_admission_data)

        try:
            admission_result =requests.post(
                url=config.wk_detail_default_url,
                json=signing_admission_data
            )

            if admission_result.json():
               public.log_record('电话签约准入结果',sys._getframe().f_lineno,admission_result.json())

            else:
                public.log_record('查询进度响应结果', sys._getframe().f_lineno, admission_result.text)
                return None


        except Exception as e:
            public.log_record('电话签约准入',sys._getframe().f_lineno,e)
            return e

        self.assertEqual(admission_result.json()['code'], '000000', '电话签约准入结果')


    def test_tel_sign_apply(self):
        '''  电话签约申请 '''

        #当前电话签约条件下数据
        signing_data = { 'apply_status':'001','state': '0070', 'sub_state': '0001'} #'operate_org_id':config.default_operate_org_id

        #电话签约请求准入数据
        signing_admission_data = {'operator': config.default_operation_name, 'systemId': '05', 'applyId': None}

        #电话签约默认数据
        signing_default_apply_data = {
            'approvalComments':{
                'opinionType':'010'
            },
            'recordingInfo':[
                { "state":"0070",
                    "callCaller":"880633",
                    "callCallee":"13823712568",
                    "callUrl":"20170522-134150-880633-13823712568-1495431709.246927.WAV",
                    "operator":config.default_operation_name,
                    "inputDate":get_time.year_mont_day(),
                    "inputTime":get_time.complete_time()
                },
            ],
            "checkingInfo": {
                "sendTarget": "TO_XW"
            }
        }


        # 电话签约提交数据
        signing_apply_data = {
            'applyId': None,
            'applyType':None,
            'businessType':None,
            'state': '0070',
            'properties':'NOTXD',
            'operatorType': 'commitTask',
            'operator': config.default_operation_name,
        }

        #添加默认请求参数
        signing_apply_data.update(signing_default_apply_data)

        wk = wk_db_server.ApplyRepository()
        query_result = wk.handel_query('1',('apply_id','business_type','apply_type'),**signing_data)

        if query_result is None:
            public.log_record('当前查询【%s】下没有待补件的数据'%signing_data,sys._getframe().f_lineno,query_result)
            return None

        signing_admission_data['applyId'] = query_result['apply_id']

        public.log_record('电话签约准入',sys._getframe().f_lineno,signing_admission_data)


        admission_result =requests.post(
            url=config.wk_detail_default_url,
            json=signing_admission_data
        )
        signing_result = admission_result.json()

        if signing_result:
            public.log_record('电话签约准入结果:',sys._getframe().f_lineno,signing_result)

            signing_apply_data['applyId'] = query_result['apply_id']
            signing_apply_data['businessType'] = query_result['business_type']
            signing_apply_data['applyType'] = query_result['apply_type']

            signing_apply_data['customerInfo'] = signing_result['data']['customerInfoDTO']
            signing_apply_data['customerInfo']['permanentLocation'] = '01'
            signing_apply_data['customerInfo']['monthIncome'] = '10000'
            signing_apply_data['customerInfo']['childFlag'] = '0'


            # 删除多余的申请信息
            del signing_apply_data['customerInfo']['age']
            del signing_apply_data['customerInfo']['familyAddT']
            del signing_apply_data['customerInfo']['familyAddFr']
            del signing_apply_data['customerInfo']['familyAddInfo']


            public.log_record('提交电话签约请求数据',sys._getframe().f_lineno,signing_apply_data)

            try:
                submit_result = requests.post(
                    url=config.wk_submit_default_url,
                    json=signing_apply_data
                )
                if submit_result.json():
                    public.log_record('【%s】提交电话签约响应结果' % signing_apply_data['applyId'], sys._getframe().f_lineno, submit_result.json())
                    self.assertEqual(submit_result.json()['code'], '000000', '提交电话签约测试结果')

                else:
                    public.log_record('提交电话签约失败响应结果', sys._getframe().f_lineno, submit_result.text)
                    return None

            except Exception as e:
                public.log_record('提交电话签约', sys._getframe().f_lineno, e)
                return e



if __name__ == '__main__':
    unittest.main()

