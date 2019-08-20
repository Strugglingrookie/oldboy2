#coding=utf-8
import os
import unittest
from config import Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def element_path_visible(driver, element_path, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, element_path)))
        return True
    except TimeoutException:
        return False

class OmsTest(unittest.TestCase):
    configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yml")
    config = Config(configPath)
    curEnv = config.getCfgValue("curEnv")
    url = config.getCfgValue(curEnv, "OMS", "url")

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

    def performJob(self,jobName):
        chrm_opt = webdriver.ChromeOptions()
        chrm_opt.add_argument("--headless")
        browser = webdriver.Chrome(options=chrm_opt)
        browser.implicitly_wait(30)
        mainUrl = "%s/user/login"%self.url
        browser.get(mainUrl)
        browser.maximize_window()
        userName = browser.find_element_by_id("userId")
        userName.clear()
        userName.send_keys("xizq")

        password = browser.find_element_by_id("password")
        password.clear()
        password.send_keys("a1234567")

        submit_btn = browser.find_element_by_tag_name("button")
        submit_btn.click()

        icon1 = browser.find_element_by_xpath("//div[@class=\"ant-layout-sider-children\"]/ul/li[1]")
        icon1.click()

        link1 = browser.find_element_by_partial_link_text("轮询管理")
        link1.click()

        input1 = browser.find_element_by_xpath(
            "//div[contains(@class,\"ant-form-item-label\")][contains(string(),\"任务名\")]/following-sibling::div[1]/descendant::input[1]")
        input1.send_keys(jobName)

        searchBtn = browser.find_element_by_xpath("//button[@type=\"submit\"][contains(string(),\"查 询\")]")
        searchBtn.click()

        element_path_visible(browser, "//table/thead/tr/th[1]/descendant::input[1]", 5)
        checkBox1 = browser.find_element_by_xpath("//table/thead/tr/th[1]/descendant::input[1]")
        checkBox1.click()

        performBtn = browser.find_element_by_xpath("//button[contains(string(),\"立即执行\")]")
        performBtn.click()

        confirmBtn = browser.find_element_by_xpath("//div[@class=\"ant-popover-buttons\"]/button[2]")
        confirmBtn.click()

        browser.quit()


    def test_OMS_00001_案例名称(self):
        # 测试步骤
        # 结果判断
        a, b, x = "", "", ""
        self.assertEqual(a, b)  # a == b
        self.assertNotEqual(a, b)  # a != b
        self.assertTrue(x)  # bool(x) is True
        self.assertFalse(x)  # bool(x) is False
        self.assertIs(a, b)  # a is b
        self.assertIsNot(a, b)  # a is not b
        self.assertIn(a, b)  # a in b
        self.assertNotIn(a, b)

if __name__ == '__main__':
    unittest.main()