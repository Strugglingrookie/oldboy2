import os
import sys
import json
import time
import random
import smtplib
import pymongo
import base64
import binascii
import requests
from settings import  config
from fun import wk_db_server
from Crypto.Cipher import AES
from email.header import Header
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart

class WkEvent:


    def signal(self):
        ''' 暂时专门用来处理补件处理数据'''

        start_time = time.time()

        # 用来改变流程状态的分案数据
        signal_data = {'apply_id': None, 'apply_status':'001', 'state': '0050', 'sub_state': '0015'}

        # 随机选择一个业务品种进行提交
        for k, v in config.business_type.items():
            business_type = v[0]
            break

        log_record('随机选择【%s】业务品种提交申请'%v[1], sys._getframe().f_lineno, business_type)

        response_result = submit(business_type)
        log_record('响应结果', sys._getframe().f_lineno, response_result)


        while not response_result:
            if time.time() - start_time > 15:
                break

        apply_id = response_result['data']['applyId']

        signal_data['apply_id'] = apply_id


        handle = wk_db_server.ApplyRepository()
        log_record('修改【%s】的状态'%apply_id,sys._getframe().f_lineno, handle.handel_update(**signal_data))

        return response_result

    def recover_status(self,apply_id):

        #恢复数据到初始状态
        signal_data = {'apply_id': apply_id, 'apply_status':'001','state': '0050', 'sub_state': '0001'}

        handle = wk_db_server.ApplyRepository()

        log_record('修改【%s】到初始状态' % signal_data['apply_id'], sys._getframe().f_lineno,signal_data)

class UploadImg:
    '''上传影像'''
    def __init__(self):
        self.img_addr = config.image_default_url
        self.get_time = GetCurrentTime()

    def upload_currency_img(self):
        '''上传通用影像'''
        try:
            file_list = {
                'multiple': ['A-08', open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
            }
            response = requests.post(
                url=self.img_addr,
                files=file_list,
                data={
                    'source': '05'}
            )

            img_no_list = response.json()['content']
            curreny_img_info = {
                "imageInfo": [
                    {
                        "attachmentNo": img_no_list[0],
                        "attachmentType": "A-08",
                        "attachmentRealFileName": "A-08-第二代身份证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    }
                ]
            }
            return curreny_img_info

        except Exception as  e:
            return e

    def upload_hxb_img(self):
        '''上传华兴银行影像'''
        try:
            file_list = {
                'multiple1': ['A-08', open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
                'multiple2': ['B-HX-01', open(os.path.join(config.file_path, 'B-HX-01-华兴银行-申请表.jpg').replace('/', '\\'), 'rb')],
                'multiple3': ['B-HX-02', open(os.path.join(config.file_path, 'B-HX-02-华兴银行-贷款合同.jpg').replace('/', '\\'), 'rb')],
                'multiple4': ['B-HX-03', open(os.path.join(config.file_path, 'B-HX-03-华兴银行-其他文件.jpg').replace('/', '\\'), 'rb')],
                'multiple5': ['B-HX-04', open(os.path.join(config.file_path, 'B-HX-04-华兴银行-购销合同.jpg').replace('/', '\\'), 'rb')],
            }
            response = requests.post(
                url=self.img_addr,
                files=file_list,
                data={
                    'source': '05'}
            )

            img_no_list = response.json()['content']
            
            hxb_img_info = {
                "imageInfo": [
                    {
                        "attachmentNo": img_no_list[0],
                        "attachmentType": "A-08",
                        "attachmentRealFileName": "A-08-第二代身份证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo":  img_no_list[1],
                        "attachmentType": "B-HX-01",
                        "attachmentRealFileName": "B-HX-01-华兴银行-申请表.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[2],
                        "attachmentType": "B-HX-02",
                        "attachmentRealFileName": "B-HX-02-华兴银行-贷款合同.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[3],
                        "attachmentType": "B-HX-03",
                        "attachmentRealFileName": "B-HX-03-华兴银行-其他文件.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[4],
                        "attachmentType": "B-HX-04",
                        "attachmentRealFileName": "B-HX-04-华兴银行-购销合同.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                ]
            }

            return hxb_img_info

        except Exception as  e:
            return e

    def upload_njb_img(self):
        '''上传南京银行影像'''
        try:
            file_list = {
                'multiple': ['A-08', open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
                'multiple1': ['A-10', open(os.path.join(config.file_path, 'A-10-客户影像.jpg').replace('/', '\\'), 'rb')],
                'multiple2': ['B-NJ-01', open(os.path.join(config.file_path, 'B-NJ-01-南京银行-营业执照_工商网截图.jpg').replace('/', '\\'), 'rb')],
                'multiple3': ['B-NJ-02', open(os.path.join(config.file_path, 'B-NJ-02-南京银行-第一年投保单.jpg').replace('/', '\\'), 'rb')],
                'multiple4': ['B-NJ-03', open(os.path.join(config.file_path, 'B-NJ-03-南京银行-第二年投保单.jpg').replace('/', '\\'), 'rb')],
                'multiple5': ['B-NJ-04', open(os.path.join(config.file_path, 'B-NJ-04-南京银行-第三年投保单.jpg').replace('/', '\\'), 'rb')],
            }
            response = requests.post(
                url=self.img_addr,
                files=file_list,
                data={
                    'source': '05'}
            )
            img_no_list = response.json()['content']

            njb_img_info = {
                "imageInfo": [
                    {
                        "attachmentNo": img_no_list[0],
                        "attachmentType": "A-08",
                        "attachmentRealFileName": "A-08-第二代身份证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[1],
                        "attachmentType": "A-10",
                        "attachmentRealFileName": "A-10-客户影像.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[2],
                        "attachmentType": "B-NJ-01",
                        "attachmentRealFileName": "B-NJ-01-南京银行-营业执照_工商网截图.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[3],
                        "attachmentType": "B-NJ-02",
                        "attachmentRealFileName": "B-NJ-02-南京银行-第一年投保单.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[4],
                        "attachmentType": "B-NJ-03",
                        "attachmentRealFileName": "B-NJ-03-南京银行-第二年投保单.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[5],
                        "attachmentType": "B-NJ-04",
                        "attachmentRealFileName": "B-NJ-04-南京银行-第三年投保单.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    }
                ]
            }
            return njb_img_info


        except Exception as e:
            return e

    def upload_mtb_img(self):
        '''上传民泰银行影像'''
        try:
            file_list = {

                'multiple1': ['A-06', open(os.path.join(config.file_path, 'A-06-征信查询授权书.jpg').replace('/', '\\'), 'rb')],
                'multiple2': ['A-08', open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
                'multiple3': ['A-10', open(os.path.join(config.file_path, 'A-10-客户影像.jpg').replace('/', '\\'), 'rb')],
                'multiple4': ['A-99', open(os.path.join(config.file_path, 'A-99-其他.jpg').replace('/', '\\'), 'rb')],
                'multiple5': ['B-MT-01',open(os.path.join(config.file_path, 'B-MT-01-民泰银行-营业执照_经营场所内部照.jpg').replace('/', '\\'), 'rb')],
                'multiple6': ['B-MT-02', open(os.path.join(config.file_path, 'B-MT-02-民泰银行-专案证明材料.jpg').replace('/', '\\'), 'rb')],
                'multiple7': ['B-MT-03', open(os.path.join(config.file_path, 'B-MT-03-民泰银行-贷款用途.jpg').replace('/', '\\'), 'rb')],
            }
            response = requests.post(
                url=self.img_addr,
                files=file_list,
                data={
                    'source': '05'}
            )
            img_no_list = response.json()['content']
            njb_img_info = {
                "imageInfo": [
                    {
                        "attachmentNo": img_no_list[0],
                        "attachmentType": "A-06",
                        "attachmentRealFileName": "A-06-征信查询授权书.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[1],
                        "attachmentType": "A-08",
                        "attachmentRealFileName": "A-08-第二代身份证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[2],
                        "attachmentType": "A-10",
                        "attachmentRealFileName": "A-10-客户影像.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[3],
                        "attachmentType": "A-99",
                        "attachmentRealFileName": "A-99-其他.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[4],
                        "attachmentType": "B-MT-01",
                        "attachmentRealFileName": "B-MT-01-民泰银行-营业执照_经营场所内部照.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[5],
                        "attachmentType": "B-MT-02",
                        "attachmentRealFileName": "B-MT-02-民泰银行-专案证明材料.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[6],
                        "attachmentType": "B-MT-03",
                        "attachmentRealFileName": "B-MT-03-民泰银行-贷款用途.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    }
                ]
            }
            return njb_img_info

        except Exception as e:
            return e

    def upload_lfb_img(self):
        '''上传廊坊银行影像'''
        try:
            file_list = {
                'multiple1': ['A-08', open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
                'multiple2': ['B-LF-01', open(os.path.join(config.file_path, 'B-LF-01-廊坊银行-征信材料.jpg').replace('/', '\\'), 'rb')],
                'multiple3': ['B-LF-02', open(os.path.join(config.file_path, 'B-LF-02-廊坊银行-审批材料.jpg').replace('/', '\\'), 'rb')],
            }
            response = requests.post(
                url=self.img_addr,
                files=file_list,
                data={
                    'source': '05'}
            )

            img_no_list = response.json()['content']
            lfb_img_info = {
                "imageInfo": [
                    {
                        "attachmentNo": img_no_list[0],
                        "attachmentType": "A-08",
                        "attachmentRealFileName": "A-08-第二代身份证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[1],
                        "attachmentType": "B-LF-01",
                        "attachmentRealFileName": "B-LF-01-廊坊银行-征信材料.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[2],
                        "attachmentType": "B-LF-02",
                        "attachmentRealFileName": "B-LF-02-廊坊银行-审批材料.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    }
                ]
            }

            return lfb_img_info


        except Exception as e:
            return e

    def upload_xwb_img(self):
        '''上传新网银行影像'''
        try:
            file_list = {
                'multiple1': ['A-08', open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
                'multiple2': ['B-XW-01', open(os.path.join(config.file_path, 'B-XW-01-新网银行-贷款用途的相关协议或合同.jpg').replace('/', '\\'), 'rb')],
                'multiple3': ['B-XW-02', open(os.path.join(config.file_path, 'B-XW-02-新网银行-营业执照.jpg').replace('/', '\\'), 'rb')],
                'multiple4': ['B-XW-05',open(os.path.join(config.file_path, 'B-XW-05-新网银行-结婚证.jpg').replace('/', '\\'), 'rb')],
                'multiple5': ['B-XW-06', open(os.path.join(config.file_path, 'B-XW-06-新网银行-控制人证明.jpg').replace('/', '\\'), 'rb')],
            }
            response = requests.post(
                url=self.img_addr,
                files=file_list,
                data={
                    'source': '05'}
            )
            img_no_list = response.json()['content']

            xwb_img_info = {
                "imageInfo": [
                    {
                        "attachmentNo": img_no_list[0],
                        "attachmentType": "A-08",
                        "attachmentRealFileName": "A-08-第二代身份证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[1],
                        "attachmentType": "B-XW-01",
                        "attachmentRealFileName": "B-XW-01-新网银行-贷款用途的相关协议或合同.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[2],
                        "attachmentType": "B-XW-02",
                        "attachmentRealFileName": "B-XW-02-新网银行-营业执照.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[3],
                        "attachmentType": "B-XW-05",
                        "attachmentRealFileName": "B-XW-05-新网银行-结婚证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[4],
                        "attachmentType": "B-XW-06",
                        "attachmentRealFileName": "B-XW-06-新网银行-控制人证明.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    }
                ]
            }
            return xwb_img_info

        except Exception as e:
            return e

    def upload_ccns_img(self):
        '''上传长春农商影像'''
        try:
            file_list = {
                'multiple1': ['A-08', open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
                'multiple2': ['A-09', open(os.path.join(config.file_path, 'A-09-还款卡.jpg').replace('/', '\\'), 'rb')],
                'multiple3': ['A-10', open(os.path.join(config.file_path, 'A-10-客户影像.jpg').replace('/', '\\'), 'rb')],
                'multiple4': ['B-CCNS-01',open(os.path.join(config.file_path, 'B-CCNS-01-长春农商-工作证明.jpg').replace('/', '\\'), 'rb')],
                'multiple5': ['B-CCNS-02', open(os.path.join(config.file_path, 'B-CCNS-02-长春农商-寿险资料.jpg').replace('/', '\\'), 'rb')],
                'multiple6': ['B-CCNS-03',open(os.path.join(config.file_path, 'B-CCNS-03-长春农商-公积金资料.jpg').replace('/', '\\'), 'rb')],
                'multiple7': ['B-CCNS-04',open(os.path.join(config.file_path, 'B-CCNS-04-长春农商-中华投保单.jpg').replace('/', '\\'), 'rb')],
            }
            response = requests.post(
                url=self.img_addr,
                files=file_list,
                data={
                    'source': '05'}
            )
            img_no_list = response.json()['content']
            ccns_img_info = {
                "imageInfo": [
                    {
                        "attachmentNo": img_no_list[0],
                        "attachmentType": "A-08",
                        "attachmentRealFileName": "A-08-第二代身份证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[1],
                        "attachmentType": "A-09",
                        "attachmentRealFileName": "A-09-还款卡.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[2],
                        "attachmentType": "A-10",
                        "attachmentRealFileName": "A-10-客户影像.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[3],
                        "attachmentType": "B-CCNS-01",
                        "attachmentRealFileName": "B-CCNS-01-长春农商-工作证明.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[4],
                        "attachmentType": "B-CCNS-02",
                        "attachmentRealFileName": "B-CCNS-02-长春农商-寿险资料.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[5],
                        "attachmentType": "B-CCNS-03",
                        "attachmentRealFileName": "B-CCNS-03-长春农商-公积金资料.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[6],
                        "attachmentType": "B-CCNS-04",
                        "attachmentRealFileName": "B-CCNS-04-长春农商-中华投保单.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    }
                ]
            }
            return ccns_img_info
        except Exception as e:
            return e

    def upload_zljr_img(self):
        '''上传招联金融影像'''
        try:
            file_list = {
                'multiple1': ['A-08', open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
                'multiple2': ['B-ZLJR-01', open(os.path.join(config.file_path, 'B-ZL-01-招联金融-贷款用途声明.pdf').replace('/', '\\'), 'rb')],
                'multiple3': ['B-ZLJR-02', open(os.path.join(config.file_path, 'B-ZL-02-招联金融-贷款用途证明.pdf').replace('/', '\\'), 'rb')],
            }
            response = requests.post(
                url=self.img_addr,
                files=file_list,
                data={
                    'source': '05'}
            )
            img_no_list = response.json()['content']
            zljr_img_info = {
                "imageInfo": [
                    {
                        "attachmentNo": img_no_list[0],
                        "attachmentType": "A-08",
                        "attachmentRealFileName": "A-08-第二代身份证.jpg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[1],
                        "attachmentType": "B-ZL-01",
                        "attachmentRealFileName": "B-ZL-01-招联金融-贷款用途声明.pdf",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    },
                    {
                        "attachmentNo": img_no_list[2],
                        "attachmentType": "B-ZL-02",
                        "attachmentRealFileName": "B-ZL-02-招联金融-贷款用途证明.pdfg",
                        "operator": "ZHAOSMB",
                        "inputDate": self.get_time.year_mont_day(),
                        "inputTime": self.get_time.hour_min_sec()
                    }
                ]
            }
            return zljr_img_info

        except Exception as e:
            return e

class CreditInquiry:

    def __init__(self,company='北京小桔科技有限公司',flag = ''):
        self.flag = flag
        self.final_data_dict = {}
        self.error_message = []
        self.company = company
        self.credit_inquiry_result = None
        self.handel_time = ChangeTimeFormat()

        if self.flag:
            pass
        else:
            self.user_info = get_user_auth_info()

    def upload_img(self):

        file_list = {
            'multiple1': ['A-01',
                          open(os.path.join(config.file_path, 'A-01-个人借款及担保申请表.jpg').replace('/', '\\'), 'rb')],
            'multiple2': ['A-06',
                          open(os.path.join(config.file_path, 'A-06-征信查询授权书.jpg').replace('/', '\\'), 'rb')],
            'multiple3': ['A-08',
                          open(os.path.join(config.file_path, 'A-08-第二代身份证.jpg').replace('/', '\\'), 'rb')],
        }

        log_record('上传征信影像附件',sys._getframe().f_lineno,file_list)

        try:
            response = requests.post(
                url=config.image_default_url,
                files=file_list,
                data={
                    'source': '05'
                }
            )
            log_record('征信影像附件上传结果', sys._getframe().f_lineno, response.text)

            return response.json()['content']

        except Exception as e:
            self.error_message.append('【%s】接口异常【%s】,请检查!' %(config.image_default_url,e))

    def inquiry_credit(self, platform='LEAGUER'):

        img_info = self.upload_img()

        wpt_no = 'I00002'
        current_time = time.localtime()
        year = (current_time[0])
        year = str(year)[2:4]

        month = (current_time[1])
        if month < 10:
            month = ''.join(['0', str(month)])
        else:
            month = str((current_time[1]))

        day = (current_time[2])
        if day < 10:
            day = ''.join(['0', str(day)])
        else:
            day = str((current_time[2]))

        final_time = ''.join([year, month, day])

        num = ''
        for i in range(10):
            num1 = random.randint(1, 9)
            num += str(num1)

        serialNo = ''.join([wpt_no, final_time, num])

        credit_data = {
            'customerName': self.user_info[0],
            'certNo': self.user_info[1],
            'serialNo': serialNo,
            'customerType': '001',
            'certType': 'Ind01',
            'outlet': '75501',
            'searcher': config.default_operation_name,
            'platform': platform,
            'saleChannel': '004',
            'triggerEvent': 'WPT',
            'authority': '南山公安局',
            'address': '广东省深圳市南山区',
            'employeeType': '010',
            'phone': '',
            'customerMgr': '152',
            'listImage': [
                {'imageSource': '06', 'imageNo': img_info[0], 'imageType': '00'},
                {'imageSource': '06', 'imageNo': img_info[1], 'imageType': '00'},
                {'imageSource': '06', 'imageNo': img_info[2],  'imageType': '00'},
            ],
            'companyName': self.company,

            'workAddress': {'province': '广东省', 'city': '深圳市', 'district': '南山区'},
            'familyAddress': {'province': '广东省', 'city': '深圳市', 'district': '南山区'}
        }

        self.final_data_dict.update(credit_data)

        log_record('提交征信查询数据', sys._getframe().f_lineno, self.final_data_dict)

        try:
            response = requests.post(
                url=config.inner_inquiryCredit_default_url,
                json=credit_data,
                headers={
                    'source': 'WPT',
                }
            )

            log_record('征信查询结果', sys._getframe().f_lineno, response.text)


            return response.json()
        except Exception as e:
            self.error_message.append('【%s】接口异常【%s】,请检查!' %( config.inner_inquiryCredit_default_url,e))

    #此函数与上述 inquiry_credit 功能重叠，因江林接口返回的数据，全是征信被否决的，此接口暂时单独用来查征信，用来准入和提交
    def query_credit(self,user_info:list,platform='LEAGUER'):

        img_info = self.upload_img()

        wpt_no = 'I00002'
        current_time = time.localtime()
        year = (current_time[0])
        year = str(year)[2:4]

        month = (current_time[1])
        if month < 10:
            month = ''.join(['0', str(month)])
        else:
            month = str((current_time[1]))

        day = (current_time[2])
        if day < 10:
            day = ''.join(['0', str(day)])
        else:
            day = str((current_time[2]))

        final_time = ''.join([year, month, day])

        num = ''
        for i in range(10):
            num1 = random.randint(1, 9)
            num += str(num1)

        serialNo = ''.join([wpt_no, final_time, num])

        credit_data = {
            'customerName': user_info[0],
            'certNo': user_info[1],
            'serialNo': serialNo,
            'customerType': '001',
            'certType': 'Ind01',
            'outlet': '75501',
            'searcher': config.default_operation_name,
            'platform': platform,
            'saleChannel': '004',
            'triggerEvent': 'WPT',
            'authority': '南山公安局',
            'address': '广东省深圳市南山区',
            'employeeType': '010',
            'phone': '',
            'customerMgr': '152',
            'listImage': [
                {'imageSource': '06', 'imageNo': img_info[0], 'imageType': '00'},
                {'imageSource': '06', 'imageNo': img_info[1], 'imageType': '00'},
                {'imageSource': '06', 'imageNo': img_info[2], 'imageType': '00'},
            ],
            'companyName': self.company,

            'workAddress': {'province': '广东省', 'city': '深圳市', 'district': '南山区'},
            'familyAddress': {'province': '广东省', 'city': '深圳市', 'district': '南山区'}
        }

        self.final_data_dict.update(credit_data)

        log_record('提交征信查询数据', sys._getframe().f_lineno, self.final_data_dict)

        try:
            response = requests.post(
                url=config.inner_inquiryCredit_default_url,
                json=credit_data,
                headers={
                    'source': 'WPT',
                }
            )

            log_record('征信查询结果', sys._getframe().f_lineno, response.text)
            return response.json()

        except Exception as e:
            self.error_message.append('【%s】接口异常【%s】,请检查!' % (config.inner_inquiryCredit_default_url, e))


    def fetch_result(self):
        #flag空判断，主要用来不使用指定身份证信息来查询征信，直接根据机构来查询

        if self.flag:
            certId = None
        else:
            certId = self.user_info[1]
            self.inquiry_credit()

        #查询征信结果数据
        query_data = {
            'certId': certId,
            'orgId': config.default_operate_org_id,
            'pageNo': 1,
            'pageSize': 30
        }
        log_record('查询征信结果请求数据',sys._getframe().f_lineno,query_data)

        start_time = time.time()
        try:
            while True:
                response = requests.post(
                    url=config.inner_fetchResult_default_url,
                    json=query_data,
                    headers={
                        'source': 'WPT'
                    }
                )

                if response.json()['data']['list']:

                    self.credit_inquiry_result = response.json()
                    log_record('查询征信结果返回数据', sys._getframe().f_lineno, response.text)

                    return response.json()


                elif time.time() - start_time > 35:
                    return self.error_message.append('【%s】征信报告解析失败!' %self.user_info[1])

        except Exception as e:
            self.error_message.append('【%s】接口异常【%s】,请检查!' %(config.inner_fetchResult_default_url,e))

    def format_data(self):

        query_result = self.fetch_result()

        print('query_result:',query_result)

        dict_result = query_result['data']['list'][0]

        if dict_result:
            pass
        else:
            return self.error_message.append('获取查询结果失败!')

        self.final_data_dict.update(dict_result)

        user_tags = dict(dict_result['userTags'].items())
        self.final_data_dict.update(user_tags)
        del self.final_data_dict['userTags']

        self.final_data_dict.update({'serialNo': dict_result['applyId']})
        del self.final_data_dict['applyId']

        self.final_data_dict.update({'certNo': dict_result['certId']})
        del self.final_data_dict['certId']

        self.final_data_dict.update({'bankInfo': dict_result['helpLoanResults']})
        del self.final_data_dict['helpLoanResults']

        # #转换成13位时间戳
        self.final_data_dict.update({'reportTime':self.handel_time.change_timestamp(dict_result['reportTime'])})

        self.final_data_dict.update({'timestamp': self.handel_time.change_timestamp(dict_result['queryDate'])})
        del self.final_data_dict['queryDate']

        del self.final_data_dict['triggerEvent']
        del self.final_data_dict['rejectCodes']

        self.final_data_dict.update({'familyAddress':[('广东省'), ('深圳市'), ('南山区')]})
        self.final_data_dict.update({'workAddress': [('广东省'), ('深圳市'), ('南山区')]})

        ##print('final_data_dict:', json.dumps(self.final_data_dict, ensure_ascii=False))

        return self.final_data_dict

    def save_to_mongoDB(self):

        self.format_data()

        client = pymongo.MongoClient(host=config.wpt_mongo_default_conn[0], port=config.wpt_mongo_default_conn[1])
        log_record('打开作业平台MongoDB', sys._getframe().f_lineno, client)

        conn = client.wpt
        cursor = conn.wpt_credit

        log_record('将征信结果保存到数据库', sys._getframe().f_lineno, self.final_data_dict)

        try:
            cursor.insert_one(self.final_data_dict)

            return self.credit_inquiry_result

        except Exception:
            self.error_message.append('【%s】数据库连接超时,请检查!' % config.wpt_mongo_default_conn)

class GetCurrentTime:
    
    def __init__(self):
        self.current_time = time.localtime()

    def all_number_time(self):

        year = (self.current_time[0])
        year = str(year)

        month = self.current_time[1]
        if month < 10:
            month = ''.join(['0', str(month)])
        else:
            month = str((self.current_time[1]))

        day = self.current_time[2]
        if day < 10:
            day = ''.join(['0', str(day)])
        else:
            day = str((self.current_time[2]))

        hour = self.current_time[3]
        if hour < 10:
            hour = ''.join(['0', str(hour)])
        else:
            hour = str((self.current_time[3]))

        # min = self.current_time[4]
        # if min < 10:
        #     min = ''.join(['0', str(min)])
        # else:
        #     min = str((self.current_time[4]))

        final_time = ''.join([year, month, day, hour])

        return final_time

    def year_mont_day(self):

        year = (self.current_time[0])
        year = str(year)

        month = self.current_time[1]
        if month < 10:
            month = ''.join(['0', str(month)])
        else:
            month = str((self.current_time[1]))

        day = self.current_time[2]
        if day < 10:
            day = ''.join(['0', str(day)])
        else:
            day = str((self.current_time[2]))

        final_date = '/'.join([year, month, day])

        return  final_date

    def hour_min_sec(self):

        hour = self.current_time[3]
        if hour < 10:
            hour = ''.join(['0', str(hour)])
        else:
            hour = str((self.current_time[3]))

        min = self.current_time[4]
        if min < 10:
            min = ''.join(['0', str(min)])
        else:
            min = str((self.current_time[4]))

        sec = self.current_time[4]

        if sec < 10:
            sec = ''.join(['0', str(sec)])
        else:
            sec = str((self.current_time[4]))

        final_time = ':'.join([hour,min,sec])

        return final_time

    def complete_time(self):
        current_time = ' '.join([self.year_mont_day(),self.hour_min_sec()])
        return current_time

class ChangeTimeFormat:
    # 将时间戳转换成字符串指定时间
    def format_timestamp(self,timeNum, format='%Y-%m-%d %H:%M:%S'):
        if len(str(timeNum)) > 10:
            timeStamp = float(timeNum / 1000)
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime(format, timeArray)
        else:
            timeArray = time.localtime(timeNum)
            otherStyleTime = time.strftime(format, timeArray)
        return otherStyleTime

    # 将指定时间转换成时间戳
    def change_timestamp(self,specify_time, format='%Y-%m-%d %H:%M:%S'):
        timestamp = time.mktime(time.strptime(specify_time, format))
        timestamp = timestamp * 1000
        return timestamp


# 加密/解密
class EncryptAndDecrypt:
    def __init__(self,iv=None,key=None):
        self.model = AES.MODE_CBC
        if iv is not None or key is not None:
            self.iv = bytes(iv, 'utf-8')
            self.key = bytes(key, 'utf-8')

    def aes_encrypt(self, raw_text):
        """PKCS5Padding加密算法 填充方式，加密内容必须为16字节的倍数，若不足则使用 padding填充"""
        text_length = len(raw_text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        bytes_text = bytes(raw_text + pad * amount_to_pad,'utf-8')
        cipher = AES.new(self.key, self.model, self.iv)
        return str(base64.b64encode(cipher.encrypt(bytes_text)),'utf-8')

    def aes_decrypt(self, encode_text):
        """解密"""
        encode_text = base64.b64decode(encode_text)
        cipher = AES.new(self.key, self.model, self.iv)
        decode_text = cipher.decrypt(encode_text).decode("utf-8")
        #去除占位符
        pad = ord(decode_text[-1])
        return decode_text[:-pad]


    def base64_encrypt(self, text):
        text = text.encode("utf-8")
        encode = base64.b64encode(text)
        return str(encode, 'utf-8')

    def base64_decrypt(self, text):
        decode = base64.b64decode(text)
        return str(decode, 'utf-8')


def log_record(log_name,lineno,log_content):
    '''

    :param log_name:  日志文件名称
    :param log_content: 日志内容
    :return: 日志记录
    '''

    current_format_time = GetCurrentTime()

    #创建loger对象
    logger = config.logging.getLogger(log_name)
    logger.setLevel(config.log_level)

    #添加文件/屏幕日志输出对象
    log_dir = os.path.join(config.base_dir, 'logs', 'AutoTest_' + current_format_time.all_number_time() + '.log')
    fh = config.logging.FileHandler(log_dir)
    sh = config.logging.StreamHandler()
    sh.setLevel(config.log_level)

    #设置输出log输出格式

    # formatter = config.logging.Formatter('%(asctime)s - %(name)s -line '+ str(lineno) +'-%(levelname)s - %(message)s')
    formatter = config.logging.Formatter('%(asctime)s, %(levelname)s, line-' + str(lineno) + ', %(name)s: %(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    #输出日志到屏幕和文件中
    logger.addHandler(fh)
    logger.addHandler(sh)

    #输出日志的内容
    logger.debug(log_content)
    logger.info(log_content)
    # logger.warning(log_content)
    # logger.error(log_content)
    # logger.critical(log_content)

    logger.removeFilter(fh)
    logger.removeHandler(sh)

    return  logger


def get_new_report():
    '''
    获取最新测试报告
    :return:
    '''

    report_dir = os.path.join(config.base_dir,'report')
    report_list = os.listdir(report_dir)

    if len(report_list)>0:

        '''
        1.在存放报告的路径下对报告的更新时间从早到晚进行排序
        2.lambda:匿名函数，将返回值赋值给key(固定写法)
        '''
        report_list.sort(key=lambda fn: os.path.getctime(report_dir + '\\' +fn))


        #获取最新测试报告
        new_report = os.path.join(report_dir,report_list[-1])

        return new_report


def send_email():

    #获取最新测试报告并打开
    test_report = get_new_report()
    if test_report:pass
    else:
        return '当前无可用测试报告'

    try:
        with open(test_report,'rb') as fr:
            mail_data = fr.read()

        #定义附件的格式
        mail_attachment = MIMEText(mail_data, 'bases64', 'utf-8')

        # 附件的类型为8进制
        mail_attachment['Content-Type'] = 'application/octet-stream'

        # 添加附件内容的配置信息
        mail_attachment['Content-Disposition'] =" attachment;filename='auto_test_report.html' "

        #创建电子邮件对象,related:表示出了可以发送邮件正文以外,还可以携带各种附件
        mail_content = MIMEMultipart('related')

        # #添加邮件主题
        mail_content['subject'] = Header(config.mail_info['subject'])

        #添加邮件正文
        mail_content.attach(MIMEText( mail_data,'html','utf-8'))

        #添加邮件附件
        mail_content.attach(mail_attachment)

        smtp = smtplib.SMTP()
        smtp.connect(config.mail_info['connect']['host'],config.mail_info['connect']['port'])
        smtp.login(config.mail_info['login']['username'],config.mail_info['login']['passwd'])
        smtp.sendmail(config.mail_info['sender'],config.mail_info['receiver'],mail_content.as_string())
        smtp.quit()

    except Exception as e:
        return e


def get_user_auth_info():
    start_time = time.time()
    user_info = []
    response = requests.post(
        url='http://172.30.1.71/api/autoGenUser',
        data={
        'phurl': config.hp_register_default_url,
        'bkName': '000001',
        }
    )

    while True:
        if response.json():

            if response.json()['status'] == 0:
                user_name = response.json()['data']['name']
                user_info.append(user_name)

                cert_id = response.json()['data']['certid']
                user_info.append(cert_id)

                phone = response.json()['data']['phone']
                user_info.append(phone)

                bank_no = response.json()['data']['bankno']
                user_info.append(bank_no)

                #获取生日
                year = cert_id[6:10]
                month = cert_id[10:12]
                day = cert_id[12:14]
                birthday = '/'.join([year,month,day])
                user_info.append(birthday)
                log_record('生成官网用户信息', sys._getframe().f_lineno, user_info)
                return user_info
            else:
               if time.time() - start_time < 90:
                   continue
               else:
                   user_info = ['默认容错用户信息', '542400198605127377', '13425106229', '6222029799547122166', '1986/05/12']
                   log_record('生成官网用户信息超时',sys._getframe().f_lineno,user_info)

                   return user_info


def get_card_num(start_with, total_num):

    result = start_with

    # 随机生成前N-1位
    while len(result) < total_num - 1:
        result += str(random.randint(0, 9))

    # 计算前N-1位的校验和
    s = 0
    card_num_length = len(result)
    for _ in range(2, card_num_length + 2):
        t = int(result[card_num_length - _ + 1])
        if _ % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t

    # 最后一位当做是校验位，用来补齐到能够整除10
    t = 10 - s % 10
    result += str(0 if t == 10 else t)
    return result


def check_card_num(card_num):
    s = 0
    card_num_length = len(card_num)
    for _ in range(1, card_num_length + 1):
        t = int(card_num[card_num_length - _])
        if _ % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t
    return s % 10 == 0


def submit(business_type):

    get_time = GetCurrentTime()
    get_user_info = get_user_auth_info()

    handel_credit = CreditInquiry()
    result = handel_credit.query_credit(get_user_info)
    print('result:',result)

    if business_type == config.business_type['HXB'][0]:

        #获取指定业务品种的银行卡号
        loan_card_id = config.bank_no['HXB']

        #获取指定业务类型的附件类型
        img = UploadImg()
        img_info = img.upload_hxb_img()

        #print('HXB_img_info:',img_info)

        start_time = time.time()
        while True:
            if img_info:
                req_data = {
                    "operatorType": "commitTask",
                    "state": "0010",
                    "properties": "NOTXD",
                    "businessType": business_type,
                    "applyType": "NormalApply",
                    "identityInfo": {
                        "idCode": get_user_info[1],
                        "idName": get_user_info[0],
                        "idSex": "男",
                        "idNation": "汉",
                        "idBirthday": get_user_info[4],
                        "idAddress": "广东省深圳市南山区",
                        "idIssuedBy": "南山公安局",
                        "idEffectDate": get_time.year_mont_day(),
                        "idExpiredDate": "2099/08/15",
                        "idRecorder": "ZHAOSMB",
                        "recorderDate": get_time.year_mont_day(),
                        "recorderTime": "11:12:22"
                    },
                    "customerInfo": {
                        # "yjsName":"U2379743969395867655",
                        "certCode": get_user_info[1],
                        "certType": "Ind01",
                        "certExpiredDate": get_time.year_mont_day(),
                        "certIssuedPlace": "南山公安局",
                        "name": "濮阳怜",
                        "education": "01",
                        "marriage": "20",
                        "familyStatus": "2",
                        "email": None,
                        "familyAddProvince": "广东省",
                        "familyAddCity": "深圳市",
                        "familyAddDistrict": "南山区",
                        "familyAddress": "讯美科技广场",
                        "familyAddInfo": "备注信息",
                        "permanentLocation": "01",
                        "mobilePhone": get_user_info[2],
                        "mobilePhone2": "13425106229",
                        "houseAreaCode": "0755",
                        "housePhone": "88888888",
                        "qq": "578812638",
                        "localHouseFlag": "1",
                        "localHouseAddress": "讯美科技广场",
                        "monthIncome": "30000",
                        "sex": "1",
                        "birthday": get_user_info[4],
                        "postAddress": None,
                        "familyAddLatitude": "22.545504",
                        "familyAddLongitude": "113.946978"
                    },
                    "workInfo": {
                        "workBelongIndustry": "A01",
                        "workOrgName": "友金所",
                        "workOrgNameRemark": "友金所",
                        "workDepartment": "系统运营部",
                        "workNature": "10",
                        "workHeadship": "测试",
                        "workPosition": "10",
                        "workBeginDate": "2018/08",
                        "workEmployeeType": "010",
                        "workIndustryDate": "2014/07/28",
                        "workAreaCode": "0755",
                        "workPhone": "88888888",
                        "workExtensionNumber": None,
                        "workAddProvince": "广东省",
                        "workAddCity": "深圳市",
                        "workAddDistrict": "南山区",
                        "workAddress": "讯美科技广场",
                        "workAddInfo": "备注信息",
                        "businessLicenceCode": "578812638",
                        "registeredCapital": "50000",
                        "workAddLatitude": "22.545504",
                        "workAddLongitude": "113.946978",
                        "stockLot": "10",
                        "takingsMonthly": 50000000,
                        "profitMarginMonthly": 100
                    },
                    "contactsInfo": [
                        {
                            "type": "1",
                            "name": "唐一",
                            "relationship": "0301",
                            "phone": "66666666",
                            "phoneArea": "0755",
                            "phoneExtensionNum": None
                        },
                        {
                            "type": "2",
                            "name": "唐二",
                            "relationship": "0101",
                            "remark": None,
                            "phone": "13425106229",
                            "contactCertId": "33038219680410795X",
                            "contactWorkCorp": "友金普惠"
                        },
                        {
                            "type": "3",
                            "name": "唐三",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106228"
                        },
                        {
                            "type": "3",
                            "name": "唐四",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106227"
                        },
                        {
                            "type": "3",
                            "name": "唐五",
                            "relationship": "0202",
                            "remark": None,
                            "phone": "13425106226"
                        }
                    ],
                    "borrowingMatters": {
                        "businessType": business_type,
                        "businessSum": "500000",
                        "loanTerm": "24",
                        "purpose": "02",
                        "otherPurpose": '企业生产经营',
                        "mainReturnType": "1",
                        "returnPeriod": "1",
                        "repayCardId": get_user_info[3],
                        "repayBank": "000020",
                        "loanCardId": loan_card_id,
                        "loanBank": "000001",
                        "tradeSum": 55
                    },
                    "notCustomerMatters": {
                        "customerType": "002",
                        "loanType": "120",
                        "saleChannel": "006",
                        "crChannel": None,
                        "isCertifition": "1",
                        "recommender": "林****",
                        "recommenderTel": "15633560000",
                        "interviewerId": "ZHAOSMB",
                        "interviewCenter": "755001",
                        "operateUserId": "7550114",
                        "operateAssistantUser": "GAOJZA",
                        "operateOrgId": "75501",
                        "inputUserName": "ZHAOSMB",
                        "inputDate": get_time.year_mont_day(),
                        "teamCaptain": "CAIJMD",
                        "saleDirector": "XUJGB",
                        "branchDirector": "ZHONGFP",
                        "departmentId": "1075501004",
                        # "officialLevel":None,
                        "recommenderNo": "000003",
                        # "relatedLoanNo":None,
                        "operateUserName": None,
                        "operateAssistantUserName": None,
                        "departmentName": None,
                        "interviewerName": None,
                        "interviewCenterName": None,
                        "crChannelName": None,
                        "insurancePolicy1": "01",
                        "insurancePolicy2": None,
                        "insurancePolicy3": None,
                        "providentFundBase": None,
                        "providentFundCompany": None,
                        "isRecommendedByOld": "0"
                    },
                    "approvalComments": {
                        "opinionType": "010"
                    },
                    "recordingAging": {
                        "startInputDate": get_time.year_mont_day(),
                        "startInputTime": get_time.hour_min_sec(),
                        "endInputDate": get_time.year_mont_day(),
                        "endInputTime": get_time.hour_min_sec()
                    }
                }
                req_data.update(img_info)
                log_record('提交【华兴银行】申请单',sys._getframe().f_lineno,req_data)
                break
            else:
                img_info = img.upload_hxb_img()
                if time.time() - start_time > 15:
                    break

        try:
            response = requests.post(
                url=config.wk_submit_default_url,
                json=req_data
            )
            return response.json()

        except Exception as e:
            return e

    if business_type == config.business_type['NJB'][0]:

        #获取指定业务类型的附件类型
        img = UploadImg()
        img_info = img.upload_njb_img()
        #print('NJB_img_info:', img_info)
        start_time = time.time()
        while True:
            if img_info:
                req_data = {
                    "operatorType": "commitTask",
                    "state": "0010",
                    "properties": "NOTXD",
                    "businessType": business_type,
                    "applyType": "NormalApply",
                    "identityInfo": {
                        "idCode": get_user_info[1],
                        "idName": get_user_info[0],
                        "idSex": "男",
                        "idNation": "汉",
                        "idBirthday": get_user_info[4],
                        "idAddress": "广东省深圳市南山区",
                        "idIssuedBy": "南山公安局",
                        "idEffectDate": get_time.year_mont_day(),
                        "idExpiredDate": "2099/08/15",
                        "idRecorder": "ZHAOSMB",
                        "recorderDate": get_time.year_mont_day(),
                        "recorderTime": "11:12:22"
                    },
                    "customerInfo": {
                        # "yjsName":"U2379743969395867655",
                        "certCode": get_user_info[1],
                        "certType": "Ind01",
                        "certExpiredDate": get_time.year_mont_day(),
                        "certIssuedPlace": "南山公安局",
                        "name": "濮阳怜",
                        "education": "01",
                        "marriage": "20",
                        "familyStatus": "2",
                        "email": None,
                        "familyAddProvince": "广东省",
                        "familyAddCity": "深圳市",
                        "familyAddDistrict": "南山区",
                        "familyAddress": "讯美科技广场",
                        "familyAddInfo": "备注信息",
                        "permanentLocation": "01",
                        "mobilePhone": get_user_info[2],
                        "mobilePhone2": "13425106229",
                        "houseAreaCode": "0755",
                        "housePhone": "88888888",
                        "qq": "578812638",
                        "localHouseFlag": "1",
                        "localHouseAddress": "讯美科技广场",
                        "monthIncome": "30000",
                        "sex": "1",
                        "birthday": get_user_info[4],
                        "postAddress": None,
                        "familyAddLatitude": "22.545504",
                        "familyAddLongitude": "113.946978"
                    },
                    "workInfo": {
                        "workBelongIndustry": "A01",
                        "workOrgName": "友金所",
                        "workOrgNameRemark": "友金所",
                        "workDepartment": "系统运营部",
                        "workNature": "10",
                        "workHeadship": "测试",
                        "workPosition": "10",
                        "workBeginDate": "2018/08",
                        "workEmployeeType": "010",
                        "workIndustryDate": "2014/07/28",
                        "workAreaCode": "0755",
                        "workPhone": "88888888",
                        "workExtensionNumber": None,
                        "workAddProvince": "广东省",
                        "workAddCity": "深圳市",
                        "workAddDistrict": "南山区",
                        "workAddress": "讯美科技广场",
                        "workAddInfo": "备注信息",
                        "businessLicenceCode": "578812638",
                        "registeredCapital": "50000",
                        "workAddLatitude": "22.545504",
                        "workAddLongitude": "113.946978",
                        "stockLot": "10",
                        "takingsMonthly": 50000000,
                        "profitMarginMonthly": 100
                    },
                    "contactsInfo": [
                        {
                            "type": "1",
                            "name": "唐一",
                            "relationship": "0301",
                            "phone": "66666666",
                            "phoneArea": "0755",
                            "phoneExtensionNum": None
                        },
                        {
                            "type": "2",
                            "name": "唐二",
                            "relationship": "0101",
                            "remark": None,
                            "phone": "13425106229",
                            "contactCertId": "33038219680410795X",
                            "contactWorkCorp": "友金普惠"
                        },
                        {
                            "type": "3",
                            "name": "唐三",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106228"
                        },
                        {
                            "type": "3",
                            "name": "唐四",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106227"
                        },
                        {
                            "type": "3",
                            "name": "唐五",
                            "relationship": "0202",
                            "remark": None,
                            "phone": "13425106226"
                        }
                    ],
                    "borrowingMatters": {
                        "businessType": business_type,
                        "businessSum": "500000",
                        "loanTerm": "24",
                        "purpose": "02",
                        "otherPurpose": '企业生产经营',
                        "mainReturnType": "1",
                        "returnPeriod": "1",
                        "repayCardId": get_user_info[3],
                        "repayBank": "000001",
                        "loanCardId": get_user_info[3],
                        "loanBank": "000001",
                        "tradeSum": 55
                    },
                    "notCustomerMatters": {
                        "customerType": "002",
                        "loanType": "120",
                        "saleChannel": "006",
                        "crChannel": None,
                        "isCertifition": "1",
                        "recommender": "林****",
                        "recommenderTel": "15633560000",
                        "interviewerId": "ZHAOSMB",
                        "interviewCenter": "755001",
                        "operateUserId": "7550114",
                        "operateAssistantUser": "GAOJZA",
                        "operateOrgId": "75501",
                        "inputUserName": "ZHAOSMB",
                        "inputDate": get_time.year_mont_day(),
                        "teamCaptain": "CAIJMD",
                        "saleDirector": "XUJGB",
                        "branchDirector": "ZHONGFP",
                        "departmentId": "1075501004",
                        # "officialLevel":None,
                        "recommenderNo": "000003",
                        # "relatedLoanNo":None,
                        "operateUserName": None,
                        "operateAssistantUserName": None,
                        "departmentName": None,
                        "interviewerName": None,
                        "interviewCenterName": None,
                        "crChannelName": None,
                        "insurancePolicy1": "01",
                        "insurancePolicy2": None,
                        "insurancePolicy3": None,
                        "providentFundBase": None,
                        "providentFundCompany": None,
                        "isRecommendedByOld": "0"
                    },
                    "approvalComments": {
                        "opinionType": "010"
                    },
                    "recordingAging": {
                        "startInputDate": get_time.year_mont_day(),
                        "startInputTime": get_time.hour_min_sec(),
                        "endInputDate": get_time.year_mont_day(),
                        "endInputTime": get_time.hour_min_sec()
                    }
                }
                req_data.update(img_info)
                log_record('提交【南京银行】申请单', sys._getframe().f_lineno, req_data)
                break
            else:
                img_info = img.upload_hxb_img()
                if time.time() - start_time > 15:
                    break

        try:
            response = requests.post(
                url=config.wk_submit_default_url,
                json=req_data
            )
            return response.json()

        except Exception as e:
            return e

    if business_type == config.business_type['MTB'][0]:

        #获取指定业务类型的附件类型
        img = UploadImg()
        img_info = img.upload_mtb_img()
        #print('mtB_img_info:', img_info)
        start_time = time.time()
        while True:
            if img_info:
                req_data = {
                    "operatorType": "commitTask",
                    "state": "0010",
                    "properties": "NOTXD",
                    "businessType": business_type,
                    "applyType": "NormalApply",
                    "identityInfo": {
                        "idCode": get_user_info[1],
                        "idName": get_user_info[0],
                        "idSex": "男",
                        "idNation": "汉",
                        "idBirthday": get_user_info[4],
                        "idAddress": "广东省深圳市南山区",
                        "idIssuedBy": "南山公安局",
                        "idEffectDate": get_time.year_mont_day(),
                        "idExpiredDate": "2099/08/15",
                        "idRecorder": "ZHAOSMB",
                        "recorderDate": get_time.year_mont_day(),
                        "recorderTime": "11:12:22"
                    },
                    "customerInfo": {
                        # "yjsName":"U2379743969395867655",
                        "certCode": get_user_info[1],
                        "certType": "Ind01",
                        "certExpiredDate": get_time.year_mont_day(),
                        "certIssuedPlace": "南山公安局",
                        "name": "濮阳怜",
                        "education": "01",
                        "marriage": "20",
                        "familyStatus": "2",
                        "email": None,
                        "familyAddProvince": "广东省",
                        "familyAddCity": "深圳市",
                        "familyAddDistrict": "南山区",
                        "familyAddress": "讯美科技广场",
                        "familyAddInfo": "备注信息",
                        "permanentLocation": "01",
                        "mobilePhone": get_user_info[2],
                        "mobilePhone2": "13425106229",
                        "houseAreaCode": "0755",
                        "housePhone": "88888888",
                        "qq": "578812638",
                        "localHouseFlag": "1",
                        "localHouseAddress": "讯美科技广场",
                        "monthIncome": "30000",
                        "sex": "1",
                        "birthday": get_user_info[4],
                        "postAddress": None,
                        "familyAddLatitude": "22.545504",
                        "familyAddLongitude": "113.946978"
                    },
                    "workInfo": {
                        "workBelongIndustry": "A01",
                        "workOrgName": "友金所",
                        "workOrgNameRemark": "友金所",
                        "workDepartment": "系统运营部",
                        "workNature": "10",
                        "workHeadship": "测试",
                        "workPosition": "10",
                        "workBeginDate": "2018/08",
                        "workEmployeeType": "010",
                        "workIndustryDate": "2014/07/28",
                        "workAreaCode": "0755",
                        "workPhone": "88888888",
                        "workExtensionNumber": None,
                        "workAddProvince": "广东省",
                        "workAddCity": "深圳市",
                        "workAddDistrict": "南山区",
                        "workAddress": "讯美科技广场",
                        "workAddInfo": "备注信息",
                        "businessLicenceCode": "578812638",
                        "registeredCapital": "50000",
                        "workAddLatitude": "22.545504",
                        "workAddLongitude": "113.946978",
                        "stockLot": "10",
                        "takingsMonthly": 50000000,
                        "profitMarginMonthly": 100
                    },
                    "contactsInfo": [
                        {
                            "type": "1",
                            "name": "唐一",
                            "relationship": "0301",
                            "phone": "66666666",
                            "phoneArea": "0755",
                            "phoneExtensionNum": None
                        },
                        {
                            "type": "2",
                            "name": "唐二",
                            "relationship": "0101",
                            "remark": None,
                            "phone": "13425106229",
                            "contactCertId": "33038219680410795X",
                            "contactWorkCorp": "友金普惠"
                        },
                        {
                            "type": "3",
                            "name": "唐三",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106228"
                        },
                        {
                            "type": "3",
                            "name": "唐四",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106227"
                        },
                        {
                            "type": "3",
                            "name": "唐五",
                            "relationship": "0202",
                            "remark": None,
                            "phone": "13425106226"
                        }
                    ],
                    "borrowingMatters": {
                        "businessType": business_type,
                        "businessSum": "500000",
                        "loanTerm": "24",
                        "purpose": "02",
                        "otherPurpose": '企业生产经营',
                        "mainReturnType": "1",
                        "returnPeriod": "1",
                        "repayCardId": get_user_info[3],
                        "repayBank": "000001",
                        "loanCardId": get_user_info[3],
                        "loanBank": "000001",
                        "tradeSum": 55
                    },
                    "notCustomerMatters": {
                        "customerType": "002",
                        "loanType": "120",
                        "saleChannel": "006",
                        "crChannel": None,
                        "isCertifition": "1",
                        "recommender": "林****",
                        "recommenderTel": "15633560000",
                        "interviewerId": "ZHAOSMB",
                        "interviewCenter": "755001",
                        "operateUserId": "7550114",
                        "operateAssistantUser": "GAOJZA",
                        "operateOrgId": "75501",
                        "inputUserName": "ZHAOSMB",
                        "inputDate": get_time.year_mont_day(),
                        "teamCaptain": "CAIJMD",
                        "saleDirector": "XUJGB",
                        "branchDirector": "ZHONGFP",
                        "departmentId": "1075501004",
                        # "officialLevel":None,
                        "recommenderNo": "000003",
                        # "relatedLoanNo":None,
                        "operateUserName": None,
                        "operateAssistantUserName": None,
                        "departmentName": None,
                        "interviewerName": None,
                        "interviewCenterName": None,
                        "crChannelName": None,
                        "insurancePolicy1": "01",
                        "insurancePolicy2": None,
                        "insurancePolicy3": None,
                        "providentFundBase": None,
                        "providentFundCompany": None,
                        "isRecommendedByOld": "0"
                    },
                    "approvalComments": {
                        "opinionType": "010"
                    },
                    "recordingAging": {
                        "startInputDate": get_time.year_mont_day(),
                        "startInputTime": get_time.hour_min_sec(),
                        "endInputDate": get_time.year_mont_day(),
                        "endInputTime": get_time.hour_min_sec()
                    }
                }
                req_data.update(img_info)
                log_record('提交【民泰银行】申请单', sys._getframe().f_lineno, req_data)
                break
            else:
                img_info = img.upload_hxb_img()
                if time.time() - start_time > 15:
                    break

        try:
            response = requests.post(
                url=config.wk_submit_default_url,
                json=req_data
            )
            return response.json()

        except Exception as e:
            return e

    if business_type == config.business_type['LFB'][0]:

        # 获取指定业务品种的银行卡号
        loan_card_id = config.bank_no['LFB']

        # 获取指定业务类型的附件类型
        img = UploadImg()
        img_info = img.upload_lfb_img()

        #print('LFB:', img_info)

        start_time = time.time()
        while True:
            if img_info:
                req_data = {
                    "operatorType": "commitTask",
                    "state": "0010",
                    "properties": "NOTXD",
                    "businessType": business_type,
                    "applyType": "NormalApply",
                    "identityInfo": {
                        "idCode": get_user_info[1],
                        "idName": get_user_info[0],
                        "idSex": "男",
                        "idNation": "汉",
                        "idBirthday": get_user_info[4],
                        "idAddress": "广东省深圳市南山区",
                        "idIssuedBy": "南山公安局",
                        "idEffectDate": get_time.year_mont_day(),
                        "idExpiredDate": "2099/08/15",
                        "idRecorder": "ZHAOSMB",
                        "recorderDate": get_time.year_mont_day(),
                        "recorderTime": "11:12:22"
                    },
                    "customerInfo": {
                        # "yjsName":"U2379743969395867655",
                        "certCode": get_user_info[1],
                        "certType": "Ind01",
                        "certExpiredDate": get_time.year_mont_day(),
                        "certIssuedPlace": "南山公安局",
                        "name": "濮阳怜",
                        "education": "01",
                        "marriage": "20",
                        "familyStatus": "2",
                        "email": None,
                        "familyAddProvince": "广东省",
                        "familyAddCity": "深圳市",
                        "familyAddDistrict": "南山区",
                        "familyAddress": "讯美科技广场",
                        "familyAddInfo": "备注信息",
                        "permanentLocation": "01",
                        "mobilePhone": get_user_info[2],
                        "mobilePhone2": "13425106229",
                        "houseAreaCode": "0755",
                        "housePhone": "88888888",
                        "qq": "578812638",
                        "localHouseFlag": "1",
                        "localHouseAddress": "讯美科技广场",
                        "monthIncome": "30000",
                        "sex": "1",
                        "birthday": get_user_info[4],
                        "postAddress": None,
                        "familyAddLatitude": "22.545504",
                        "familyAddLongitude": "113.946978"
                    },
                    "workInfo": {
                        "workBelongIndustry": "A01",
                        "workOrgName": "友金所",
                        "workOrgNameRemark": "友金所",
                        "workDepartment": "系统运营部",
                        "workNature": "10",
                        "workHeadship": "测试",
                        "workPosition": "10",
                        "workBeginDate": "2018/08",
                        "workEmployeeType": "010",
                        "workIndustryDate": "2014/07/28",
                        "workAreaCode": "0755",
                        "workPhone": "88888888",
                        "workExtensionNumber": None,
                        "workAddProvince": "广东省",
                        "workAddCity": "深圳市",
                        "workAddDistrict": "南山区",
                        "workAddress": "讯美科技广场",
                        "workAddInfo": "备注信息",
                        "businessLicenceCode": "578812638",
                        "registeredCapital": "50000",
                        "workAddLatitude": "22.545504",
                        "workAddLongitude": "113.946978",
                        "stockLot": "10",
                        "takingsMonthly": 50000000,
                        "profitMarginMonthly": 100
                    },
                    "contactsInfo": [
                        {
                            "type": "1",
                            "name": "唐一",
                            "relationship": "0301",
                            "phone": "66666666",
                            "phoneArea": "0755",
                            "phoneExtensionNum": None
                        },
                        {
                            "type": "2",
                            "name": "唐二",
                            "relationship": "0101",
                            "remark": None,
                            "phone": "13425106229",
                            "contactCertId": "33038219680410795X",
                            "contactWorkCorp": "友金普惠"
                        },
                        {
                            "type": "3",
                            "name": "唐三",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106228"
                        },
                        {
                            "type": "3",
                            "name": "唐四",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106227"
                        },
                        {
                            "type": "3",
                            "name": "唐五",
                            "relationship": "0202",
                            "remark": None,
                            "phone": "13425106226"
                        }
                    ],
                    "borrowingMatters": {
                        "businessType": business_type,
                        "businessSum": "500000",
                        "loanTerm": "24",
                        "purpose": "02",
                        "otherPurpose": '企业生产经营',
                        "mainReturnType": "1",
                        "returnPeriod": "1",
                        "repayCardId": get_user_info[3],
                        "repayBank": "000021",
                        "loanCardId": loan_card_id,
                        "loanBank": "000001",
                        "tradeSum": 55
                    },
                    "notCustomerMatters": {
                        "customerType": "002",
                        "loanType": "120",
                        "saleChannel": "006",
                        "crChannel": None,
                        "isCertifition": "1",
                        "recommender": "林****",
                        "recommenderTel": "15633560000",
                        "interviewerId": "ZHAOSMB",
                        "interviewCenter": "755001",
                        "operateUserId": "7550114",
                        "operateAssistantUser": "GAOJZA",
                        "operateOrgId": "75501",
                        "inputUserName": "ZHAOSMB",
                        "inputDate": get_time.year_mont_day(),
                        "teamCaptain": "CAIJMD",
                        "saleDirector": "XUJGB",
                        "branchDirector": "ZHONGFP",
                        "departmentId": "1075501004",
                        # "officialLevel":None,
                        "recommenderNo": "000003",
                        # "relatedLoanNo":None,
                        "operateUserName": None,
                        "operateAssistantUserName": None,
                        "departmentName": None,
                        "interviewerName": None,
                        "interviewCenterName": None,
                        "crChannelName": None,
                        "insurancePolicy1": "01",
                        "insurancePolicy2": None,
                        "insurancePolicy3": None,
                        "providentFundBase": None,
                        "providentFundCompany": None,
                        "isRecommendedByOld": "0"
                    },
                    "approvalComments": {
                        "opinionType": "010"
                    },
                    "recordingAging": {
                        "startInputDate": get_time.year_mont_day(),
                        "startInputTime": get_time.hour_min_sec(),
                        "endInputDate": get_time.year_mont_day(),
                        "endInputTime": get_time.hour_min_sec()
                    }
                }
                req_data.update(img_info)
                log_record('提交【廊坊银行】申请单', sys._getframe().f_lineno, req_data)
                break
            else:
                img_info = img.upload_hxb_img()
                if time.time() - start_time > 15:
                    break

        try:
            response = requests.post(
                url=config.wk_submit_default_url,
                json=req_data
            )
            return response.json()

        except Exception as e:
            return e

    if business_type == config.business_type['XWB'][0]:


        # 获取指定业务类型的附件类型
        img = UploadImg()
        img_info = img.upload_xwb_img()
        #print('XWB:', img_info)
        start_time = time.time()
        while True:
            if img_info:
                req_data = {
                    "operatorType": "commitTask",
                    "state": "0010",
                    "properties": "NOTXD",
                    "businessType": business_type,
                    "applyType": "NormalApply",
                    "identityInfo": {
                        "idCode": get_user_info[1],
                        "idName": get_user_info[0],
                        "idSex": "男",
                        "idNation": "汉",
                        "idBirthday": get_user_info[4],
                        "idAddress": "广东省深圳市南山区",
                        "idIssuedBy": "南山公安局",
                        "idEffectDate": get_time.year_mont_day(),
                        "idExpiredDate": "2099/08/15",
                        "idRecorder": "ZHAOSMB",
                        "recorderDate": get_time.year_mont_day(),
                        "recorderTime": "11:12:22"
                    },
                    "customerInfo": {
                        # "yjsName":"U2379743969395867655",
                        "certCode": get_user_info[1],
                        "certType": "Ind01",
                        "certExpiredDate": get_time.year_mont_day(),
                        "certIssuedPlace": "南山公安局",
                        "name": "濮阳怜",
                        "education": "01",
                        "marriage": "20",
                        "familyStatus": "2",
                        "email": None,
                        "familyAddProvince": "广东省",
                        "familyAddCity": "深圳市",
                        "familyAddDistrict": "南山区",
                        "familyAddress": "讯美科技广场",
                        "familyAddInfo": "备注信息",
                        "permanentLocation": "01",
                        "mobilePhone": get_user_info[2],
                        "mobilePhone2": "13425106229",
                        "houseAreaCode": "0755",
                        "housePhone": "88888888",
                        "qq": "578812638",
                        "localHouseFlag": "1",
                        "localHouseAddress": "讯美科技广场",
                        "monthIncome": "30000",
                        "sex": "1",
                        "birthday": get_user_info[4],
                        "postAddress": None,
                        "familyAddLatitude": "22.545504",
                        "familyAddLongitude": "113.946978"
                    },
                    "workInfo": {
                        "workBelongIndustry": "A01",
                        "workOrgName": "友金所",
                        "workOrgNameRemark": "友金所",
                        "workDepartment": "系统运营部",
                        "workNature": "10",
                        "workHeadship": "测试",
                        "workPosition": "10",
                        "workBeginDate": "2018/08",
                        "workEmployeeType": "010",
                        "workIndustryDate": "2014/07/28",
                        "workAreaCode": "0755",
                        "workPhone": "88888888",
                        "workExtensionNumber": None,
                        "workAddProvince": "广东省",
                        "workAddCity": "深圳市",
                        "workAddDistrict": "南山区",
                        "workAddress": "讯美科技广场",
                        "workAddInfo": "备注信息",
                        "shareholdingRatio":"50",
                        "businessLicenceCode":"51370181MJD77237X5",
                        "registeredCapital":"5000000",
                        "paiclUpCapital":"5000000",
                        "employeesNum" :"10000",
                        "businessLocation": "北京市海淀区东北旺西路8号院35号楼5层501室",
                        "businessYear":"10",
                        "mainBusiness":"电子设备",
                        "businessAnnualIncome":"2000000",
                        "annualGrossProfit":"1000000",
                        "recent6MonthTurnover":"200000",
                        "recent6MonthSaleOrders":"100000",
                        "businessLicenceCode": "578812638",
                        "registeredCapital": "50000",
                        "workAddLatitude": "22.545504",
                        "workAddLongitude": "113.946978",
                        "stockLot": "10",
                        "takingsMonthly": 50000000,
                        "profitMarginMonthly": 100
                    },
                    "contactsInfo": [
                        {
                            "type": "1",
                            "name": "唐一",
                            "relationship": "0301",
                            "phone": "66666666",
                            "phoneArea": "0755",
                            "phoneExtensionNum": None
                        },
                        {
                            "type": "2",
                            "name": "唐二",
                            "relationship": "0101",
                            "remark": None,
                            "phone": "13425106229",
                            "contactCertId": "33038219680410795X",
                            "contactWorkCorp": "友金普惠"
                        },
                        {
                            "type": "3",
                            "name": "唐三",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106228"
                        },
                        {
                            "type": "3",
                            "name": "唐四",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106227"
                        },
                        {
                            "type": "3",
                            "name": "唐五",
                            "relationship": "0202",
                            "remark": None,
                            "phone": "13425106226"
                        }
                    ],
                    "borrowingMatters": {
                        "businessType": business_type,
                        "businessSum": "320000",
                        "loanTerm": "24",
                        "purpose": "02",
                        "otherPurpose": '企业生产经营',
                        "mainReturnType": "1",
                        "returnPeriod": "1",
                        "repayCardId": get_user_info[3],
                        "repayBank": "000001",
                        "loanCardId": get_user_info[3],
                        "loanBank": "000001",
                        "tradeSum": 55
                    },
                    "notCustomerMatters": {
                        "customerType": "002",
                        "loanType": "120",
                        "saleChannel": "006",
                        "crChannel": None,
                        "isCertifition": "1",
                        "recommender": "林****",
                        "recommenderTel": "15633560000",
                        "interviewerId": "ZHAOSMB",
                        "interviewCenter": "755001",
                        "operateUserId": "7550114",
                        "operateAssistantUser": "GAOJZA",
                        "operateOrgId": "75501",
                        "inputUserName": "ZHAOSMB",
                        "inputDate": get_time.year_mont_day(),
                        "teamCaptain": "CAIJMD",
                        "saleDirector": "XUJGB",
                        "branchDirector": "ZHONGFP",
                        "departmentId": "1075501004",

                        # "officialLevel":None,
                        "recommenderNo": "000003",
                        # "relatedLoanNo":None,
                        "operateUserName": None,
                        "operateAssistantUserName": None,
                        "departmentName": None,
                        "interviewerName": None,
                        "interviewCenterName": None,
                        "crChannelName": None,
                        "insurancePolicy1": "01",
                        "insurancePolicy2": None,
                        "insurancePolicy3": None,
                        "providentFundBase": None,
                        "providentFundCompany": None,
                        "isRecommendedByOld": "0"
                    },
                    "approvalComments": {
                        "opinionType": "010"
                    },
                    "recordingAging": {
                        "startInputDate": get_time.year_mont_day(),
                        "startInputTime": get_time.hour_min_sec(),
                        "endInputDate": get_time.year_mont_day(),
                        "endInputTime": get_time.hour_min_sec()
                    }
                }
                req_data.update(img_info)
                log_record('提交【新网银行】申请单', sys._getframe().f_lineno, req_data)
                break
            else:
                img_info = img.upload_hxb_img()
                if time.time() - start_time > 15:
                    break

        try:
            response = requests.post(
                url=config.wk_submit_default_url,
                json=req_data
            )
            return response.json()

        except Exception as e:
            return e

    if business_type == config.business_type['CCNS'][0]:

        # 获取指定业务品种的银行卡号
        loan_card_id = config.bank_no['CCNS']
        #print('loan_card_id:',loan_card_id)

        # 获取指定业务类型的附件类型
        img = UploadImg()
        img_info = img.upload_ccns_img()
        #print('CCNS:', img_info)

        start_time = time.time()
        while True:
            if img_info:
                req_data = {
                    "operatorType": "commitTask",
                    "state": "0010",
                    "properties": "NOTXD",
                    "businessType": business_type,
                    "applyType": "NormalApply",
                    "identityInfo": {
                        "idCode": get_user_info[1],
                        "idName": get_user_info[0],
                        "idSex": "男",
                        "idNation": "汉",
                        "idBirthday": get_user_info[4],
                        "idAddress": "广东省深圳市南山区",
                        "idIssuedBy": "南山公安局",
                        "idEffectDate": get_time.year_mont_day(),
                        "idExpiredDate": "2099/08/15",
                        "idRecorder": "ZHAOSMB",
                        "recorderDate": get_time.year_mont_day(),
                        "recorderTime": "11:12:22"
                    },
                    "customerInfo": {
                        # "yjsName":"U2379743969395867655",
                        "certCode": get_user_info[1],
                        "certType": "Ind01",
                        "certExpiredDate": get_time.year_mont_day(),
                        "certIssuedPlace": "南山公安局",
                        "name": "濮阳怜",
                        "education": "01",
                        "marriage": "20",
                        "familyStatus": "2",
                        "email": None,
                        "familyAddProvince": "广东省",
                        "familyAddCity": "深圳市",
                        "familyAddDistrict": "南山区",
                        "familyAddress": "讯美科技广场",
                        "familyAddInfo": "备注信息",
                        "permanentLocation": "01",
                        "mobilePhone": get_user_info[2],
                        "mobilePhone2": "13425106229",
                        "houseAreaCode": "0755",
                        "housePhone": "88888888",
                        "qq": "578812638",
                        "localHouseFlag": "1",
                        "localHouseAddress": "讯美科技广场",
                        "monthIncome": "30000",
                        "sex": "1",
                        "birthday": get_user_info[4],
                        "postAddress": None,
                        "familyAddLatitude": "22.545504",
                        "familyAddLongitude": "113.946978"
                    },
                    "workInfo": {
                        "workBelongIndustry": "A01",
                        "workOrgName": "友金所",
                        "workOrgNameRemark": "友金所",
                        "workDepartment": "系统运营部",
                        "workNature": "10",
                        "workHeadship": "测试",
                        "workPosition": "10",
                        "workBeginDate": "2018/08",
                        "workEmployeeType": "010",
                        "workIndustryDate": "2014/07/28",
                        "workAreaCode": "0755",
                        "workPhone": "88888888",
                        "workExtensionNumber": None,
                        "workAddProvince": "广东省",
                        "workAddCity": "深圳市",
                        "workAddDistrict": "南山区",
                        "workAddress": "讯美科技广场",
                        "workAddInfo": "备注信息",
                        "businessLicenceCode": "578812638",
                        "registeredCapital": "50000",
                        "workAddLatitude": "22.545504",
                        "workAddLongitude": "113.946978",
                        "stockLot": "10",
                        "takingsMonthly": 50000000,
                        "profitMarginMonthly": 100
                    },
                    "contactsInfo": [
                        {
                            "type": "1",
                            "name": "唐一",
                            "relationship": "0301",
                            "phone": "66666666",
                            "phoneArea": "0755",
                            "phoneExtensionNum": None
                        },
                        {
                            "type": "2",
                            "name": "唐二",
                            "relationship": "0101",
                            "remark": None,
                            "phone": "13425106229",
                            "contactCertId": "33038219680410795X",
                            "contactWorkCorp": "友金普惠"
                        },
                        {
                            "type": "3",
                            "name": "唐三",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106228"
                        },
                        {
                            "type": "3",
                            "name": "唐四",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106227"
                        },
                        {
                            "type": "3",
                            "name": "唐五",
                            "relationship": "0202",
                            "remark": None,
                            "phone": "13425106226"
                        }
                    ],
                    "borrowingMatters": {
                        "businessType": business_type,
                        "businessSum": "500000",
                        "loanTerm": "24",
                        "purpose": "02",
                        "otherPurpose": '企业生产经营',
                        "mainReturnType": "1",
                        "returnPeriod": "1",
                        "repayCardId": get_user_info[3],
                        "repayBank": "000023",
                        "loanCardId": loan_card_id,
                        "loanBank": "000001",
                        "tradeSum": 55
                    },
                    "notCustomerMatters": {
                        "customerType": "002",
                        "loanType": "120",
                        "saleChannel": "006",
                        "crChannel": None,
                        "isCertifition": "1",
                        "recommender": "林****",
                        "recommenderTel": "15633560000",
                        "interviewerId": "ZHAOSMB",
                        "interviewCenter": "755001",
                        "operateUserId": "7550114",
                        "operateAssistantUser": "GAOJZA",
                        "operateOrgId": "75501",
                        "inputUserName": "ZHAOSMB",
                        "inputDate": get_time.year_mont_day(),
                        "teamCaptain": "CAIJMD",
                        "saleDirector": "XUJGB",
                        "branchDirector": "ZHONGFP",
                        "departmentId": "1075501004",
                        # "officialLevel":None,
                        "recommenderNo": "000003",
                        # "relatedLoanNo":None,
                        "operateUserName": None,
                        "operateAssistantUserName": None,
                        "departmentName": None,
                        "interviewerName": None,
                        "interviewCenterName": None,
                        "crChannelName": None,
                        "insurancePolicy1": "01",
                        "insurancePolicy2": None,
                        "insurancePolicy3": None,
                        "providentFundBase": None,
                        "providentFundCompany": None,
                        "isRecommendedByOld": "0"
                    },
                    "insuranceInfo":[{
                        "keys":[
                            1],
                        "insuranceCompany1":"平安人寿",
                        "insuranceName1":"人寿保险",
                        "paymentType1":"4",
                        "premiumPayment1":"10000",
                        "effectiveDate1":"2010-01-0"
                    }],
                    "approvalComments": {
                        "opinionType": "010"
                    },
                    "recordingAging": {
                        "startInputDate": get_time.year_mont_day(),
                        "startInputTime": get_time.hour_min_sec(),
                        "endInputDate": get_time.year_mont_day(),
                        "endInputTime": get_time.hour_min_sec()
                    }
                }
                req_data.update(img_info)
                #print('req_data:',req_data)
                log_record('提交【长春农商】申请单', sys._getframe().f_lineno, req_data)
                break
            else:
                img_info = img.upload_hxb_img()
                if time.time() - start_time > 15:
                    break

        try:
            response = requests.post(
                url=config.wk_submit_default_url,
                json=req_data
            )
            return response.json()

        except Exception as e:
            return e

    if business_type == config.business_type['ZLJR'][0]:

        # 获取指定业务类型的附件类型
        img = UploadImg()
        img_info = img.upload_zljr_img()
        #print('ZLJR:', img_info)
        start_time = time.time()
        while True:
            if img_info:
                req_data = {
                    "operatorType": "commitTask",
                    "state": "0010",
                    "properties": "NOTXD",
                    "businessType": business_type,
                    "applyType": "NormalApply",
                    "identityInfo": {
                        "idCode": get_user_info[1],
                        "idName": get_user_info[0],
                        "idSex": "男",
                        "idNation": "汉",
                        "idBirthday": get_user_info[4],
                        "idAddress": "广东省深圳市南山区",
                        "idIssuedBy": "南山公安局",
                        "idEffectDate": get_time.year_mont_day(),
                        "idExpiredDate": "2099/08/15",
                        "idRecorder": "ZHAOSMB",
                        "recorderDate": get_time.year_mont_day(),
                        "recorderTime": "11:12:22"
                    },
                    "customerInfo": {
                        # "yjsName":"U2379743969395867655",
                        "certCode": get_user_info[1],
                        "certType": "Ind01",
                        "certExpiredDate": get_time.year_mont_day(),
                        "certIssuedPlace": "南山公安局",
                        "name": "濮阳怜",
                        "education": "01",
                        "marriage": "20",
                        "familyStatus": "2",
                        "email": None,
                        "familyAddProvince": "广东省",
                        "familyAddCity": "深圳市",
                        "familyAddDistrict": "南山区",
                        "familyAddress": "讯美科技广场",
                        "familyAddInfo": "备注信息",
                        "permanentLocation": "01",
                        "mobilePhone": get_user_info[2],
                        "mobilePhone2": "13425106229",
                        "houseAreaCode": "0755",
                        "housePhone": "88888888",
                        "qq": "578812638",
                        "localHouseFlag": "1",
                        "localHouseAddress": "讯美科技广场",
                        "monthIncome": "30000",
                        "sex": "1",
                        "birthday": get_user_info[4],
                        "postAddress": None,
                        "familyAddLatitude": "22.545504",
                        "familyAddLongitude": "113.946978"
                    },
                    "workInfo": {
                        "workBelongIndustry": "A01",
                        "workOrgName": "友金所",
                        "workOrgNameRemark": "友金所",
                        "workDepartment": "系统运营部",
                        "workNature": "10",
                        "workHeadship": "测试",
                        "workPosition": "10",
                        "workBeginDate": "2018/08",
                        "workEmployeeType": "010",
                        "workIndustryDate": "2014/07/28",
                        "workAreaCode": "0755",
                        "workPhone": "88888888",
                        "workExtensionNumber": None,
                        "workAddProvince": "广东省",
                        "workAddCity": "深圳市",
                        "workAddDistrict": "南山区",
                        "workAddress": "讯美科技广场",
                        "workAddInfo": "备注信息",
                        "businessLicenceCode": "578812638",
                        "registeredCapital": "50000",
                        "workAddLatitude": "22.545504",
                        "workAddLongitude": "113.946978",
                        "stockLot": "10",
                        "takingsMonthly": 50000000,
                        "profitMarginMonthly": 100
                    },
                    "contactsInfo": [
                        {
                            "type": "1",
                            "name": "唐一",
                            "relationship": "0301",
                            "phone": "66666666",
                            "phoneArea": "0755",
                            "phoneExtensionNum": None
                        },
                        {
                            "type": "2",
                            "name": "唐二",
                            "relationship": "0101",
                            "remark": None,
                            "phone": "13425106229",
                            "contactCertId": "33038219680410795X",
                            "contactWorkCorp": "友金普惠"
                        },
                        {
                            "type": "3",
                            "name": "唐三",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106228"
                        },
                        {
                            "type": "3",
                            "name": "唐四",
                            "relationship": "0201",
                            "remark": None,
                            "phone": "13425106227"
                        },
                        {
                            "type": "3",
                            "name": "唐五",
                            "relationship": "0202",
                            "remark": None,
                            "phone": "13425106226"
                        }
                    ],
                    "borrowingMatters": {
                        "businessType": business_type,
                        "businessSum": "500000",
                        "loanTerm": "24",
                        "purpose": "02",
                        "otherPurpose": '企业生产经营',
                        "mainReturnType": "1",
                        "returnPeriod": "1",
                        "repayCardId": get_user_info[3],
                        "repayBank": "000001",
                        "loanCardId": get_user_info[3],
                        "loanBank": "000001",
                        "tradeSum": 55
                    },
                    "notCustomerMatters": {
                        "customerType": "002",
                        "loanType": "120",
                        "saleChannel": "006",
                        "crChannel": None,
                        "isCertifition": "1",
                        "recommender": "林****",
                        "recommenderTel": "15633560000",
                        "interviewerId": "ZHAOSMB",
                        "interviewCenter": "755001",
                        "operateUserId": "7550114",
                        "operateAssistantUser": "GAOJZA",
                        "operateOrgId": "75501",
                        "inputUserName": "ZHAOSMB",
                        "inputDate": get_time.year_mont_day(),
                        "teamCaptain": "CAIJMD",
                        "saleDirector": "XUJGB",
                        "branchDirector": "ZHONGFP",
                        "departmentId": "1075501004",
                        # "officialLevel":None,
                        "recommenderNo": "000003",
                        # "relatedLoanNo":None,
                        "operateUserName": None,
                        "operateAssistantUserName": None,
                        "departmentName": None,
                        "interviewerName": None,
                        "interviewCenterName": None,
                        "crChannelName": None,
                        "insurancePolicy1": "01",
                        "insurancePolicy2": None,
                        "insurancePolicy3": None,
                        "providentFundBase": None,
                        "providentFundCompany": None,
                        "isRecommendedByOld": "0"
                    },
                    "approvalComments": {
                        "opinionType": "010"
                    },
                    "recordingAging": {
                        "startInputDate": get_time.year_mont_day(),
                        "startInputTime": get_time.hour_min_sec(),
                        "endInputDate": get_time.year_mont_day(),
                        "endInputTime": get_time.hour_min_sec()
                    }
                }
                req_data.update(img_info)
                log_record('提交【招联金融】申请单', sys._getframe().f_lineno, req_data)
                break
            else:
                img_info = img.upload_hxb_img()
                if time.time() - start_time > 15:
                    break

        try:
            response = requests.post(
                url=config.wk_submit_default_url,
                json=req_data
            )
            return response.json()

        except Exception as e:
            return e

    else:
        if business_type == config.business_type['CDB'][0]:

            # 获取指定业务品种的银行卡号
            loan_card_id = config.bank_no['CDB']

            # 获取指定业务类型的附件类型
            img = UploadImg()
            img_info = img.upload_currency_img()

            #print('CDB:', img_info)

            start_time = time.time()
            while True:
                if img_info:
                    req_data = {
                        "operatorType": "commitTask",
                        "state": "0010",
                        "properties": "NOTXD",
                        "businessType": business_type,
                        "applyType": "NormalApply",
                        "identityInfo": {
                            "idCode": get_user_info[1],
                            "idName": get_user_info[0],
                            "idSex": "男",
                            "idNation": "汉",
                            "idBirthday": get_user_info[4],
                            "idAddress": "广东省深圳市南山区",
                            "idIssuedBy": "南山公安局",
                            "idEffectDate": get_time.year_mont_day(),
                            "idExpiredDate": "2099/08/15",
                            "idRecorder": "ZHAOSMB",
                            "recorderDate": get_time.year_mont_day(),
                            "recorderTime": "11:12:22"
                        },
                        "customerInfo": {
                            # "yjsName":"U2379743969395867655",
                            "certCode": get_user_info[1],
                            "certType": "Ind01",
                            "certExpiredDate": get_time.year_mont_day(),
                            "certIssuedPlace": "南山公安局",
                            "name": "濮阳怜",
                            "education": "01",
                            "marriage": "20",
                            "familyStatus": "2",
                            "email": None,
                            "familyAddProvince": "广东省",
                            "familyAddCity": "深圳市",
                            "familyAddDistrict": "南山区",
                            "familyAddress": "讯美科技广场",
                            "familyAddInfo": "备注信息",
                            "permanentLocation": "01",
                            "mobilePhone": get_user_info[2],
                            "mobilePhone2": "13425106229",
                            "houseAreaCode": "0755",
                            "housePhone": "88888888",
                            "qq": "578812638",
                            "localHouseFlag": "1",
                            "localHouseAddress": "讯美科技广场",
                            "monthIncome": "30000",
                            "sex": "1",
                            "birthday": get_user_info[4],
                            "postAddress": None,
                            "familyAddLatitude": "22.545504",
                            "familyAddLongitude": "113.946978"
                        },
                        "workInfo": {
                            "workBelongIndustry": "A01",
                            "workOrgName": "友金所",
                            "workOrgNameRemark": "友金所",
                            "workDepartment": "系统运营部",
                            "workNature": "10",
                            "workHeadship": "测试",
                            "workPosition": "10",
                            "workBeginDate": "2018/08",
                            "workEmployeeType": "010",
                            "workIndustryDate": "2014/07/28",
                            "workAreaCode": "0755",
                            "workPhone": "88888888",
                            "workExtensionNumber": None,
                            "workAddProvince": "广东省",
                            "workAddCity": "深圳市",
                            "workAddDistrict": "南山区",
                            "workAddress": "讯美科技广场",
                            "workAddInfo": "备注信息",
                            "businessLicenceCode": "578812638",
                            "registeredCapital": "50000",
                            "workAddLatitude": "22.545504",
                            "workAddLongitude": "113.946978",
                            "stockLot": "10",
                            "takingsMonthly": 50000000,
                            "profitMarginMonthly": 100
                        },
                        "contactsInfo": [
                            {
                                "type": "1",
                                "name": "唐一",
                                "relationship": "0301",
                                "phone": "66666666",
                                "phoneArea": "0755",
                                "phoneExtensionNum": None
                            },
                            {
                                "type": "2",
                                "name": "唐二",
                                "relationship": "0101",
                                "remark": None,
                                "phone": "13425106229",
                                "contactCertId": "33038219680410795X",
                                "contactWorkCorp": "友金普惠"
                            },
                            {
                                "type": "3",
                                "name": "唐三",
                                "relationship": "0201",
                                "remark": None,
                                "phone": "13425106228"
                            },
                            {
                                "type": "3",
                                "name": "唐四",
                                "relationship": "0201",
                                "remark": None,
                                "phone": "13425106227"
                            },
                            {
                                "type": "3",
                                "name": "唐五",
                                "relationship": "0202",
                                "remark": None,
                                "phone": "13425106226"
                            }
                        ],
                        "borrowingMatters": {
                            "businessType": business_type,
                            "businessSum": "500000",
                            "loanTerm": "24",
                            "purpose": "02",
                            "otherPurpose": '企业生产经营',
                            "mainReturnType": "1",
                            "returnPeriod": "1",
                            "repayCardId": get_user_info[3],
                            "repayBank": "000019",
                            "loanCardId": loan_card_id,
                            "loanBank": "000001",
                            "tradeSum": 55
                        },
                        "notCustomerMatters": {
                            "customerType": "002",
                            "loanType": "120",
                            "saleChannel": "006",
                            "crChannel": None,
                            "isCertifition": "1",
                            "recommender": "林****",
                            "recommenderTel": "15633560000",
                            "interviewerId": "ZHAOSMB",
                            "interviewCenter": "755001",
                            "operateUserId": "7550114",
                            "operateAssistantUser": "GAOJZA",
                            "operateOrgId": "75501",
                            "inputUserName": "ZHAOSMB",
                            "inputDate": get_time.year_mont_day(),
                            "teamCaptain": "CAIJMD",
                            "saleDirector": "XUJGB",
                            "branchDirector": "ZHONGFP",
                            "departmentId": "1075501004",
                            # "officialLevel":None,
                            "recommenderNo": "000003",
                            # "relatedLoanNo":None,
                            "operateUserName": None,
                            "operateAssistantUserName": None,
                            "departmentName": None,
                            "interviewerName": None,
                            "interviewCenterName": None,
                            "crChannelName": None,
                            "insurancePolicy1": "01",
                            "insurancePolicy2": None,
                            "insurancePolicy3": None,
                            "providentFundBase": None,
                            "providentFundCompany": None,
                            "isRecommendedByOld": "0"
                        },
                        "approvalComments": {
                            "opinionType": "010"
                        },
                        "recordingAging": {
                            "startInputDate": get_time.year_mont_day(),
                            "startInputTime": get_time.hour_min_sec(),
                            "endInputDate": get_time.year_mont_day(),
                            "endInputTime": get_time.hour_min_sec()
                        }
                    }
                    req_data.update(img_info)
                    log_record('提交【承德银行】申请单', sys._getframe().f_lineno, req_data)
                    break
                else:
                    img_info = img.upload_hxb_img()
                    if time.time() - start_time > 15:
                        break

            try:
                response = requests.post(
                    url=config.wk_submit_default_url,
                    json=req_data
                )
                return response.json()

            except Exception as e:
                return e

        else:

            #获取到其他业务类型的中文名称
            for k,v in config.business_type.items():
                if v[0] ==  business_type:
                    k_name = v[1]

            # 获取指定业务类型的附件类型
            img = UploadImg()
            img_info = img.upload_currency_img()
            #print('other:',img_info)
            start_time = time.time()
            while True:
                if img_info:
                    req_data = {
                        "operatorType": "commitTask",
                        "state": "0010",
                        "properties": "NOTXD",
                        "businessType": business_type,
                        "applyType": "NormalApply",
                        "identityInfo": {
                            "idCode": get_user_info[1],
                            "idName": get_user_info[0],
                            "idSex": "男",
                            "idNation": "汉",
                            "idBirthday": get_user_info[4],
                            "idAddress": "广东省深圳市南山区",
                            "idIssuedBy": "南山公安局",
                            "idEffectDate": get_time.year_mont_day(),
                            "idExpiredDate": "2099/08/15",
                            "idRecorder": "ZHAOSMB",
                            "recorderDate": get_time.year_mont_day(),
                            "recorderTime": "11:12:22"
                        },
                        "customerInfo": {
                            # "yjsName":"U2379743969395867655",
                            "certCode": get_user_info[1],
                            "certType": "Ind01",
                            "certExpiredDate": get_time.year_mont_day(),
                            "certIssuedPlace": "南山公安局",
                            "name": "濮阳怜",
                            "education": "01",
                            "marriage": "20",
                            "familyStatus": "2",
                            "email": None,
                            "familyAddProvince": "广东省",
                            "familyAddCity": "深圳市",
                            "familyAddDistrict": "南山区",
                            "familyAddress": "讯美科技广场",
                            "familyAddInfo": "备注信息",
                            "permanentLocation": "01",
                            "mobilePhone": get_user_info[2],
                            "mobilePhone2": "13425106229",
                            "houseAreaCode": "0755",
                            "housePhone": "88888888",
                            "qq": "578812638",
                            "localHouseFlag": "1",
                            "localHouseAddress": "讯美科技广场",
                            "monthIncome": "30000",
                            "sex": "1",
                            "birthday": get_user_info[4],
                            "postAddress": None,
                            "familyAddLatitude": "22.545504",
                            "familyAddLongitude": "113.946978"
                        },
                        "workInfo": {
                            "workBelongIndustry": "A01",
                            "workOrgName": "友金所",
                            "workOrgNameRemark": "友金所",
                            "workDepartment": "系统运营部",
                            "workNature": "10",
                            "workHeadship": "测试",
                            "workPosition": "10",
                            "workBeginDate": "2018/08",
                            "workEmployeeType": "010",
                            "workIndustryDate": "2014/07/28",
                            "workAreaCode": "0755",
                            "workPhone": "88888888",
                            "workExtensionNumber": None,
                            "workAddProvince": "广东省",
                            "workAddCity": "深圳市",
                            "workAddDistrict": "南山区",
                            "workAddress": "讯美科技广场",
                            "workAddInfo": "备注信息",
                            "businessLicenceCode": "578812638",
                            "registeredCapital": "50000",
                            "workAddLatitude": "22.545504",
                            "workAddLongitude": "113.946978",
                            "stockLot": "10",
                            "takingsMonthly": 50000000,
                            "profitMarginMonthly": 100
                        },
                        "contactsInfo": [
                            {
                                "type": "1",
                                "name": "唐一",
                                "relationship": "0301",
                                "phone": "66666666",
                                "phoneArea": "0755",
                                "phoneExtensionNum": None
                            },
                            {
                                "type": "2",
                                "name": "唐二",
                                "relationship": "0101",
                                "remark": None,
                                "phone": "13425106229",
                                "contactCertId": "33038219680410795X",
                                "contactWorkCorp": "友金普惠"
                            },
                            {
                                "type": "3",
                                "name": "唐三",
                                "relationship": "0201",
                                "remark": None,
                                "phone": "13425106228"
                            },
                            {
                                "type": "3",
                                "name": "唐四",
                                "relationship": "0201",
                                "remark": None,
                                "phone": "13425106227"
                            },
                            {
                                "type": "3",
                                "name": "唐五",
                                "relationship": "0202",
                                "remark": None,
                                "phone": "13425106226"
                            }
                        ],
                        "borrowingMatters": {
                            "businessType": business_type,
                            "businessSum": "500000",
                            "loanTerm": "24",
                            "purpose": "02",
                            'nbtsEleAccount':'578812638578812638888',
                            "otherPurpose": '企业生产经营',
                            "mainReturnType": "1",
                            "returnPeriod": "1",
                            "repayCardId": get_user_info[3],
                            "repayBank": "000001",
                            "loanCardId": get_user_info[3],
                            "loanBank": "000001",
                            "tradeSum": 55
                        },
                        "notCustomerMatters": {
                            "customerType": "002",
                            "loanType": "120",
                            "saleChannel": "006",
                            "crChannel": None,
                            "isCertifition": "1",
                            "recommender": "林****",
                            "recommenderTel": "15633560000",
                            "interviewerId": "ZHAOSMB",
                            "interviewCenter": "755001",
                            "operateUserId": "7550114",
                            "operateAssistantUser": "GAOJZA",
                            "operateOrgId": "75501",
                            "inputUserName": "ZHAOSMB",
                            "inputDate": get_time.year_mont_day(),
                            "teamCaptain": "CAIJMD",
                            "saleDirector": "XUJGB",
                            "branchDirector": "ZHONGFP",
                            "departmentId": "1075501004",
                            # "officialLevel":None,
                            "recommenderNo": "000003",
                            # "relatedLoanNo":None,
                            "operateUserName": None,
                            "operateAssistantUserName": None,
                            "departmentName": None,
                            "interviewerName": None,
                            "interviewCenterName": None,
                            "crChannelName": None,
                            "insurancePolicy1": "01",
                            "insurancePolicy2": None,
                            "insurancePolicy3": None,
                            "providentFundBase": None,
                            "providentFundCompany": None,
                            "isRecommendedByOld": "0"
                        },
                        "approvalComments": {
                            "opinionType": "010"
                        },
                        "recordingAging": {
                            "startInputDate": get_time.year_mont_day(),
                            "startInputTime": get_time.hour_min_sec(),
                            "endInputDate": get_time.year_mont_day(),
                            "endInputTime": get_time.hour_min_sec()
                        }
                    }
                    req_data.update(img_info)
                    log_record('提交【%s】申请单'%k_name, sys._getframe().f_lineno, req_data)
                    break
                else:
                    img_info = img.upload_hxb_img()
                    if time.time() - start_time > 15:
                        break

            try:
                response = requests.post(
                    url=config.wk_submit_default_url,
                    json=req_data
                )
                return response.json()

            except Exception as e:
                return e



if __name__ == '__main__':
    pass

    # credit = CreditInquiry()
    # credit.save_to_mongoDB()



    # user_info = get_user_auth_info()
    # print(user_info)

    # credit_result = get_credit_result(user_info[1])
    # #print(credit_result)
    # log_record('获取当前时间',sys._getframe().f_lineno,get_self.current_time())


    # for _ in range(10):
    #     random_card_num = get_card_num('621469', 16)
    #     valid_result = check_card_num(random_card_num)
    #     #print('%s %s' % (random_card_num, valid_result))



      # res = submit(config.business_type['HXB'][0])
      # print(res)

    # dic = {'apply_id': 'NA20190817000033', 'state': '0050', 'sub_state': '0015'}
    # signal = WkEvent()
    # signal.signal()

    # wk = WkEvent()
    # wk.signal()

     # get_time = GetCurrentTime()
     # res = get_time.complete_time()
     # #print(res)

     # handel_credit = CreditInquiry()
     # handel_credit.save_to_mongoDB()

     # aes = EncryptAndDecrypt(key='0e80ab1f7c824152',iv='0102030405060708')
     # res = aes.aes_encrypt('513223198602189459')
     # print(res)
     # rr = aes.aes_decrypt('3IUWCJ9yC3VbRDTTlJnUuledDzkREYq+IXY+4TLgJviy94tyc0HQKgsvN348s1UaY0YTIR1enVlBos7yVe7CqD6UQ9ed7yzdPK0cZtEOSs7xqsUV4icml+D8gXc6WxlQOE2qaQABDgO7GD8Mfa0fDZiqogPA27aLrjqHQsWBCs7ONnH7wrvich46otGo8C+ZXdT2PhJDks0AvcSBXUrUA5QbhVs7jfd+MNgRCbl47PEgi75/BQaU261fhnUhkq1mJC7Z10tdRpsQDi/ZaE4aUYcF52Cv2wL8meLJfHRNfVTlvVIAze7StNzG8W+GugIAJ+lyz5cQ/OVVFbhhi/6SYe4dCBxljW/F5kD0WT7g/9AsaqxdIT8XlPYWeW7d1O/G11OgxTP8bX5jvlxmPlWAAbTggioAI12ZpHXqrVllNdtyphKlj1ge4aHfQTE+RQ6fu8VhQfPXqmK6sqsn9MHYU7TmcvNwYaP34AL')
     # print(rr)

     # get_user_auth_info()
    submit_result = submit('1101700')
    print('submit_result:',submit_result)




