#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 9:05
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : accept_input.py
# @Software: PyCharm
import sys
import unittest
import requests
from fun import public
from settings import config

for i in range(3):
    get_user_info = public.get_user_auth_info()
    if get_user_info[0] != '默认容错用户信息':
        break

def admission(business_type):

    req_data = {
        'certId':get_user_info[1],
        'businessType': business_type,
        'inputType': 'NOTXD',
        'mainBorrowerCertId': '',
        'interfaceType': 'Y1',
        'source': 'WPT'
    }

    # 获取到其他业务类型的中文名称
    for k, v in config.business_type.items():
        if v[0] == business_type:
            business_type_name = v[1]

    try:
        response = requests.post(
            url=config.inner_admission_default_url,
            json=req_data
        )
        public.log_record('准入%s'%business_type_name, sys._getframe().f_lineno, '{url:%s,data:%s}' % (response.url, str(req_data)))
        return response.json()

    except Exception as e:
        public.log_record('准入%s'% business_type_name,sys._getframe().f_lineno,',异常信息:%s'%e)


class Admission(unittest.TestCase):
    '''  申请录入'''

    def test_admission_yyfax(self):
        ''' 准入友金快贷'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['YYFAX'][0])

        if admission_result:
            is_y = admission_result['data']['isAdmission']
            public.log_record('准入友金快贷响应结果:', sys._getframe().f_lineno, admission_result)
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入友金快贷')
        else:
            public.log_record('准入友金快贷失败响应结果',sys._getframe().f_lineno,admission_result)

    def test_admission_zrb(self):
        ''' 准入真融宝'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['ZRB'][0])


        if admission_result:
            is_y = admission_result['data']['isAdmission']
            public.log_record('准入真融宝响应结果:', sys._getframe().f_lineno, admission_result)
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入真融宝')
        else:
            public.log_record('准入真融宝失败响应结果',sys._getframe().f_lineno,admission_result)

    def test_admission_szs(self):
        ''' 准入石嘴山'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['SZS'][0])


        if admission_result:
            public.log_record('准入石嘴山响应结果', sys._getframe().f_lineno, admission_result)
            is_y = admission_result['data']['isAdmission']
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入石嘴山')
        else:
            public.log_record('准入石嘴山失败响应结果', sys._getframe().f_lineno,'未查征信：%s' % admission_result)

    def test_admission_xgm(self):
        ''' 准入西格玛'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['XGM'][0])


        if admission_result:
            is_y = admission_result['data']['isAdmission']
            public.log_record('准入西格玛响应结果', sys._getframe().f_lineno,  admission_result)
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入西格玛')
        else:
            public.log_record('准入西格玛失败响应结果', sys._getframe().f_lineno, '未查征信：%s' % admission_result)

    def test_admission_hxb(self):
        ''' 准入华兴银行'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['HXB'][0])

        if admission_result:
            public.log_record('准入华兴银行响应结果', sys._getframe().f_lineno,  admission_result)
            is_y = admission_result['data']['isAdmission']
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入华兴银行')
        else:
            public.log_record('准入华兴银行失败响应结果', sys._getframe().f_lineno, '未查征信：%s' % admission_result)


    def test_admission_njb(self):
        ''' 准入南京银行'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['NJB'][0])

        if admission_result:
            is_y = admission_result['data']['isAdmission']
            public.log_record('准入南京银行响应结果', sys._getframe().f_lineno,  admission_result)
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入南京银行')
        else:
            public.log_record('准入南京银行失败响应结果', sys._getframe().f_lineno, '未查征信：%s' % admission_result)

    def test_admission_xwb(self):
        ''' 准入新网银行'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['XWB'][0])

        if admission_result:
            public.log_record('准入新网银行响应结果', sys._getframe().f_lineno, admission_result)
            is_y = admission_result['data']['isAdmission']
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入新网银行')
        else:
            public.log_record('准入新网银行失败响应结果', sys._getframe().f_lineno,  admission_result)

    def test_admission_mtb(self):
        ''' 准入民泰银行'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['MTB'][0])

        if admission_result:
            public.log_record('准入民泰银行响应结果', sys._getframe().f_lineno, admission_result)
            is_y = admission_result['data']['isAdmission']
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入民泰银行')
        else:
            public.log_record('准入民泰银行失败响应结果', sys._getframe().f_lineno, admission_result)

    def test_admission_lfb(self):
        ''' 准入廊坊银行'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['LFB'][0])

        if admission_result:
            public.log_record('准入廊坊银行响应结果:', sys._getframe().f_lineno, admission_result)
            is_y = admission_result['data']['isAdmission']
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入廊坊银行')
        else:
            public.log_record('准入廊坊银行失败响应结果', sys._getframe().f_lineno, admission_result)

    def test_admission_cdb(self):
        ''' 准入承德银行'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['CDB'][0])


        if admission_result:
            public.log_record('准入承德银行响应结果:', sys._getframe().f_lineno, admission_result)
            is_y = admission_result['data']['isAdmission']
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入承德银行')
        else:
            public.log_record('准入承德银行失败响应结果', sys._getframe().f_lineno, admission_result)

    def test_admission_ccns(self):
        ''' 准入长春农商'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['CCNS'][0])

        if admission_result:
            is_y = admission_result['data']['isAdmission']
            public.log_record('准入长春农商响应结果:', sys._getframe().f_lineno, admission_result)
            self.assertEqual(str(is_y).upper(), 'Y'.upper() )
        else:
            public.log_record('准入长春农商失败响应结果', sys._getframe().f_lineno,  admission_result)

    def test_admission_nbts(self):
        ''' 准入宁波通商'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['NBTS'][0])

        if admission_result:
            public.log_record('准入宁波通商响应结果:', sys._getframe().f_lineno, admission_result)
            is_y = admission_result['data']['isAdmission']
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入宁波通商')
        else:
            public.log_record('准入宁波通商失败响应结果', sys._getframe().f_lineno,  admission_result)

    def test_admission_zljr(self):
        ''' 准入招联金融'''
        public.log_record('用户信息', sys._getframe().f_lineno, get_user_info)
        admission_result = admission(config.business_type['ZLJR'][0])

        if admission_result:
            public.log_record('准入招联金融响应结果:', sys._getframe().f_lineno, admission_result)
            is_y = admission_result['data']['isAdmission']
            self.assertEqual(str(is_y).upper(), 'Y'.upper(), '准入招联金融')
        else:
            public.log_record('准入招联金失败响应结果', sys._getframe().f_lineno, admission_result)


class Submit(unittest.TestCase):
    ''' 提交申请'''

    def test_submit_yyfax(self):
        ''' 提交友金快贷 '''
        business_type = config.business_type['YYFAX'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【友金快贷】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status,'000000')
        else:
            public.log_record('提交【友金快贷】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_zrb(self):
        '''  提交真融宝 '''
        business_type = config.business_type['ZRB'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【真融宝】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status,'000000')
        else:
            public.log_record('提交【真融宝】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_szs(self):
        '''  提交石嘴山 '''
        business_type = config.business_type['SZS'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【石嘴山】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status,'000000')
        else:
            public.log_record('提交【石嘴山】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_xgm(self):
        '''  提交西格玛 '''
        business_type = config.business_type['XGM'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【西格玛】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status,'000000')
        else:
            public.log_record('提交【西格玛】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_hxb(self):
        '''  提交华兴银行 '''
        business_type = config.business_type['HXB'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【华兴银行】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status,'000000')
        else:
            public.log_record('提交【华兴银行】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_njb(self):
        '''  提交南京银行 '''
        business_type = config.business_type['NJB'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【南京银行】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status, '000000')
        else:
            public.log_record('提交【南京银行】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_xwb(self):
        '''  提交新网银行 '''
        business_type = config.business_type['XWB'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【新网银行】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status, '000000')
        else:
            public.log_record('提交【新网银行】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_mtb(self):
        '''  提交民泰银行 '''
        business_type = config.business_type['MTB'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【民泰银行】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status, '000000')
        else:
            public.log_record('提交【民泰银行】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_lfb(self):
        '''  提交廊坊银行 '''
        business_type = config.business_type['LFB'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【廊坊银行】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status, '000000')
        else:
            public.log_record('提交【廊坊银行】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_cdb(self):
        '''  提交承德银行 '''
        business_type = config.business_type['CDB'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【承德银行】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status, '000000')
        else:
            public.log_record('提交【承德银行】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_ccns(self):
        '''  提交长春农商 '''
        business_type = config.business_type['CCNS'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【长春农商】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status, '000000')
        else:
            public.log_record('提交【长春农商】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_nbts(self):
        '''  提交宁波通商 '''
        business_type = config.business_type['NBTS'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【宁波通商】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status, '000000')
        else:
            public.log_record('提交【宁波通商】失败响应结果', sys._getframe().f_lineno, submit_result)

    def test_submit_zljr(self):
        '''  提交招联金融 '''
        business_type = config.business_type['ZLJR'][0]
        submit_result = public.submit(business_type)

        if submit_result:
            public.log_record('提交【招联金融】响应结果', sys._getframe().f_lineno, submit_result)
            submit_status = submit_result['code']
            self.assertEqual(submit_status, '000000')
        else:
            public.log_record('提交【招联金融】失败响应结果', sys._getframe().f_lineno, submit_result)


if __name__ == '__main__':
    unittest.main()
