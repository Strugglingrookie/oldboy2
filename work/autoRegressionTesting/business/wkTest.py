#coding=utf-8
import json
import os
import math
import time
import unittest
from urllib import request,parse
from config import Config
from business.phTest import PHTest
from business.wptTest import WPTTest
from tools.base import Base
from random import randint,choice
from selenium import webdriver


IMAGE = {
    'YJKD': [{"attachmentNo": "IM2019042000000001", "attachmentType": "A-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042000000002", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042000000003", "attachmentType": "A-99", "attachmentRealFileName": ""}],
    'XWBK': [{"attachmentNo": "IM2019042200000001", "attachmentType": "B-XW-03", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000002", "attachmentType": "B-XW-03", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000003", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000004", "attachmentType": "A-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000005", "attachmentType": "B-XW-02", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000006", "attachmentType": "B-XW-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000007", "attachmentType": "B-XW-06", "attachmentRealFileName": ""}],
    'CDBK': [{"attachmentNo": "IM2019042000000001", "attachmentType": "A-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019050600000107", "attachmentType": "A-04", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019050600000108", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019050600000109", "attachmentType": "A-03", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000199", "attachmentType": "A-06", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019050600000110", "attachmentType": "A-03", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019050600000111", "attachmentType": "A-10", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019050600000112", "attachmentType": "A-09", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000201", "attachmentType": "A-99", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000201", "attachmentType": "A-99", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000201", "attachmentType": "A-99", "attachmentRealFileName": ""}],
    'HXBK': [{"attachmentNo": "IM2019042200000048", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000049", "attachmentType": "B-HX-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000050", "attachmentType": "B-HX-03", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042200000052", "attachmentType": "B-HX-02", "attachmentRealFileName": ""}],
    'MTBK': [{"attachmentNo": "IM2019042500000193", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000195", "attachmentType": "B-MT-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000197", "attachmentType": "B-MT-02", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000198", "attachmentType": "B-MT-03", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000199", "attachmentType": "A-06", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000200", "attachmentType": "A-10", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042500000201", "attachmentType": "A-99", "attachmentRealFileName": ""}],
    'NJBK': [{"attachmentNo": "IM2019042800000194", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042800000195", "attachmentType": "B-NJ-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042800000199", "attachmentType": "B-NJ-02", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042800000198", "attachmentType": "B-NJ-03", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042800000196", "attachmentType": "B-NJ-04", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042800000197", "attachmentType": "B-NJ-05", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042800000200", "attachmentType": "A-10", "attachmentRealFileName": ""}],
    'NBTS': [{"attachmentNo": "IM2019042900000292", "attachmentType": "A-08", "attachmentRealFileName": ""}],
    'LFBK': [{"attachmentNo": "IM2019042900000182", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042900000185", "attachmentType": "B-LF-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042900000186", "attachmentType": "B-LF-02", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019042900000189", "attachmentType": "A-01", "attachmentRealFileName": ""}],
    'XGM': [{"attachmentNo": "IM2019043000000006", "attachmentType": "A-08", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019043000000007", "attachmentType": "A-10", "attachmentRealFileName": ""}],
    'SZS': [{"attachmentNo": "IM2019042800000159", "attachmentType": "A-01", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019042800000160", "attachmentType": "A-08", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019043000000007", "attachmentType": "A-10", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019042800000167", "attachmentType": "B-SZS-01", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019071600000647", "attachmentType": "B-SZS-02", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019071600000649", "attachmentType": "B-SZS-03", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019071600000648", "attachmentType": "B-SZS-04", "attachmentRealFileName": ""}],
    'ZGC': [{"attachmentNo": "IM2019043000000008", "attachmentType": "A-01", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019043000000009", "attachmentType": "A-08", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019043000000010", "attachmentType": "A-07", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019043000000011", "attachmentType": "A-10", "attachmentRealFileName": ""},
            {"attachmentNo": "IM2019043000000012", "attachmentType": "A-99", "attachmentRealFileName": ""}],
    'CCNS': [{"attachmentNo": "IM2019043000000017", "attachmentType": "B-CCNS-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019043000000018", "attachmentType": "B-CCNS-02", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019043000000019", "attachmentType": "B-CCNS-03", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019043000000020", "attachmentType": "B-CCNS-04", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019043000000021", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019043000000023", "attachmentType": "A-09", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019043000000022", "attachmentType": "A-10", "attachmentRealFileName": ""}],
    'ZLJR': [{"attachmentNo": "IM2019050600000031", "attachmentType": "A-08", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019050700000111", "attachmentType": "B-ZL-01", "attachmentRealFileName": ""},
             {"attachmentNo": "IM2019050700000112", "attachmentType": "B-ZL-02", "attachmentRealFileName": ""}]}


class WKTest(unittest.TestCase):
    configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yml")
    config = Config(configPath)
    curEnv = config.getCfgValue("curEnv")
    url = config.getCfgValue(curEnv, "WK", "url")
    businessType = None


    @classmethod
    def setUpClass(cls):  # 在所有用例执行之前运行的
        pass

    @classmethod
    def tearDownClass(cls):  # 在所有用例都执行完之后运行的
        pass

    def setUp(self):  # 每个用例运行之前运行的
        pass

    def tearDown(self):  # 每个用例运行之后运行的
        pass


    def orderSubmitYJKD(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                                 customerType, operatorOrgId, interviewCenter, departmentId, interviewerId, inputUserId,
                                 operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()

        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100100",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "一大菠菜",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100100",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["YJKD"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitYJD(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                             customerType, operatorOrgId, interviewCenter, departmentId, interviewerId, inputUserId,
                             operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        uid = PHTest().queryYYfaxUid(phone)
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100200",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "礼即常德",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100200",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": Base.autoGenerateBankCardNo("000015"),
                "loanBank": "000015",
                "lbTseleAccount": "%4d %04d %04d %04d %03d" % (
                    randint(1000, 9999), randint(0, 9999), randint(0, 9999),
                    randint(0, 9999),
                    randint(0, 999))
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["YJKD"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitLHXD(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                              customerType, operatorOrgId, interviewCenter, departmentId, interviewerId, inputUserId,
                              operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100300",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "五常牛肉",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100300",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["YJKD"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitZRB(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                             customerType, operatorOrgId, interviewCenter, departmentId, interviewerId, inputUserId,
                             operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100400",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "唐牛集团",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100400",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["YJKD"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitSZS(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                             customerType, operatorOrgId,
                             interviewCenter, departmentId, interviewerId, inputUserId, operatorUserId, recommenderTel,
                             recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100500",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "天山水莲",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3],
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100500",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode,
                "lbTseleAccount": "%4d %04d %04d %04d %03d" % (
                    randint(1000, 9999), randint(0, 9999), randint(0, 9999),
                    randint(0, 9999),
                    randint(0, 999))
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["SZS"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitHKbank(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                                   customerType, operatorOrgId, interviewCenter, departmentId, interviewerId,
                                   inputUserId,
                                   operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100600",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "花果山泉",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100600",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": Base.autoGenerateBankCardNo("000017"),
                "loanBank": "000017",
                "lbTseleAccount": "%4d %04d %04d %04d %03d" % (
                    randint(1000, 9999), randint(0, 9999), randint(0, 9999),
                    randint(0, 9999),
                    randint(0, 999))
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["YJKD"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitNBbank(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                                   customerType,
                                   operatorOrgId, interviewCenter, departmentId, interviewerId, inputUserId,
                                   operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100700",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "凯迪威烧烤",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100700",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode,
                "nbtsEleAccount": Base.autoGenerateBankCardNo("000018")
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["NBTS"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitZGC(self, phone, name, certId, bkCardNo, bkCode,
                                loanAmounts, loanType, loanTerm, customerType, operatorOrgId,
                                interviewCenter, departmentId, interviewerId, inputUserId, operatorUserId,
                                recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100800",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "英雄担保",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100800",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode,
                "lbTseleAccount": "%4d %04d %04d %04d %03d" % (
                    randint(1000, 9999), randint(0, 9999), randint(0, 9999),
                    randint(0, 9999),
                    randint(0, 999))
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["ZGC"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitXGM(self, phone, name, certId, bkCardNo, bkCode, loanAmounts,
                               loanType, loanTerm, customerType, operatorOrgId,
                             interviewCenter, departmentId, interviewerId, inputUserId,
                             operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1100900",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "RGB水冷",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1100900",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["XGM"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitHXbank(self, phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                  loanType, loanTerm, customerType, operatorOrgId,
                                interviewCenter, departmentId, interviewerId,
                                inputUserId, operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1101300",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "10",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": "北京小桔科技有限公司",  # base.autoGenerateCompName(),
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "010",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3],
                "stockLot": "50",
                "takingsMonthly": 1000000,
                "profitMarginMonthly": 50
            },
            "workInfoDTO": {
                "corpArea": "0755",
                "workTel": "12856320",
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1101300",
                "businessSum": loanAmounts,
                "tradeSum": int(math.ceil(int(loanAmounts) / 10000.0)),
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": Base.autoGenerateBankCardNo("000020"),
                "loanBank": "000020",
                "lbTseleAccount": "%4d %04d %04d %04d %03d" % (
                    randint(1000, 9999), randint(0, 9999), randint(0, 9999),
                    randint(0, 9999),
                    randint(0, 999))
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["HXBK"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitCDbank(self, phone, name, certId, bkCardNo, bkCode,
                                loanAmounts,
                                  loanType, loanTerm, customerType, operatorOrgId,
                                interviewCenter, departmentId, interviewerId,
                                inputUserId, operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1101200",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "劳动承接",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1101200",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": choice(
                    ["6230606601007717929", "6230606601007717937", "6230606601007717945", "6230606601007717952",
                     "6230606601007717960", "6230606601007717978", "6230606601007717986", "6230606601007717994",
                     "6230606601007718000", "6230606601007718018", "6230606601007718026", "6230606601007718034",
                     "6230606601007718042", "6230606601007718059", "6230606601007718067"]),
                "loanBank": "000019",
                "lbTseleAccount": "%4d %04d %04d %04d %03d" % (
                    randint(1000, 9999), randint(0, 9999), randint(0, 9999),
                    randint(0, 9999),
                    randint(0, 999))
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["CDBK"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitNJbank(self, phone, name, certId, bkCardNo, bkCode,
                                loanAmounts,
                                  loanType, loanTerm, customerType, operatorOrgId,
                                interviewCenter, departmentId, interviewerId,
                                inputUserId, operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1101400",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "没得课欧文",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1101400",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "loanPurpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["NJBK"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitLFbank(self, phone, name, certId, bkCardNo, bkCode,
                                loanAmounts,
                                  loanType, loanTerm, customerType, operatorOrgId,
                                interviewCenter, departmentId, interviewerId,
                                inputUserId, operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1101600",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "解耦IEN家",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1101600",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "loanPurpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": Base.autoGenerateBankCardNo("000021"),
                "loanBank": "000021"
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["LFBK"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitMTbank(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                                customerType, operatorOrgId, interviewCenter, departmentId, interviewerId, inputUserId,
                                operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1101500",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "克切克雕刻",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1101500",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode,
                "lbTseleAccount": "%4d %04d %04d %04d %03d" % (
                    randint(1000, 9999), randint(0, 9999), randint(0, 9999),
                    randint(0, 9999),
                    randint(0, 999))
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["MTBK"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitXWbank(self, phone, name, certId, bkCardNo, bkCode,
                                loanAmounts,
                                  loanType, loanTerm, customerType,
                                operatorOrgId, interviewCenter, departmentId, interviewerId,
                                inputUserId, operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1101700",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "解耦奥吉尔",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "测试",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3],
                "customerClass": "1",
                "shareholdingRatio": "51",
                "businessLicenceCode": "9145100058434245XC",
                "registeredCapital": "150000",
                "paiclUpCapital": "150000",
                "employeesNum": "3",
                "businessLocation": "北京市海淀区东北旺西路8号院35号楼5层501室",
                "businessYear": 7,
                "mainBusiness": "范德萨",
                "businessAnnualIncome": "151",
                "annualGrossProfit": "34.73",
                "recent6MonthTurnover": "75.5",
                "recent6MonthSaleOrders": "3000000"
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1101700",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["XWBK"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitCCNS(self, phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                loanType, loanTerm, customerType, operatorOrgId, interviewCenter, departmentId,
                              interviewerId,
                              inputUserId, operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1101800",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "吹风机都",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "安保人员",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1101800",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": Base.autoGenerateBankCardNo("000023"),
                "loanBank": "000023"
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["CCNS"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def orderSubmitZLJR(self, phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType, loanTerm,
                              customerType,
                              operatorOrgId, interviewCenter, departmentId, interviewerId,
                              inputUserId, operatorUserId, recommenderTel, recommender, NA):
        url = self.url + "/api/wpt/apply/submit"
        uid = PHTest().queryYYfaxUid(phone)
        birthday = certId[6:10] + "/" + certId[10:12] + "/" + certId[12:14]
        addr1 = Base.autoGenerateAddrs()
        addr2 = Base.autoGenerateAddrs()
        data = {
            "operatorType": "commitTask",
            "applyId": NA,
            "state": "0010",
            "properties": "NOTXD",
            "businessType": "1101900",
            "applyType": "NormalApply",
            "identityInfo": {
                "idCode": certId,
                "idName": name,
                "idSex": "男",
                "idNation": "汉",
                "idBirthday": birthday,
                "idAddress": "广东省深圳市南山区讯美科技广场",
                "idIssuedBy": "深圳市公安局",
                "idEffectDate": "2018/08/20",
                "idExpiredDate": "2039/06/29",
                "idRecorder": inputUserId,
                "recorderDate": time.strftime('%Y/%m/%d', time.localtime()),
                "recorderTime": "19:58:42"
            },
            "customerInfo": {
                "yjsName": uid,
                "certCode": certId,
                "certType": "Ind01",
                "certExpiredDate": "2039/06/29",
                "certIssuedPlace": "深圳",
                "name": name,
                "education": "02",
                "marriage": "20",
                "familyStatus": "1",
                "familyAddProvince": addr1[0],
                "familyAddCity": addr1[1],
                "familyAddDistrict": addr1[2],
                "familyAddress": addr1[3] + "波托菲诺纯水岸七期三单元205室",
                "permanentLocation": "01",
                "mobilePhone": phone,
                "localHouseFlag": "1",
                "monthIncome": "80000",
                "sex": "1",
                "birthday": birthday
            },
            "workInfo": {
                "workBelongIndustry": "A02",
                "workOrgName": Base.autoGenerateName() + "哦琼文对接",
                "workDepartment": "开发",
                "workNature": "20",
                "workHeadship": "安保人员",
                "workPosition": "10",
                "workBeginDate": "2018/05",
                "workIndustryDate": "2005/10",
                "workEmployeeType": "020",
                "workPhone": "0",
                "workAddProvince": addr2[0],
                "workAddCity": addr2[1],
                "workAddDistrict": addr2[2],
                "workAddress": addr2[3]
            },
            "contactsInfo": [
                {
                    "type": "1",
                    "name": Base.autoGenerateName(),
                    "relationship": "0302",
                    "phone": "0",
                    "phoneArea": "",
                    "phoneExtensionNum": ""
                },
                {
                    "type": "2",
                    "name": Base.autoGenerateName(),
                    "relationship": "0101",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0202",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                },
                {
                    "type": "3",
                    "name": Base.autoGenerateName(),
                    "relationship": "0201",
                    "phone": Base.autoGeneratePhoneNo(),
                    "remark": ""
                }
            ],
            "borrowingMatters": {
                "businessType": "1101900",
                "businessSum": loanAmounts,
                "loanTerm": loanTerm,
                "purpose": "01",
                "mainReturnType": "1",
                "returnPeriod": "1",
                "repayCardId": bkCardNo,
                "repayBank": bkCode,
                "loanCardId": bkCardNo,
                "loanBank": bkCode
            },
            "notCustomerMatters": {
                "customerType": customerType,
                "loanType": loanType,
                "saleChannel": "002",
                "isCertifition": "0",
                "interviewerId": interviewerId,
                "interviewCenter": interviewCenter,
                "operateUserId": operatorUserId,
                "operateAssistantUser": "ZENGTAB",
                "operateOrgId": operatorOrgId,
                "inputUserName": inputUserId,
                "inputDate": time.strftime('%Y/%m/%d',
                                           time.localtime()),
                "departmentId": departmentId,
                "isRecommendedByOld": "0"
            },
            "imageInfo": [{"attachmentNo": attach["attachmentNo"], "attachmentType": attach["attachmentType"],
                           "attachmentRealFileName": "%s.jpg" % attach["attachmentType"], "operator": inputUserId,
                           "inputDate": time.strftime('%Y/%m/%d', time.localtime()), "inputTime": "10:27:44"} for attach
                          in IMAGE["ZLJR"]],
            "approvalComments": {
                "opinionType": "010"
            },
            "recordingAging": {
                "startInputDate": time.strftime('%Y/%m/%d',
                                                time.localtime()),
                "startInputTime": "09:58:42",
                "endInputDate": time.strftime('%Y/%m/%d',
                                              time.localtime()),
                "endInputTime": "10:27:44"
            }
        }
        if recommenderTel:
            data["notCustomerMatters"].setdefault("recommenderTel", recommenderTel)
        if recommender:
            data["notCustomerMatters"].setdefault("recommender", recommender)
        headers = {"content-type": "application/json",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

        req = request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        return json.loads(request.urlopen(req, None, 60).read().decode("utf-8"))['data'].get("applyId"), uid

    def submitOrder(self, name, phone, certId, bkCardNo, bkCode="000001", loanAmounts="303000", loanType="120", loanTerm="36",
                                 customerType="002", operatorOrgId="75501", interviewCenter="755001", departmentId="1075501004", interviewerId="ZHAOSMB", inputUserId="ZHAOSMB",
                                 operatorUserId="7550122", recommenderTel=None,recommender=None):
        applyNo,uid = "",""
        NA = request.urlopen(request.Request("http://10.126.0.249:8080/getApplyNo",data=bytes(parse.urlencode({"url": self.url}),encoding="utf-8"))).read().decode("utf-8")
        if self.businessType == "1100100":
            applyNo, uid = self.orderSubmitYJKD(phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                                               loanType, loanTerm, customerType, operatorOrgId,
                                                             interviewCenter, departmentId, interviewerId, inputUserId,
                                                             operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1100200":
            applyNo, uid = self.orderSubmitYJD(phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType,
                                                     loanTerm,
                                                     customerType, operatorOrgId, interviewCenter, departmentId,
                                                     interviewerId, inputUserId,
                                                     operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1100300":
            applyNo, uid = self.orderSubmitLHXD(phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType,
                                                      loanTerm,
                                                      customerType, operatorOrgId, interviewCenter, departmentId,
                                                      interviewerId, inputUserId,
                                                      operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1100400":
            applyNo, uid = self.orderSubmitZRB(phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType,
                                                     loanTerm,
                                                     customerType, operatorOrgId, interviewCenter, departmentId,
                                                     interviewerId, inputUserId,
                                                     operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1100500":
            applyNo, uid = self.orderSubmitSZS(phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType,
                                                     loanTerm, customerType, operatorOrgId,
                                                     interviewCenter, departmentId, interviewerId, inputUserId,
                                                     operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1100600":
            applyNo, uid = self.orderSubmitHKbank(phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                                             loanType, loanTerm,
                                                           customerType, operatorOrgId, interviewCenter, departmentId,
                                                           interviewerId, inputUserId,
                                                           operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1100700":
            applyNo, uid = self.orderSubmitNBbank(phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                                             loanType, loanTerm, customerType,
                                                           operatorOrgId, interviewCenter, departmentId, interviewerId,
                                                           inputUserId,
                                                           operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1100800":
            applyNo, uid = self.orderSubmitZGC(phone, name, certId, bkCardNo, bkCode,
                                                        loanAmounts, loanType, loanTerm, customerType,
                                                        operatorOrgId,
                                                        interviewCenter, departmentId, interviewerId, inputUserId,
                                                        operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1100900":
            applyNo, uid = self.orderSubmitXGM(phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                                       loanType, loanTerm, customerType, operatorOrgId,
                                                     interviewCenter, departmentId, interviewerId, inputUserId,
                                                     operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1101300":
            applyNo, uid = self.orderSubmitHXbank(phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                                          loanType, loanTerm, customerType, operatorOrgId,
                                                        interviewCenter, departmentId, interviewerId,
                                                        inputUserId, operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1101200":
            applyNo, uid = self.orderSubmitCDbank(phone, name, certId, bkCardNo, bkCode,
                                                        loanAmounts,
                                                          loanType, loanTerm, customerType, operatorOrgId,
                                                        interviewCenter, departmentId, interviewerId,
                                                        inputUserId, operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1101400":
            applyNo, uid = self.orderSubmitNJbank(phone, name, certId, bkCardNo, bkCode,
                                                        loanAmounts,
                                                          loanType, loanTerm, customerType, operatorOrgId,
                                                        interviewCenter, departmentId, interviewerId,
                                                        inputUserId, operatorUserId, recommenderTel, recommender, NA)

        elif self.businessType == "1101600":
            applyNo, uid = self.orderSubmitLFbank(phone, name, certId, bkCardNo, bkCode,
                                                        loanAmounts,
                                                          loanType, loanTerm, customerType, operatorOrgId,
                                                        interviewCenter, departmentId, interviewerId,
                                                        inputUserId, operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1101500":
            applyNo, uid = self.orderSubmitMTbank(phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                                          loanType, loanTerm,
                                                        customerType, operatorOrgId, interviewCenter, departmentId,
                                                        interviewerId, inputUserId,
                                                        operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1101700":
            applyNo, uid = self.orderSubmitXWbank(phone, name, certId, bkCardNo, bkCode,
                                                        loanAmounts,
                                                          loanType, loanTerm, customerType,
                                                        operatorOrgId, interviewCenter, departmentId, interviewerId,
                                                        inputUserId, operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1101800":
            applyNo, uid = self.orderSubmitCCNS(phone, name, certId, bkCardNo, bkCode, loanAmounts,
                                                        loanType, loanTerm, customerType, operatorOrgId,
                                                      interviewCenter, departmentId, interviewerId,
                                                      inputUserId, operatorUserId, recommenderTel, recommender, NA)
        elif self.businessType == "1101900":
            applyNo, uid = self.orderSubmitZLJR(phone, name, certId, bkCardNo, bkCode, loanAmounts, loanType,
                                                      loanTerm, customerType,
                                                      operatorOrgId, interviewCenter, departmentId, interviewerId,
                                                      inputUserId, operatorUserId, recommenderTel, recommender, NA)

        return applyNo,uid

    def modifyIsNeedEnsure(self,applyNo):
        wkDB = self.get_WKDB_info()
        request.urlopen(request.Request("http://10.126.0.249:8080/modifyIsNeedEnsure", data=bytes(parse.urlencode({"wkDB": wkDB, "applyNo":applyNo}), encoding="utf-8")))


    def get_WKDB_info(self):
        return self.config.getCfgValue(self.curEnv, "WK", "DB")

    def queryOrderState(self,applyNo):
        wkDB = self.get_WKDB_info()
        return request.urlopen(request.Request("http://10.126.0.249:8080/queryOrderState",
                                               data=bytes(parse.urlencode({"applyNo": applyNo, "wkDB": wkDB}),
                                                          encoding="utf-8"))).read().decode("utf-8")


    def adjustTask(self,applyNo,state_operator="LUZHONG"):
        """任务调整 """
        chrm_opt = webdriver.ChromeOptions()
        chrm_opt.add_argument("--headless")
        browser = webdriver.Chrome(options=chrm_opt)
        browser.implicitly_wait(30)
        browser.get(self.url)
        browser.maximize_window()
        userName = browser.find_element_by_id("username")
        userName.clear()
        userName.send_keys("luzhong")

        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys("a1234567")

        submit_btn = browser.find_element_by_tag_name("button")
        submit_btn.click()

        icon1 = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/ul/li[7]')
        icon1.click()

        applyNoInput = browser.find_element_by_xpath('//*[@id="applyId"]')
        applyNoInput.send_keys(applyNo)

        queryBtn = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div/form/div[2]/div[1]/div/div/div/span/button')
        queryBtn.click()

        time.sleep(5)
        checkBox1 = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/table/thead/tr/th[1]/span/div/label/span/input')
        checkBox1.click()

        performBtn = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[1]/button[3]')
        performBtn.click()

        userIdInput = browser.find_element_by_xpath('//*[@id="userId"]')
        userIdInput.send_keys(state_operator)

        queryBtn2 = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div/form/div[2]/div[1]/div/div/div/span/button')
        queryBtn2.click()

        checkBox2 = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div/table/thead/tr/th[1]/span/div/label/span/input')
        checkBox2.click()

        confirmBtn = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[3]/button[2]')
        confirmBtn.click()
        time.sleep(5)
        browser.quit()


    def ZXDC(self,applyNo):
        """征信调查"""
        self.adjustTask(applyNo)
        chrm_opt = webdriver.ChromeOptions()
        chrm_opt.add_argument("--headless")
        browser = webdriver.Chrome(options=chrm_opt)
        browser.implicitly_wait(30)
        browser.get(self.url)
        browser.maximize_window()
        userName = browser.find_element_by_id("username")
        userName.clear()
        userName.send_keys("luzhong")

        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys("a1234567")

        submit_btn = browser.find_element_by_tag_name("button")
        submit_btn.click()

        icon1 = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/ul/li[4]')
        icon1.click()

        time.sleep(3)
        nextPage = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/ul/li[@title="下一页"]')
        while applyNo not in browser.page_source:
            nextPage.click()
            time.sleep(3)

        handleBtn = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[contains(string(),"%s")]/td[11]/span/a' % applyNo)
        handleBtn.click()

        yewuheding = browser.find_element_by_xpath('//*[@id="right"]/div/div/div/div[1]/div[1]/div/div/div/div/div[10]')
        yewuheding.click()

        agreeRadio = browser.find_element_by_xpath('//*[@id="opinionType"]/label[1]')
        agreeRadio.click()

        saveOpinionBtn = browser.find_element_by_xpath(
            '//*[@id="right"]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/button')
        saveOpinionBtn.click()

        js = 'var q=document.querySelector("#right > div > div > div > div.show.business_wrap");q.scrollTop=10000'
        browser.execute_script(js)

        input1Js = 'var i = document.querySelector("#incomeBase");i.value="50000.00"'
        browser.execute_script(input1Js)

        time.sleep(2)
        input2 = browser.find_element_by_xpath('//*[@id="unSecuredBalance"]')
        input2.clear()
        input2.send_keys("0.00")

        input3 = browser.find_element_by_xpath('//*[@id="unSecuredMonthpay"]')
        input3.clear()
        input3.send_keys("0.00")

        input4 = browser.find_element_by_xpath('//*[@id="creditSum"]')
        input4.clear()
        input4.send_keys("0.00")

        input5 = browser.find_element_by_xpath('//*[@id="creditOverdraft"]')
        input5.clear()
        input5.send_keys("0.00")

        saveBtn = browser.find_element_by_xpath('//*[@id="right"]/div/div/div/div[2]/div[3]/div[2]/div/button')
        saveBtn.click()

        submitTaskBtn = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/button')
        submitTaskBtn.click()

        time.sleep(5)
        confirmBtn = browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button')
        confirmBtn.click()

        browser.quit()

    def ZLSH(self,applyNo):
        """资料审核"""
        self.adjustTask(applyNo)
        pass

    def DKSP(self,applyNo):
        """贷款审批"""
        self.adjustTask(applyNo)
        chrm_opt = webdriver.ChromeOptions()
        chrm_opt.add_argument("--headless")
        browser = webdriver.Chrome(options=chrm_opt)
        browser.implicitly_wait(30)
        browser.get(self.url)
        browser.maximize_window()
        userName = browser.find_element_by_id("username")
        userName.clear()
        userName.send_keys("luzhong")

        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys("a1234567")

        submit_btn = browser.find_element_by_tag_name("button")
        submit_btn.click()

        icon1 = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/ul/li[5]')
        icon1.click()

        time.sleep(3)
        nextPage = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/ul/li[@title="下一页"]')
        while applyNo not in browser.page_source:
            nextPage.click()
            time.sleep(3)

        handleBtn = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[contains(string(),"%s")]/td[11]/span/a' % applyNo)
        handleBtn.click()

        yewuheding = browser.find_element_by_xpath('//*[@id="right"]/div/div/div/div[1]/div[1]/div/div/div/div/div[10]')
        yewuheding.click()

        agreeRadio = browser.find_element_by_xpath('//*[@id="opinionType"]/label[1]')
        agreeRadio.click()

        saveOpinionBtn = browser.find_element_by_xpath(
            '//*[@id="right"]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/button')
        saveOpinionBtn.click()

        js = 'var q=document.querySelector("#right > div > div > div > div.show.business_wrap");q.scrollTop=10000'
        browser.execute_script(js)

        input1Js = 'var i = document.querySelector("#incomeBase");i.value="50000.00"'
        browser.execute_script(input1Js)

        time.sleep(2)
        input2 = browser.find_element_by_xpath('//*[@id="unSecuredBalance"]')
        input2.clear()
        input2.send_keys("0.00")

        input3 = browser.find_element_by_xpath('//*[@id="unSecuredMonthpay"]')
        input3.clear()
        input3.send_keys("0.00")

        input4 = browser.find_element_by_xpath('//*[@id="creditSum"]')
        input4.clear()
        input4.send_keys("0.00")

        input5 = browser.find_element_by_xpath('//*[@id="creditOverdraft"]')
        input5.clear()
        input5.send_keys("0.00")

        saveBtn = browser.find_element_by_xpath('//*[@id="right"]/div/div/div/div[2]/div[3]/div[2]/div/button')
        saveBtn.click()

        time.sleep(5)
        submitTaskBtn = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[1]/button')
        submitTaskBtn.click()

        time.sleep(5)
        confirmBtn = browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button')
        confirmBtn.click()

        confirmBtn2 = browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button[2]')
        confirmBtn2.click()

        browser.quit()

    @classmethod
    def pushToBidPool(cls,applyNo,isNeedEnsure=True):
        wkTest = WKTest()
        """推到发标池"""
        errortimes = 30
        while True:
            state, subState, stateCount = wkTest.queryOrderState(applyNo).split("|")
            if state == "1000":
                break
            elif state=="0050":
                if subState=="0001":
                    wkTest.ZXDC(applyNo)
                elif subState=="0019":
                    wkTest.ZLSH(applyNo)
                if not isNeedEnsure:
                    wkTest.modifyIsNeedEnsure(applyNo)
            elif state=="0060":
                wkTest.DKSP(applyNo)
            elif state=="0070":
                WPTTest().telSigning(applyNo)
            elif state in ("0010","0012"):
                if errortimes==0:
                    raise Exception("%s状态异常，请前往悟空系统检查！"%applyNo)
                time.sleep(1)
                errortimes-=1
            else:
                raise Exception("%s状态为%s，未处理异常！"%(applyNo,state))

    def test_WK_00001_案例名称(self):
        # 测试步骤
        # 结果判断
        a,b,x = "","",""
        self.assertEqual(a, b)      # a == b
        self.assertNotEqual(a, b)   # a != b
        self.assertTrue(x)          # bool(x) is True
        self.assertFalse(x)         # bool(x) is False
        self.assertIs(a, b)         # a is b
        self.assertIsNot(a, b)      # a is not b
        self.assertIn(a, b)         # a in b
        self.assertNotIn(a, b)


if __name__ == '__main__':
    unittest.main()