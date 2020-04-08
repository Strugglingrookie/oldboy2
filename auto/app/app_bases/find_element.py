from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:5557'
desired_caps['appPackage'] = 'com.tencent.mobileqq'
desired_caps['appActivity'] = '.activity.SplashActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps["noReset"] = "True"
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(4)
# ID定位于selenium不同，可能存在重复的问题。
# appium-desktop抓取元素时如果出现有id，则可以直接用。
# resource-id可能出现重复，需要具体看下有多少个。
# driver.find_element_by_id('resource-id')
ele1 = driver.find_element_by_id('com.tencent.mobileqq:id/btn_login')
ele1.click()

time.sleep(2)
# Android对应content-desc IOS对应accessibility identifier
# content-desc是给残障人士定义的特殊字段
# ele2 = driver.find_element_by_accessibility_id('content-desc')
ele2 = driver.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱')
ele2.send_keys('1234567')

time.sleep(2)
# Xpath路径定位，与Web的Xpath定位在有一点点区别
# Native App的定位以class为基准，主要用到参数有text、resource-id、index
# driver.find_element_by_xpath('//android.widget.EditText[@text="手机号"]')
ele3 = driver.find_element_by_xpath('//*[@content-desc="密码 安全"]')
ele3.send_keys('7654321')

'''
# 对应class字段，有可能存在多个相同class。
# 多个相同class，每次获取只取第一个遇到的元素。
driver.find_element_by_class_name('class')

# 这个在运行时，调用的是Android自带的UI框架UiAutomator的Api
# 介绍几个简单常用的，text、className、resource-id
# text
# 匹配全部text文字
driver.find_element_by_android_uiautomator('new UiSelector().text("手机号")')
# 包含text文字
driver.find_element_by_android_uiautomator('new UiSelector().textContains("机")')
# 以text什么开始
driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith("手")')
# 正则匹配text
driver.find_element_by_android_uiautomator('new UiSelector().textMatches("^手.*")')

# className
driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.TextView")')
# classNameMatches
driver.find_elements_by_android_uiautomator('new UiSelector().classNameMatches("^android.widget.*")')

# resource-id、resourceIdMatches
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.syqy.wecash:id/et_content")')

# description
driver.find_element_by_android_uiautomator('new UiSelector().description("S 日历")')
# descriptionStartsWith
driver.find_element_by_android_uiautomator('new UiSelector().descriptionStartsWith("日历")')
# descriptionMatches
driver.find_element_by_android_uiautomator('new UiSelector().descriptionMatches(".*历$")')

# Native App 暂不能使用
driver.find_element_by_tag_name('')

# Native App 暂不能使用
driver.find_element_by_partial_link_text('')

# Native App 暂不能使用
driver.find_element_by_link_text('')

# Native App 暂不能使用
driver.find_element_by_css_selector('')
'''



# ele2.send_keys('123456')