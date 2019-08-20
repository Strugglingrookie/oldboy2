#coding=utf-8
import os
import unittest
from config import Config
from selenium import webdriver

class WPTTest(unittest.TestCase):
    configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yml")
    config = Config(configPath)
    curEnv = config.getCfgValue("curEnv")
    url = config.getCfgValue(curEnv, "WPT", "url")

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

    def telSigning(self,applyNo,Recordfile="20170522-134150-880633-13823712568-1495431709.246927.WAV"):
        ie_opt  = webdriver.IeOptions()
        ie_opt.add_argument("--headless")
        browser = webdriver.Ie()
        browser.implicitly_wait(30)
        browser.get(self.url)
        userName = browser.find_element_by_id("userName")
        userName.clear()
        userName.send_keys("zhaosmb")

        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys("a1234567")

        submit_btn = browser.find_element_by_tag_name("button")
        submit_btn.click()

        telSign_img = browser.find_element_by_css_selector("[href=\"#/phoneSigningNew\"]")
        telSign_img.click()

        applySerialNo = browser.find_element_by_id("applySerialNo")
        applySerialNo.send_keys(applyNo)

        searchBtn = browser.find_element_by_css_selector("button[type=\"submit\"]")
        searchBtn.click()

        handleBtn = browser.find_element_by_link_text("处理")
        handleBtn.click()

        tab1 = browser.find_element_by_xpath("//div[contains(text(),\"通话录音\")]")
        tab1.click()

        uploadBtn = browser.find_element_by_xpath("//button/span[contains(text(),\"上传录音\")]")
        uploadBtn.click()

        fileName = browser.find_element_by_id("fileName")
        fileName.send_keys(Recordfile)

        confirmBtn = browser.find_element_by_xpath("//button/span[contains(text(),\"确 定\")]")
        confirmBtn.click()

        antmodalcloseBtn = browser.find_element_by_css_selector("button[class=\"ant-modal-close\"]")
        antmodalcloseBtn.click()

        submitBtn2 = browser.find_element_by_xpath("//button/span[contains(text(),\"提交任务\")]")
        submitBtn2.click()

        confirmBtn2 = browser.find_elements_by_xpath("//button/span[contains(text(),\"确 定\")]")
        confirmBtn2[1].click()

        browser.quit()

    def test_WPT_00001_案例名称(self):
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


