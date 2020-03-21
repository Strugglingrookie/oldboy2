#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 16:48
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : base.py
# @Software: PyCharm

import sys
import time
import json
import requests
import unittest
from settings import config
from fun import public
from fun import  wk_db_server
from fun import  cma_db_server

for i in range(3):
    get_user_info = public.get_user_auth_info()
    if get_user_info[0] != '默认容错用户信息':
        break

def cma_recommend():
    #根据客户的身份证号获取从CMA获取最近有效的推荐编码以及推荐人信息
    import time
    import hashlib
    import uuid
    app_id = 'I0007'
    cam_key = config.cme_key
    random_str =str( uuid.uuid1())
    serial_no = app_id+random_str
    timestamp = str(time.time())
    md5 = hashlib.md5()
    sign = ''.join([app_id,serial_no,timestamp,cam_key])
    md5.update(sign.encode('utf-8'))
    signature = (md5.hexdigest().upper())

    cma = cma_db_server.UserToRcmdRecord()

    #查询客户身份证号
    query_result = cma.handel_query(('t2.cert_id'))
    if query_result is None:
        public.log_record('根据身份证号查询最近一笔有效推荐人信息无数据', sys._getframe().f_lineno, query_result)
        return  None
    base64_cert_no = query_result['cert_id']

    #对身份证进行base64解密
    base64 = public.EncryptAndDecrypt()
    base64_decode_cert_no = base64.base64_decrypt(base64_cert_no)

    #对身份证进行aes加密
    aes = public.EncryptAndDecrypt(key=config.cme_key,iv=config.cma_iv)
    aes_encode_cert_no = aes.aes_encrypt(base64_decode_cert_no)


    recommend_req_data = {}
    # 根据身份证号查询最近一笔有效推荐人信息请求数据
    valid_recommend_req_data = {
        'certId': aes_encode_cert_no,
    }
    recommend_req_data.update(valid_recommend_req_data)

    valid_recommend_req_header = {
        'AppID':app_id,
        'Serial-No':serial_no,
        'Timestamp':timestamp,
        'Signature':signature
    }
    recommend_req_data.update(valid_recommend_req_header)

    public.log_record('根据身份证号查询最近一笔有效推荐人信息请求数据', sys._getframe().f_lineno, recommend_req_data)

    valid_recommend_res_data = requests.post(
       url= config.cma_valid_recommend_default_url,
       json=valid_recommend_req_data,
       headers={
            'AppID':app_id,
            'Serial-No':serial_no,
            'Timestamp':timestamp,
            'Signature':signature
        }
    )
    if valid_recommend_res_data.json():
        print('valid_recommend_res_data.json():',valid_recommend_res_data.json())
        return valid_recommend_res_data.json()
    else:
        public.log_record('根据身份证号查询最近一笔有效推荐人信息失败响应数据', sys._getframe().f_lineno, valid_recommend_res_data.text)
        return None

class LoginLogout:

    def login(self):
        all_req_data = {}
        login_req_data = {
            'userId': config.default_operation_name,
            'password': '96qyVNn/porDY',
        }
        all_req_data.update(login_req_data)

        login_req_header =  {
            'serialno':'1098293248392',
            'systemId':'WPT'
        }
        all_req_data.update(login_req_header)

        public.log_record('登录请求数据', sys._getframe().f_lineno, all_req_data)

        login_res_data = requests.post(
            url=config.plms_login_default_url,
            json=login_req_data,
            headers = login_req_header
        )
        if login_res_data.json()['retCode']:
            return login_res_data.json()

        else:
            public.log_record('登录请求败响应数据', sys._getframe().f_lineno, login_res_data.text)
            return None

    def logout(self):
        all_req_data = {}
        token = self.login()

        #退出登录请求数据
        logout_req_data = token['data']['accToken']
        all_req_data.update({'accToken':logout_req_data})

        #退出登录请求头
        logout_req_header = {
        'serialno':'1098293248392',
        'accToken':logout_req_data,
        'systemId':'WPT'
    }
        all_req_data.update(logout_req_header)

        #退出登录请求数据
        public.log_record('退出登录请求数据', sys._getframe().f_lineno, all_req_data)

        logout_res_data = requests.post(
            url=config.plms_logout_default_url,
            json={'accToken':logout_req_data},
            headers = logout_req_header
        )
        if logout_res_data.json()['retCode']:
            return logout_res_data.json()
        else:
            public.log_record('退出登录失败响应数据', sys._getframe().f_lineno, logout_res_data.text)


class Base(unittest.TestCase):
    '''  基础接口'''

    def test_login(self):
        '''  登录认证'''


        login = LoginLogout()
        login_res_data = login.login()

        if login_res_data['retCode']:
            public.log_record('登录请求应数据', sys._getframe().f_lineno, login_res_data)
            self.assertEqual(login_res_data['retCode'], '000000')
        else:
            public.log_record('登录请求败响应数据', sys._getframe().f_lineno, login_res_data)

    def test_logout(self):
        '''  退出登录'''

        logout = LoginLogout()
        logout_res_data = logout.logout()

        if logout_res_data['retCode']:
            self.assertEqual(logout_res_data['retCode'], '000000')
        else:
            public.log_record('退出登录请求败响应数据', sys._getframe().f_lineno, logout_res_data)

    def test_get_apply_id(self):
        '''  获取空白申请编号'''

        apply_id_res = requests.get(url=config.wk_get_apply_id_default_url)
        if apply_id_res.json()['code']:
            public.log_record('获取空白申请编号响应数据', sys._getframe().f_lineno, apply_id_res.text)
            self.assertEqual(apply_id_res.json()['code'],'000000')
        else:
            public.log_record('获取空白申请编号失败响应数据', sys._getframe().f_lineno, apply_id_res.text)

    def test_real_auth(self):
        '''  实名认证'''

        AES = public.EncryptAndDecrypt(key='abcdefghij123456',iv='0102030405060708')

        time_format = public.ChangeTimeFormat()
        timestamp = time_format.change_timestamp(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

        #实名认证请求数据
        real_auth_req_data ={
        'timeStamp':timestamp,
        'certId':get_user_info[1],
        'source':'shizuishan',
        'inputType':'NOTXD',
        'isCompany':'false'
        }
        public.log_record('实名认证请数据,加密前:', sys._getframe().f_lineno, real_auth_req_data)

        encode_data = AES.aes_encrypt(json.dumps(real_auth_req_data))
        public.log_record('实名认证请求数据,加密后:', sys._getframe().f_lineno, encode_data)

        real_auth_res_data = requests.post(
            url=config.hp_real_auth_default_url,
            json={
                'json':encode_data
            }
        )
        if real_auth_res_data.json():
            public.log_record('实名认证响应数据:',sys._getframe().f_lineno,real_auth_res_data.text)
            self.assertEqual(str(real_auth_res_data.json()['authed']).lower(), 'true')

        else:
            public.log_record('实名认证失败响应数据:', sys._getframe().f_lineno, real_auth_res_data.text)

    def test_natural_person(self):
        '''  自然人检测'''

        #自然人检测请求数据
        naturalperson_req_data = {
            "certId":get_user_info[1],
            "source":"WPT"
        }
        public.log_record('自然人检测请求数据', sys._getframe().f_lineno, naturalperson_req_data)

        naturalperson_res_data = requests.post(
            url=config.inner_naturalperson_default_url,
            json=naturalperson_req_data
        )

        if naturalperson_res_data.json()['code']:
            public.log_record('自然人检测响应数据', sys._getframe().f_lineno, naturalperson_res_data.text)
            self.assertEqual(str(naturalperson_res_data.json()['code']),'0')
        else:
            public.log_record('自然人检测失败响应数据', sys._getframe().f_lineno, naturalperson_res_data.text)

    def test_XD_type(self):
        '''  识别续贷类型'''

        # 识别续贷请求数据
        XD_req_data = {
            "certId": ' 451229198910108833',  # user_info[1],
        }
        public.log_record('识别续贷客户类型请求数据', sys._getframe().f_lineno, XD_req_data)

        XD_res_data = requests.post(
            url=config.lcrm_XD_type_default_url,
            json=XD_req_data
        )
        if XD_res_data.json()['retCode']:
            public.log_record('识别续贷客户类型响应数据',sys._getframe().f_lineno,XD_res_data.text)
            self.assertEqual(XD_res_data.json()['retCode'],'000000')
        else:
            public.log_record('识别续贷客户类型失败响应数据', sys._getframe().f_lineno, XD_res_data.text)

    def test_batch_query_seller(self):
        '''  批量查询营销人员信息 '''

        #批量查询营销人员请求数据
        batch_req_data = {
            'sellerIds':config.seller_id_list
        }
        public.log_record('批量查询营销人员请求数据', sys._getframe().f_lineno, batch_req_data)

        batch_res_data = requests.post(
            url=config.bms_seller_list_default_url,
            json=batch_req_data
        )

        if batch_res_data.json()['retCode']:
            public.log_record('批量查询营销人员响应数据', sys._getframe().f_lineno, batch_res_data.text)
            self.assertEqual(batch_res_data.json()['retCode'],'000000')
        else:
            public.log_record('批量查询营销人员失败响应数据', sys._getframe().f_lineno, batch_res_data.text)

    def test_flag_isLock(self):
        '''  判断是否锁定 '''

        #根据身份证号判断是否锁定请求数据
        isLcok_req_data = {
            'systemId':'WPT',
            'certId':'451229198910108833',#user_info[1]
        }
        public.log_record('根据身份证号判断是否锁定请求数据', sys._getframe().f_lineno, isLcok_req_data)

        isLcok_res_data = requests.post(
            url =config.lcrm_is_lock_default_url,
            json=isLcok_req_data
        )
        if isLcok_res_data.json()['retCode']:
            public.log_record('根据身份证号判断是否锁定响应数据', sys._getframe().f_lineno, isLcok_res_data.text)
            self.assertEqual(isLcok_res_data.json()['retCode'],'000000')
        else:
            public.log_record('根据身份证号判断是否锁定失败响应数据', sys._getframe().f_lineno, isLcok_res_data.text)

    def test_query_valid_recommend(self):
        '''  查询有效推荐 '''

        recommend_info = cma_recommend()
        if recommend_info:
            public.log_record('根据身份证号查询最近一笔有效推荐人信息响应数据', sys._getframe().f_lineno, recommend_info)
            self.assertEqual(recommend_info['code'],'000000')

        else:
            public.log_record('根据身份证号查询最近一笔有效推荐人信息失败响应数据', sys._getframe().f_lineno, recommend_info)

    def test_bind_relation(self):
        '''   获取推荐人绑定关系 '''

        #获取推荐人编码
        recommerd_info = cma_recommend()

        print('recommerd_info:',recommerd_info)
        if recommerd_info:

            #根据推荐人编码获取推荐人绑定关系请求数据
            bind_req_data = {
                'recommerderNo': recommerd_info['content']['rcmderId']
            }
            public.log_record('根据推荐人编码获取推荐人绑定关系请求数据', sys._getframe().f_lineno, bind_req_data)

            bind_res_data = requests.post(
                url=config.bms_bind_relation_default_url,
                json=bind_req_data
            )
            if bind_res_data.json()['retCode']:
                public.log_record('根据推荐人编码获取推荐人绑定关系响应数据', sys._getframe().f_lineno, bind_res_data.text)
                self.assertEqual(bind_res_data.json()['retCode'], '000000')
            else:
                public.log_record('根据推荐人编码获取推荐人绑定关系响应数据', sys._getframe().f_lineno, bind_res_data.text)
        else:
            public.log_record('推荐人编码为空,未能获取推荐人绑定关系', sys._getframe().f_lineno, recommerd_info)
            return None

    def test_query_channel_info(self):
        '''  查询渠道信息 '''

        # 根据指定营销渠道编号查询营销渠道信息请求信息
        channel_info_req_data = {
            'channelType': config.special_channel_type
        }
        public.log_record('根据指定营销渠道编号查询营销渠道信息请求数据', sys._getframe().f_lineno, channel_info_req_data)

        channel_info_res_data = requests.post(
            url=config.bms_channel_info_default_url,
            json=channel_info_req_data
        )
        if channel_info_res_data.json()['retCode']:
            public.log_record('根据指定营销渠道编号查询营销渠道信息响应数据', sys._getframe().f_lineno, channel_info_res_data.text)
            channel_count = len(channel_info_res_data.json()['data'])
            self.assertGreater(channel_count,0)

        else:
            public.log_record('根据指定营销渠道编号查询营销渠道信息失败响应数据', sys._getframe().f_lineno, channel_info_res_data.text)
            return None

    def test_query_seller_info(self):
        '''  查询客户经理信息 '''

        # 根据营销渠道编号查询客户经理信息
        seller_info_req_data = {
            'channelType': config.channel_type,
            'orgId':config.default_org_id
        }
        public.log_record('根据营销渠道编号查询客户经理信息请求数据', sys._getframe().f_lineno, seller_info_req_data)

        channel_info_res_data = requests.post(
            url=config.bms_get_seller_default_url,
            json=seller_info_req_data
        )
        if channel_info_res_data.json()['retCode']:
            public.log_record('根据营销渠道编号查询客户经理信息响应数据', sys._getframe().f_lineno, channel_info_res_data.text)
            self.assertEqual(channel_info_res_data.json()['retCode'],'000000')

        else:
            public.log_record('根据营销渠道编号查询客户经理信息响应数据失败响应数据', sys._getframe().f_lineno, channel_info_res_data.text)
            return None

    def test_auto_show_seller(self):
        '''  自动展示客户经理 '''

        # 营销渠道为代账/代理渠道,带出合作渠道绑定的客户经理请求数据
        auto_show_req_data = {
            'sellerId': config.dz_seller_id,
        }
        public.log_record('带出代账合作渠道绑定的客户经理请求数据', sys._getframe().f_lineno, auto_show_req_data)

        auto_show_res_data = requests.post(
            url=config.bms_get_seller_default_url,
            json=auto_show_req_data
        )
        if auto_show_res_data.json()['retCode']:
            public.log_record('带出代账合作渠道绑定的客户经理响应数据', sys._getframe().f_lineno, auto_show_res_data.text)
            self.assertEqual(auto_show_res_data.json()['retCode'], '000000')
        else:
            public.log_record('带出代账合作渠道绑定的客户经理响应数据失败响应数据', sys._getframe().f_lineno, auto_show_res_data.text)
            return None

    def test_get_org_list(self):
        '''  获取机构列表 '''

        # 获取机构列表请求数据
        org_list_req_data = {
                    'pageNo':'1',
                    'pageSize':'100',
                    'param':{
                        'orgId':'',
                        'orgName':'',
                        'parentOrgId':'',
                        'orgLevelList':['3','5'],
                    },
        }
        public.log_record('获取机构列表请求数据', sys._getframe().f_lineno, org_list_req_data)

        org_list_res_data = requests.post(
            url=config.bms_org_list_default_list,
            json=org_list_req_data
        )
        if org_list_res_data.json()['retCode']:
            public.log_record('获取机构列表请求数据响应数据', sys._getframe().f_lineno, org_list_res_data.text)
            self.assertEqual(org_list_res_data.json()['retCode'], '000000')
        else:
            public.log_record('获取机构列表请求数据失败响应数据', sys._getframe().f_lineno, org_list_res_data.text)
            return None

    def test_qcc_company(self):
        '''  企查查模糊匹配企业名称'''

        # 企查查模糊匹配企业名称请求数据
        qcc_req_data = {
            'name':'公司',
            'pageSize':10,
             'pageIndex':1
        }
        public.log_record('企查查模糊匹配企业名称请求数据', sys._getframe().f_lineno, qcc_req_data)

        org_list_res_data = requests.post(
            url=config.inner_qcc_default_url,
            json=qcc_req_data
        )
        if org_list_res_data.json()['code']:
            public.log_record('企查查模糊匹配企业名称响应数据', sys._getframe().f_lineno, org_list_res_data.text)
            self.assertEqual(org_list_res_data.json()['code'], 0)
        else:
            public.log_record('企查查模糊匹配企业名称失败响应数据', sys._getframe().f_lineno, org_list_res_data.text)
            return None

    def test_qcc_company(self):
        '''  企查查模糊匹配企业名称'''

        # 企查查模糊匹配企业名称请求数据
        qcc_req_data = {
            'name': '公司',
            'pageSize': 10,
            'pageIndex': 1
        }
        public.log_record('企查查模糊匹配企业名称请求数据', sys._getframe().f_lineno, qcc_req_data)

        qcc_res_data = requests.post(
            url=config.inner_qcc_default_url,
            json=qcc_req_data
        )
        if qcc_res_data.json()['code']:
            public.log_record('企查查模糊匹配企业名称响应数据', sys._getframe().f_lineno, qcc_res_data.text)
            self.assertEqual(qcc_res_data.json()['code'], 0)
        else:
            public.log_record('企查查模糊匹配企业名称失败响应数据', sys._getframe().f_lineno, qcc_res_data.text)
            return None

    def test_query_gjj(self):
        '''  查询公积金'''

        # 查询公积金请求数据
        gjj_req_data = {
            'source': 'WPT',
            'certId': '4305231986012600423', #user_info[1]
        }
        public.log_record('查询公积金请求数据', sys._getframe().f_lineno, gjj_req_data)

        gjj_res_data = requests.post(
            url=config.inner_gjj_default_url,
            json=gjj_req_data
        )
        if gjj_res_data.json()['code']:
            public.log_record('查询公积金响应数据', sys._getframe().f_lineno, gjj_res_data.text)

        else:
            public.log_record('查询公积金响应失败数据', sys._getframe().f_lineno, gjj_res_data.text)
            return None

    def test_query_soins(self):
        '''  查询社保'''

        # 查询社保请求数据
        soins_req_data = {
            'name': '公司',
        }
        public.log_record('查询社保请求数据', sys._getframe().f_lineno, soins_req_data)

        soins_res_data = requests.post(
            url=config.inner_soins_default_url,
            json=soins_req_data
        )
        if soins_res_data.json()['code']:
            public.log_record('查询社保响应数据', sys._getframe().f_lineno, soins_res_data.text)

        else:
            public.log_record('查询社保响应失败数据', sys._getframe().f_lineno, soins_res_data.text)
            return None

    def test_query_insurance(self):
        '''  查询保单'''

        # 查询保单请求数据
        insurance_req_data = {
            'source': 'WPT',
            'certId': '4305231986012600423',  # user_info[1]
        }
        public.log_record('查询保单请求数据', sys._getframe().f_lineno, insurance_req_data)

        insurance_res_data = requests.post(
            url=config.inner_insurance_default_url,
            json=insurance_req_data
        )
        if insurance_res_data.json()['code']:
            public.log_record('查询保单响应数据', sys._getframe().f_lineno, insurance_res_data.text)
            self.assertEqual(insurance_res_data.json()['code'], 0)
        else:
            public.log_record('查询社保响应失败数据', sys._getframe().f_lineno, insurance_res_data.text)
            return None

    def test_phone_status(self):
        '''  查看手机在网状态'''

        # 查看手机在网状态请求数据
        phone_req_data = {
        'source':'WPT',
        'phoneList':['13425106229','13412345676','13412345675','13412345674','13412345673','13412345672']
        }
        public.log_record('查看手机在网状态请求数据', sys._getframe().f_lineno, phone_req_data)

        phone_res_data = requests.post(
            url=config.inner_phone_status_default_inner,
            json=phone_req_data
        )
        if phone_res_data.json()['code']:
            public.log_record('查看手机在网状态响应数据', sys._getframe().f_lineno, phone_res_data.text)
            self.assertEqual(phone_res_data.json()['code'], 0)
        else:
            public.log_record('查看手机在网状态失败响应数据', sys._getframe().f_lineno, phone_res_data.text)
            return None

    def test_get_workdays(self):
        '''  获取工作时间'''

        current_time = public.GetCurrentTime()
        workdays = str(current_time.year_mont_day())

        # 查看工作日请求数据
        workdays_req_data ={
            'date':workdays,
            'days':'6'
        }
        public.log_record('查看工作日请求数据', sys._getframe().f_lineno, workdays_req_data)
        workdays_res_data = requests.post(
            url=config.oms_workdays_default_url,
            json=workdays_req_data
        )
        if workdays_res_data.json()['retCode']:
            public.log_record('查看工作日响应数据', sys._getframe().f_lineno, workdays_res_data.text)
            self.assertEqual(workdays_res_data.json()['retCode'], '000000')
        else:
            public.log_record('查看工作日失败响应数据', sys._getframe().f_lineno, workdays_res_data.text)
            return None

    def test_get_code_detail(self):
        '''  获取枚举值'''

        # 获取枚举值请求数据
        code_detail_req_data ={
            'codeTypeList':config.code_list
        }
        public.log_record('获取枚举值请求数据', sys._getframe().f_lineno, code_detail_req_data)
        code_detail_res_data = requests.post(
            url=config.oms_code_detail_default_url,
            json=code_detail_req_data
        )
        if code_detail_res_data.json()['retCode']:
            public.log_record('获取枚举值响应数据', sys._getframe().f_lineno, code_detail_res_data.text)
            self.assertEqual(code_detail_res_data.json()['retCode'], '000000')
        else:
            public.log_record('获取枚举值失败响应数据', sys._getframe().f_lineno, code_detail_res_data.text)
            return None

    def test_get_pass_apply(self):
        '''  获取审批通过的申请单'''

        #查询条件 已放款
        apply_status = {'apply_status':'004'}

        wk = wk_db_server.ApplyToCuBaseInfoRepository()

        query_result = wk.handel_query(('cert_code'),**apply_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下无数据' % apply_status, sys._getframe().f_lineno, query_result)
            return None

        # 获取审批通过申请单的请求数据
        pass_apply_req_data = {
            'certId': query_result['cert_code']
        }
        public.log_record('获取审批通过申请单的请求数据', sys._getframe().f_lineno, pass_apply_req_data)
        pass_apply_res_data = requests.post(
            url=config.wk_pass_apply_default_url,
            json=pass_apply_req_data
        )
        if pass_apply_res_data.json()['code']:
            public.log_record('获取审批通过申请单的响应数据', sys._getframe().f_lineno, pass_apply_res_data.text)
            apply_count = len(pass_apply_res_data.json()['data']['applyIdList'])
            self.assertGreater(apply_count,0)
        else:
            public.log_record('获取审批通过申请单失败响应数据', sys._getframe().f_lineno, pass_apply_res_data.text)
            return None


if __name__ == '__main__':
    unittest.main()
