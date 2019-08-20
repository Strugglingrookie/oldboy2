#coding=utf-8
import uuid
import json
import unittest
import os
from random import randint,random
from urllib import request,parse
from config import Config
from queryCredit import queryCredit


class PHTest(unittest.TestCase):
    configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yml")
    config = Config(configPath)
    curEnv = config.getCfgValue("curEnv")
    url = config.getCfgValue(curEnv, "PH", "url")
    wechatUrl = url.replace("testweb", "testwechat")
    sesig = None
    businessType = None

    @classmethod
    def setUpClass(cls):  # 在所有用例执行之前运行的
        pass

    @classmethod
    def tearDownClass(cls):  # 在所有用例都执行完之后运行的
        pass

    def setUp(self):  # 每个用例运行之前运行的
        self.sesig = "{0:6x}-{1:4x}-{2:4x}-{3:4x}-{4:12x}".format(randint(16 ** 7, 16 ** 8), randint(16 ** 3, 16 ** 4),
                                                                  randint(16 ** 3, 16 ** 4), randint(16 ** 3, 16 ** 4),
                                                                  randint(16 ** 11, 16 ** 12))

    def tearDown(self):  # 每个用例运行之后运行的
        pass

    def get_YYfax_MsgDb_Info(self):
        return self.config.getCfgValue(self.curEnv,"YYFAX","msgDB")

    def get_YYfax_JiesuanDB_Info(self):
        return self.config.getCfgValue(self.curEnv, "YYFAX", "jiesuanDB")

    def get_PHDB_info(self):
        return self.config.getCfgValue(self.curEnv,"PH","DB")

    def get_innerDB_info(self):
        return self.config.getCfgValue(self.curEnv,"INNER","DB")

    def get_inne_urls(self):
        inner_url = self.config.getCfgValue(self.curEnv,"INNER","url")
        inne_urls = {
            'upload_report': '%s/InnerEval/api/pbcc/report/fileUpload'%inner_url,
            'query_credit': '%s/InnerEval/api/pbcc/report/apply'%inner_url,
            'query_result': '%s/InnerEval/api/credit/result/list'%inner_url
        }
        return inne_urls

    def get_wpt_mongo_conn(self):
        return list(self.config.getCfgValue(self.curEnv, "WPT", "DB").values())

    def recognPicCode(self):
        return request.urlopen(request.Request("http://10.126.0.249:8080/recognizeCaptcha",data=bytes(parse.urlencode({"svg": request.urlopen(request.Request("%s/server?model=captcha&action=getCaptcha&%0.16f" % (self.wechatUrl, random()), headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig})).read().decode("utf-8"), "id": uuid.uuid4()}),encoding="utf-8"))).read().decode("utf-8")

    def sendRegisterSMSCode(self,phone,captcha):
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "verify", "action": "getSmsCode", "mobile": phone, "type": "1", "operation": "reg","captcha": captcha}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))

    def queryRegisterSms(self,phone):
        msgDB = self.get_YYfax_MsgDb_Info()
        return request.urlopen(request.Request("http://10.126.0.249:8080/queryRegisterSms",data=bytes(parse.urlencode({"phone": phone,"msgDB":msgDB}), encoding="utf-8"))).read().decode("utf-8")

    def queryYYfaxUid(self,phone):
        jiesuanDB = self.get_YYfax_JiesuanDB_Info()
        return request.urlopen(request.Request("http://10.126.0.249:8080/queryYYfaxUid",data=bytes(parse.urlencode({"phone": phone, "jiesuanDB": jiesuanDB}),encoding="utf-8"))).read().decode("utf-8")


    def register(self,phone,smsCode):
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "register", "params": {"name": phone,"pass":"qTvNxfyCs0kQoRuQCJYO6T01iadzO+qJFILx/CllmHg6EByIGLKTimjwUEiHcFzRSTHn7xi/JdfiAoyjVG+5kYeGSh4VvDTQK80B8TiC/rtk+XX4Xj2/E4Ja/LMg2EgcxdW8lgym6P6+sPgEifWURar8vWzwFXqjN6gM7+Ntd3g=","smsCode": smsCode}}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))

    def userAuth(self, name, certId, bank, bkCardNo):
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps(request.urlopen(request.Request("http://10.126.0.249:8080/phAuthPacket",data=bytes(parse.urlencode({"name":name,"certId":certId,"bank":bank,"bkCardNo":bkCardNo}),encoding="utf-8"))).read().decode("utf-8")).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))

    def fuiouXYZFSign(self,phone):
        preBindRequestSerialNo = json.loads(request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "prebind","params": {"phone": phone, "channel": "Fuiou", "preBindRequestSerialNo": ""}}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig})).read().decode("utf-8")).get("content").get("preBindRequestSerialNo")
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "confirmbind","params": {"phone": phone, "preBindRequestSerialNo": preBindRequestSerialNo,"uniqueCode": "", "channel": "Fuiou", "verifyCode": "000000"}}).encode("utf-8"), headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))

    def allInPayXYZFSign(self,phone):
        preBindRequestSerialNo = json.loads(request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "prebind","params": {"phone": phone, "channel": "AllInPay", "preBindRequestSerialNo": ""}}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig})).read().decode("utf-8")).get("content").get("preBindRequestSerialNo")
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "confirmbind", "params": {"phone": phone, "preBindRequestSerialNo": preBindRequestSerialNo, "uniqueCode": "","channel": "AllInPay", "verifyCode": "111111"}}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))

    def baoFooXYZFSign(self,phone):
        data = json.loads(request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "prebind","params": {"phone": phone, "channel": "BaoFoo", "preBindRequestSerialNo": ""}}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig})).read().decode("utf-8"))
        preBindRequestSerialNo = data.get("content").get("preBindRequestSerialNo")
        uniqueCode = data.get("content").get("uniqueCode")
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "confirmbind", "params": {"phone": phone, "preBindRequestSerialNo": preBindRequestSerialNo, "uniqueCode": uniqueCode, "channel": "BaoFoo", "verifyCode": "111111"}}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))

    def signContracts(self):
        if self.businessType == "1100500":
            cid = [6, 7, 8, 9, 11]
        elif self.businessType == "1101500":
            cid = [21, 22, 23, 24, 25]
        elif self.businessType == "1101400":
            cid = [30]
        else:
            cid = None
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "contract", "action": "check", "cid": 10005}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}), timeout=60)
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "contract", "action": "check", "cid": [1, 2, 3, 10002]}).encode("utf-8"), headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}), timeout=60)
        if cid is not None:
            request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "contract", "action": "check", "cid": cid}).encode("utf-8"), headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}), timeout=60)


    def SZSsmsSignContract(self,phone):
        sn = json.loads(request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "prebind", "params": {"phone": phone, "channel": "SZS"}}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig})).read().decode("utf-8")).get("content").get("preBindRequestSerialNo")
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "user", "action": "confirmbind","params": {"phone": phone, "preBindRequestSerialNo": sn, "verifyCode": "111111","channel": "SZS"}}).encode("utf-8"), headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))


    def ZLJRopenAccount(self,phone,uid):
        phDB = self.get_PHDB_info()
        request.urlopen(request.Request("http://10.126.0.249:8080/zljrOpenAccount01",data=bytes(parse.urlencode({"phDB": phDB, "uid":uid}),encoding="utf-8")))
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "zljrLoan", "action": "verifyBank"}).encode("utf-8"), headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))
        smscode = request.urlopen(request.Request("http://10.126.0.249:8080/getZLJRsmscode", data=bytes(parse.urlencode({"phone": phone}),encoding="utf-8"))).read().decode("utf-8")
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "zljrLoan", "action": "bindBank", "dynamicCode": smscode}).encode("utf-8"), headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))
        request.urlopen(request.Request("%s/server" % self.wechatUrl, data=json.dumps({"model": "zljrLoan", "action": "zljrSign"}).encode("utf-8"),headers={"Cookie": "_dOX8hsSDjdZ=%s" % self.sesig}))
        request.urlopen(request.Request("http://10.126.0.249:8080/zljrOpenAccount02",data=bytes(parse.urlencode({"phDB": phDB, "uid": uid}), encoding="utf-8")))

    def XWBankopenAccount(self,phone,uid):
        phDB = self.get_PHDB_info()
        request.urlopen(request.Request("http://10.126.0.249:8080/XWBankopenAccount",data=bytes(parse.urlencode({"phDB": phDB, "uid": uid, "phone":phone}), encoding="utf-8")))

    def thirdPartyOpenAccount(self,phone):
        if self.businessType == "1100500":
            self.SZSsmsSignContract(phone)
        elif self.businessType == "1101900":
            uid = self.queryYYfaxUid(phone)
            self.ZLJRopenAccount(phone,uid)
        elif self.businessType == "1101700":
            uid = self.queryYYfaxUid(phone)
            self.XWBankopenAccount(phone,uid)

    def queryCredit(self,name,certId,isMD):
        innerDB = self.get_innerDB_info()
        request.urlopen(request.Request("http://10.126.0.249:8080/innerCreditReport", data=bytes(parse.urlencode({"innerDB": innerDB, "name": name, "certId": certId, "isMD": isMD}),encoding="utf-8"))).read().decode("utf-8")
        inne_urls = self.get_inne_urls()
        mongo_conn = self.get_wpt_mongo_conn()
        queryCredit.run(inne_urls,mongo_conn,name,certId,"地激发多少")


    def test_PH_00001_案例名称(self):
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
