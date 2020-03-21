#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 8:21
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com

# @Software: PyCharm

import sys
import  unittest
import requests
from fun import public
from settings import  config

class OrganizationRepair(unittest.TestCase):
    '''  机构补件'''

    def test_organization_repair(self):
        '''  查询机构补件'''

        repair_req_data = {
            'belongOrgId':config.default_operate_org_id
        }
        public.log_record('查询机构补件请求数据', sys._getframe().f_lineno, repair_req_data)

        repair_res_data = requests.post(
            url=config.fatp_organization_repair_default_url,
            json=repair_req_data
        )
        if repair_res_data.json()['retCode']:
            public.log_record('查询机构补件响应数据', sys._getframe().f_lineno, repair_res_data.text)
            self.assertEqual(repair_res_data.json()['retCode'],'000000')
        else:
            public.log_record('查询机构补件失败响应数据', sys._getframe().f_lineno, repair_res_data.text)

if __name__ == '__main__':
    unittest.main()