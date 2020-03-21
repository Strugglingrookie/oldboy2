#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 8:22
# @Author  : TangYong
# @Email   : tangyonge@yonyou.com
# @File    : remote_signature.py
# @Software: PyCharm

import  unittest
import sys
import requests
from fun import public
from settings import  config

class RemoteSignature(unittest.TestCase):
    '''  远程面签 '''

    def test_current_finish_signature(self):
        '''  当前/已完成面签列表'''

        signatured_req_data = {
            'pageNo':1,
            'pageSize':10,
            'param':{
                'entryType':'lasDirectApprove'
            }
        }
        public.log_record('当前/已完成面签请求数据', sys._getframe().f_lineno, signatured_req_data)

        signatured_res_data = requests.post(
            url=config.bms_signature_default_url,
            json=signatured_req_data
        )
        if signatured_res_data.json()['retCode']:
            public.log_record('当前/已完成面签响应数据', sys._getframe().f_lineno, signatured_res_data.text)
            self.assertEqual(signatured_res_data.json()['retCode'],'000000')
        else:
            public.log_record('当前/已完成面签失败响应数据', sys._getframe().f_lineno, signatured_res_data.text)

    def test_video_task_list(self):
        '''  视频任务列表'''

        video_req_data = {
            'pageNo':1,
            'pageSize':10,
            'param':{
                'entryType':'lasDirectApprove'
            }
        }
        public.log_record('视频任务列表请求数据', sys._getframe().f_lineno, video_req_data)

        video_res_data = requests.post(
            url=config.bms_video_default_url,
            json=video_req_data
        )
        if video_res_data.json()['retCode']:
            public.log_record('视频任务列表请求数据响应数据', sys._getframe().f_lineno, video_res_data.text)
            self.assertEqual(video_res_data.json()['retCode'],'000000')
        else:
            public.log_record('视频任务列表失败响应数据', sys._getframe().f_lineno, video_res_data.text)


if __name__ == '__main__':
    unittest.main()