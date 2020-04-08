from lib.pyapp import Pyapp
from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = '.activity.SplashActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps["noReset"] = "True"
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

pyapp = Pyapp(driver)

# time.sleep(4)
# ele1 = driver.find_element_by_id('com.tencent.mobileqq:id/btn_login')
# ele1.click()
# time.sleep(2)
# ele2 = driver.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱')
# ele2.send_keys('1234567')
# time.sleep(2)
# ele3 = driver.find_element_by_xpath('//*[@content-desc="密码 安全"]')
# ele3.send_keys('7654321')

pyapp.click('android=>new UiSelector().resourceId("com.tencent.mobileqq:id/btn_login")')
pyapp.type('content=>请输入QQ号码或手机或邮箱','12345678')
pyapp.type('content=>密码 安全','87654321')

print('done')