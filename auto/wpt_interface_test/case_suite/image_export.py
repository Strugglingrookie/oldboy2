#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 15:28
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : image_export.py
# @Software: PyCharm

import sys
import requests
import unittest
from settings import config
from fun import public
from fun import  wk_db_server

class ImageExport(unittest.TestCase):
    '''  影像导出 '''

    def test_export_image(self):
        '''  导出影像 '''

        #查询条件,发标中
        apply_status = {'apply_status':'200'}

        wk = public.wk_db_server.ApplyToCuBaseInfoRepository()

        query_result = wk.handel_query(('t1.apply_id','t2.cert_code'),**apply_status)

        if query_result is None:
            public.log_record('当前查询条件【%s】下无数据'%apply_status, sys._getframe().f_lineno, query_result)
            return None

        #影像导出请求数据
        export_req_data = {
            'applyId':query_result['apply_id'],
            'certId':query_result['cert_code']
        }
        public.log_record('影像导出请求数据' , sys._getframe().f_lineno, export_req_data)

        export_res_data = requests.post(
            url = config.wk_image_export_default_url,
            json=export_req_data,
        )
        if export_res_data.json()['code']:
            public.log_record('影像导出响应数据', sys._getframe().f_lineno, export_res_data.text)
            image_count = len(export_res_data.json()['data']['list'])
            self.assertGreater(image_count,0)
        else:
            public.log_record('影像导出失败响应数据', sys._getframe().f_lineno, export_res_data.text)


if __name__ == '__main__':
    unittest.main()