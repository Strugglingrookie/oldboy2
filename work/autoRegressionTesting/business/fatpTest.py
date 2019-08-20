#coding=utf-8
import json
import time
import os
import unittest
from urllib import request,parse
from config import Config
from business.omsTest import OmsTest
from selenium import webdriver

class FatpTest(unittest.TestCase):
    configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yml")
    config = Config(configPath)
    curEnv = config.getCfgValue("curEnv")
    url = config.getCfgValue(curEnv, "FATP", "url")
    bsHost = config.getCfgValue(curEnv, "BS", "host")


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

    def get_fatpDB_info(self):
        return self.config.getCfgValue(self.curEnv, "FATP", "DB")

    def get_coreDB_info(self):
        return self.config.getCfgValue(self.curEnv, "CORE", "DB")

    def get_bsDB_info(self):
        return self.config.getCfgValue(self.curEnv, "BS", "DB")

    def get_xgmDB_info(self):
        return self.config.getCfgValue(self.curEnv, "YYFAX", "xgmDB")

    def get_ZljrFtp_info(self):
        return self.config.getCfgValue(self.curEnv, "ZLJR", "ftpServer")

    def query_core_businessDate(self):
        coreDB = self.get_coreDB_info()
        return request.urlopen(request.Request("http://10.126.0.249:8080/corebusinessDate",
                                               data=bytes(parse.urlencode({"coreDB": coreDB}),
                                                          encoding="utf-8"))).read().decode("utf-8")

    def getLA_Detail(self, applyNo):
        return request.urlopen(request.Request("http://10.126.0.249:8080/getLADetail",
                                               data=parse.urlencode(
                                                   {"applyNo": applyNo, "env": self.curEnv}))).read().decode("utf-8")

    def handPublish_ZLJR(self, la):
        chrm_opt = webdriver.ChromeOptions()
        chrm_opt.add_argument("--headless")
        browser = webdriver.Chrome(options=chrm_opt)
        browser.implicitly_wait(30)
        browser.get(self.url)
        browser.maximize_window()
        userName = browser.find_element_by_id("userId")
        userName.clear()
        userName.send_keys("yancfa")

        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys("a1234567")

        submit_btn = browser.find_element_by_tag_name("button")
        submit_btn.click()

        icon1 = browser.find_element_by_xpath("//div[@class=\"ant-layout-sider-children\"]/ul/li[1]")
        icon1.click()

        link1 = browser.find_element_by_partial_link_text("发标管理")
        link1.click()

        js = "var q=document.documentElement.scrollTop=10000"
        browser.execute_script(js)

        enterLabel = browser.find_element_by_xpath(
            "//div[contains(@class,\"ant-card-padding-transition\")][4]/div[@class=\"ant-card-body\"]/div/div[1]/a")
        enterLabel.click()

        input1 = browser.find_element_by_xpath(
            "//div[contains(@class,\"ant-form-item-label\")][contains(string(),\"借据编号\")]/following-sibling::div[1]/descendant::input[1]")
        input1.send_keys(la)

        searchBtn = browser.find_element_by_xpath("//button[@type=\"submit\"][contains(string(),\"查 询\")]")
        searchBtn.click()

        time.sleep(2)
        checkBox1 = browser.find_element_by_xpath("//table/thead/tr/th[1]/descendant::input[1]")
        checkBox1.click()

        performBtn = browser.find_element_by_xpath("//button[contains(string(),\"手动发标\")]")
        performBtn.click()

        time.sleep(2)
        confirmBtn = browser.find_element_by_xpath("//div[@class=\"ant-popover-buttons\"]/button[2]")
        confirmBtn.click()

        time.sleep(5)
        confirmBtn2 = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[3]/button[2]")
        confirmBtn2.click()
        time.sleep(30)
        browser.quit()

    def handPublish_SZS(self, la):
        chrm_opt = webdriver.ChromeOptions()
        chrm_opt.add_argument("--headless")
        browser = webdriver.Chrome(options=chrm_opt)
        browser.implicitly_wait(30)
        browser.get(self.url)
        browser.maximize_window()
        userName = browser.find_element_by_id("userId")
        userName.clear()
        userName.send_keys("yancfa")

        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys("a1234567")

        submit_btn = browser.find_element_by_tag_name("button")
        submit_btn.click()

        icon1 = browser.find_element_by_xpath("//div[@class=\"ant-layout-sider-children\"]/ul/li[1]")
        icon1.click()

        link1 = browser.find_element_by_partial_link_text("发标管理")
        link1.click()

        enterLabel = browser.find_element_by_xpath(
            "//div[contains(@class,\"ant-card-padding-transition\")][3]/div[@class=\"ant-card-body\"]/div/div[3]/a")
        enterLabel.click()

        input1 = browser.find_element_by_xpath(
            "//div[contains(@class,\"ant-form-item-label\")][contains(string(),\"借据编号\")]/following-sibling::div[1]/descendant::input[1]")
        input1.send_keys(la)

        time.sleep(10)
        searchBtn = browser.find_element_by_xpath("//button[@type=\"submit\"][contains(string(),\"查 询\")]")
        searchBtn.click()

        time.sleep(2)
        checkBox1 = browser.find_element_by_xpath("//table/thead/tr/th[1]/descendant::input[1]")
        checkBox1.click()

        performBtn = browser.find_element_by_xpath("//button[contains(string(),\"手动发标\")]")
        performBtn.click()

        time.sleep(2)
        confirmBtn = browser.find_element_by_xpath("//div[@class=\"ant-popover-buttons\"]/button[2]")
        confirmBtn.click()

        time.sleep(5)
        confirmBtn2 = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[3]/button[2]")
        confirmBtn2.click()
        time.sleep(30)
        browser.quit()

    def handPublish_XGM(self, la):
        chrm_opt = webdriver.ChromeOptions()
        chrm_opt.add_argument("--headless")
        browser = webdriver.Chrome(options=chrm_opt)
        browser.implicitly_wait(30)
        mainUrl = "https://testfatpsit08.yylending.com"
        browser.get(mainUrl)
        browser.maximize_window()
        userName = browser.find_element_by_id("userId")
        userName.clear()
        userName.send_keys("yancfa")

        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys("a1234567")

        submit_btn = browser.find_element_by_tag_name("button")
        submit_btn.click()

        icon1 = browser.find_element_by_xpath("//div[@class=\"ant-layout-sider-children\"]/ul/li[1]")
        icon1.click()

        link1 = browser.find_element_by_partial_link_text("发标管理")
        link1.click()

        enterLabel = browser.find_element_by_xpath(
            "//div[contains(@class,\"ant-card-padding-transition\")][1]/div[@class=\"ant-card-body\"]/div/div[2]/a")
        enterLabel.click()

        input1 = browser.find_element_by_xpath(
            "//div[contains(@class,\"ant-form-item-label\")][contains(string(),\"借据编号\")]/following-sibling::div[1]/descendant::input[1]")
        input1.send_keys(la)

        time.sleep(10)
        searchBtn = browser.find_element_by_xpath("//button[@type=\"submit\"][contains(string(),\"查 询\")]")
        searchBtn.click()

        time.sleep(2)
        checkBox1 = browser.find_element_by_xpath("//table/thead/tr/th[1]/descendant::input[1]")
        checkBox1.click()

        performBtn = browser.find_element_by_xpath("//button[contains(string(),\"手动发标\")]")
        performBtn.click()

        time.sleep(2)
        confirmBtn = browser.find_element_by_xpath("//div[@class=\"ant-popover-buttons\"]/button[2]")
        confirmBtn.click()

        time.sleep(10)
        confirmBtn2 = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[1]/div[3]/button[2]")
        confirmBtn2.click()
        time.sleep(10)
        browser.quit()

    def updateStatus_NBTS(self, la):
        fatpDB = self.get_fatpDB_info()
        request.urlopen(request.Request("http://10.126.0.249:8080/updateStatusNBTS",
                                        data=bytes(parse.urlencode({"fatpDB": fatpDB, "la": la}), encoding="utf-8")))

    def updateStatus_YJF(self, la):
        fatpDB = self.get_fatpDB_info()
        request.urlopen(request.Request("http://10.126.0.249:8080/updateStatusYJF",
                                        data=bytes(parse.urlencode({"fatpDB": fatpDB, "la": la}), encoding="utf-8")))

    def callback_YJF(self, la, amount, certId, name, term, coreBusinessDate):
        request.urlopen(request.Request("%s/fatp-lm-service/http/lm/foreign/callback/loanout/do" % self.url,
                                        data=json.dumps({"dataTempVo": {"beginDate": "2019-01-31",
                                                                        "businessSum": "%s" % amount, "certId": certId,
                                                                        "loanNo": la, "name": name,
                                                                        "putoutDate": coreBusinessDate, "sterm": term},
                                                         "loanNo": la}).encode("utf-8"),
                                        headers={"Content-Type": "application/json"}))

    def callback_CD(self, la, amount, term, name, phone, certId, coreBusinessDate):
        request.urlopen(request.Request("http://10.126.0.249:8080/callbackCDBank", data=bytes(parse.urlencode(
            {"amount": amount, "la": la, "term": term, "name": name, "phone": phone, "certId": certId,
             "coreBusinessDate": coreBusinessDate, "bs": self.bsHost}), encoding="utf-8")))

    def callback_NJ(self, la, amount, term, coreBusinessDate):
        request.urlopen(request.Request("http://10.126.0.249:8080/callbackNJBank", data=bytes(parse.urlencode(
            {"amount": amount, "la": la, "term": term, "coreBusinessDate": coreBusinessDate, "bs": self.bsHost}),
            encoding="utf-8")))

    def callback_ZLJR(self, la, amount, certId, name, term, coreBusinessDate):
        request.urlopen(request.Request("%s/fatp-lm-service/http/lm/foreign/callback/loanout/do" % self.url,
                                        data=json.dumps({"dataTempVo": {"beginDate": "2019-01-31",
                                                                        "businessSum": "%s" % amount, "certId": certId,
                                                                        "loanNo": la, "name": name,
                                                                        "putoutDate": coreBusinessDate, "sterm": term},
                                                         "loanNo": la}).encode("utf-8"),
                                        headers={"Content-Type": "application/json"}))

    def queryJnlNo(self, certId, apiname):
        bsDB = self.get_bsDB_info()
        return request.urlopen(request.Request("http://10.126.0.249:8080/queryJnlNo", data=bytes(
            parse.urlencode({"bsDB": bsDB, "certId": certId, "apiname": apiname}), encoding="utf-8"))).read().decode(
            "utf-8")

    def update_YYFAX_xgmDB(self, la, coreBusinessDate):
        xmgDB = self.get_xgmDB_info()
        request.urlopen(request.Request("http://10.126.0.249:8080/updateXGMDB", data=bytes(
            parse.urlencode({"xmgDB": xmgDB, "la": la, "coreBusinessDate": coreBusinessDate}), encoding="utf-8")))

    def bidYJKD(self, la, amount, term, name, certId):
        coreBusinessDate = self.query_core_businessDate()
        self.updateStatus_YJF(la)
        self.callback_YJF(la, amount, name, certId, term, coreBusinessDate)

    def bidYJMD(self, la, amount, term, name, certId):
        coreBusinessDate = self.query_core_businessDate()
        self.updateStatus_YJF(la)
        self.callback_YJF(la, amount, name, certId, term, coreBusinessDate)

    def bidCDBank(self, la, amount, term, name, phone, certId):
        coreBusinessDate = self.query_core_businessDate()
        self.callback_CD(la, amount, term, name, phone, certId, coreBusinessDate)

    def bidNJBank(self, la, amount, term):
        coreBusinessDate = self.query_core_businessDate()
        self.callback_NJ(la, amount, term, coreBusinessDate)

    def bidZLJR(self, la, amount, term, name, certId):
        OmsTest().performJob("ZLJRSignStatusJob")
        self.handPublish_ZLJR(la)
        coreBusinessDate = self.query_core_businessDate()
        self.callback_ZLJR(la, amount, certId, name, term, coreBusinessDate)

    def bidSZS(self, la, certId):
        self.handPublish_SZS(la)
        request.urlopen(request.Request("http://10.126.0.249:8080/creditAuditNotifySZS", data=bytes(
            parse.urlencode({"jnlNo": self.queryJnlNo(certId, "per.MCCreditAudit"), "bs": self.bsHost}),
            encoding="utf-8")))
        request.urlopen(request.Request("http://10.126.0.249:8080/grantCreditFullBackSZS", data=bytes(
            parse.urlencode({"jnlNo": self.queryJnlNo(certId, "transfer.MCGrantCreditFull"), "bs": self.bsHost}),
            encoding="utf-8")))

    def bidXGM(self, la):
        self.handPublish_XGM(la)
        OmsTest().performJob("SendXGMReadyJob")
        coreBusinessDate = self.query_core_businessDate()
        self.update_YYFAX_xgmDB(la, coreBusinessDate)
        OmsTest().performJob("ToXGMLoanJob")


    def test_FATP_00001_案例名称(self):
        #测试步骤
        #结果判断
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