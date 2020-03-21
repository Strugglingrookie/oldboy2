#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 9:48
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : repair_matter.py
# @Software: PyCharm

import sys
import  time
import requests
import  unittest
from  fun import public
from fun import wk_db_server
from settings import  config


class RepairMatter(unittest.TestCase):
    '''  补件处理'''

    def test_repair_admission(self):
        '''  补件准入'''

        start_time = time.time()

        #提交申请单，悟空改变申请状态
        wk = public.WkEvent()
        submit_result = wk.signal()

        handle = wk_db_server.ApplyRepository()

        try:
            # 获取待补件apply_id
            apply_id = submit_result['data']['applyId']

            # 设置补件准入的参数
            req_data = {
                "operator": config.default_operation_name,
                "applyId": apply_id,
                "systemId": "05"
            }
            public.log_record('补件处理请求数据:', sys._getframe().f_lineno, req_data)

            response_result = requests.post(
                url=config.wk_detail_default_url,
                json=req_data,
            )

            while not response_result:
                if time.time() - start_time > 15:
                    public.log_record('【%s】准入超时' % apply_id, sys._getframe().f_lineno, response_result.text)
                    return  '补件准入超时'

            public.log_record('【%s】补件处理响应数据:' % apply_id, sys._getframe().f_lineno, response_result.text)
            self.assertEqual(response_result.json()['code'], '000000', '准入补件')

        except  Exception as e:
            public.log_record('获取待补件【%s】'%apply_id,sys._getframe().f_lineno,e)

        #删除数据
        handle.handel_delete(apply_id)
        # wk.recover_status(apply_id)



    def test_repair_apply(self):
        '''  补件提交'''

        #补件申请数据
        repair_apply_data = {}

        start_time =time.time()

        handle = wk_db_server.ApplyRepository()

        #补件状态的数据
        signal_data = { 'apply_status':'001','state': '0050', 'sub_state': '0015','operate_org_id':config.default_operate_org_id}

        # 获取待补件apply_id
        query_result = handle.handel_query(1,('apply_id','business_type'),**signal_data)


        if query_result == None:
            public.log_record('当前查询条件【%s】未存在补件数据' % signal_data, sys._getframe().f_lineno, query_result)
            return None

        apply_id = query_result['apply_id']
        business_type = query_result['business_type']



        # 设置补件准入的参数
        repair_admission_data = {
            "operator": config.default_operation_name,
             "applyId": apply_id,
            "systemId": "05"
        }
        public.log_record('补件准入请求数据:', sys._getframe().f_lineno, repair_admission_data)


        repair_admission = requests.post(
            url=config.wk_detail_default_url,
            json=repair_admission_data,
        )
        admission_result = repair_admission.json()


        while not admission_result:
            if time.time() - start_time > 15:
                public.log_record('【%s】准入超时' % apply_id, sys._getframe().f_lineno, admission_result)
                return None

        public.log_record('【%s】补件准入响应数据' % apply_id, sys._getframe().f_lineno, admission_result)


        public.log_record('获取待补件【%s】' % apply_id, sys._getframe().f_lineno, admission_result)

        public.log_record('提交补件【%s】数据' % apply_id, sys._getframe().f_lineno, admission_result)

        #从准入结果中获取准入申请数据
        repair_apply_data['identityInfo'] = admission_result['data']['identityInfoDTO']
        repair_apply_data['customerInfo'] = admission_result['data']['customerInfoDTO']
        repair_apply_data['workInfo'] = admission_result['data']['workInfoDTO']
        repair_apply_data['contactsInfo'] = admission_result['data']['contactsInfoDTO']
        repair_apply_data['borrowingMatters'] = admission_result['data']['borrowingMattersDTO']
        repair_apply_data['notCustomerMatters'] = admission_result['data']['notCustomerMattersDTO']
        print('repair_apply_data:', repair_apply_data)

       #从数据库获取补件影像
        columns = ('attachment_no','attachment_type','attachment_real_file_name','input_user_id','create_time')
        get_images = public.wk_db_server.AttachmentRepository()
        images = get_images.handel_query(columns,**{'apply_id':apply_id})

        for image in images:
            image['attachmentNo'] = image['attachment_no']
            del image['attachment_no']

            image['attachmentType'] = image['attachment_type']
            del image['attachment_type']

            image['attachmentRealFileName'] = image['attachment_real_file_name']
            del image['attachment_real_file_name']

            image['operator'] = image['input_user_id']
            del image['input_user_id']



            image['inputDate'] = str(image['create_time']).strip()[0:10]
            image['inputTime'] = str(image['create_time']).strip()[11:19]

            del image['create_time']

        repair_apply_data['imageInfo'] = images

        #删除多余的申请信息
        del repair_apply_data['customerInfo']['age']
        del repair_apply_data['customerInfo']['familyAddT']
        del repair_apply_data['customerInfo']['familyAddFr']
        del repair_apply_data['customerInfo']['familyAddInfo']

        del repair_apply_data['identityInfo']['idSamId']

        del repair_apply_data['workInfo']['workAddT']
        del repair_apply_data['workInfo']['workAddFr']

        del repair_apply_data['borrowingMatters']['loanPurpose']
        del repair_apply_data['notCustomerMatters']['crChannelName']

        repair_apply_data['identityInfo']['idSex'] = '男'
        repair_apply_data['customerInfo']['childFlag'] = '0'
        repair_apply_data['notCustomerMatters']['isCertifition'] = '0'
        repair_apply_data['notCustomerMatters']['operateAssistantUserName'] = 'test'
        repair_apply_data['borrowingMatters']['socialCreditCode'] = '51370181MJD7731881'

        if business_type == config.business_type['NBTS'][0]:
            repair_apply_data['borrowingMatters']['nbtsEleAccount'] = '578812638578812638123'
        else:
            del repair_apply_data['borrowingMatters']['nbtsEleAccount']

        # print('repair_apply_data:', repair_apply_data)

        # 提交补件专有标识数据
        apply_special_data = {
            'applyType': 'NormalApply',
            'operatorType': 'backApproval',
            'state': '0015',
            'operator': config.default_operation_name,
            'properties': 'NOTXD',
            'applyId': apply_id,
            'businessType': business_type
        }

        repair_apply_data.update(apply_special_data)

        public.log_record('【%s】提交补件申请信息' % apply_id, sys._getframe().f_lineno, repair_apply_data)

        apply_result = requests.post(
            url=config.wk_submit_default_url,
            json=repair_apply_data
        )

        public.log_record('【%s】提交补件响应结果' % apply_id, sys._getframe().f_lineno, apply_result.json())

        self.assertEqual(apply_result.json()['code'], '000000', '提交补件测试结果')










#
# suite = unittest.TestSuite()
# suite.addTest(RepairMatter('test_repair_apply'))
# runner = unittest.TextTestRunner()
# runner.run(suite)