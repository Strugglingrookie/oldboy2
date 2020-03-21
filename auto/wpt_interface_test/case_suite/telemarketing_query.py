#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 8:17
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : telemarketing_query.py
# @Software: PyCharm

import  unittest
import sys
import requests
from fun import public
from settings import  config

class TelemarketingQuery(unittest.TestCase):
    '''  电销查询'''

    def test_telemarketing_query(self):
        '''  电销查询'''

        telemarketing_req_data =  {
            "param": {
                "orgId": config.default_operate_org_id,
                "isDefault": 1
            },
            "pageNo": 1,
            "pageSize": 10
        }
        public.log_record('电销查询请求数据', sys._getframe().f_lineno, telemarketing_req_data)

        telemarketing_res_data = requests.post(
            url=config.lcrm_telemarketing_default_url,
            json=telemarketing_req_data
        )
        if telemarketing_res_data.json()['retCode']:
            public.log_record('电销查询响应数据', sys._getframe().f_lineno, telemarketing_res_data.text)
            self.assertEqual(telemarketing_res_data.json()['retCode'],'000000')

        else:
            public.log_record('电销查询失败响应数据', sys._getframe().f_lineno, telemarketing_res_data.text)



if __name__ == '__main__':
    unittest.main()