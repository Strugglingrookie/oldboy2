# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "4.4.2"
caps["deviceName"] = "127.0.0.1:62001"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = "com.tencent.mobileqq.activity.SplashActivity"
caps["unicodeKeyboard"] = True
caps["resetKeyboard"] = True
caps["noReset"] = True

driver = webdriver.remote("http://localhost:8888/wd/hub", caps)

el2 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el2.send_keys("11111")
driver.back()
els1 = driver.find_elements_by_id("btn_login")
els1[0].click()
els2 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
els2.send_keys("123123")

driver.quit()