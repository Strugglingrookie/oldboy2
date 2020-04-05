from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = '.BrowserActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps["noReset"] = "True"
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 判断app是否已安装
flag = driver.is_app_installed('com.tencent.mobileqq')
print('删除前',flag)

# 安装app
driver.install_app(r"E:\Automantic\win\qq.apk")
flag = driver.is_app_installed('com.tencent.mobileqq')
print('重新安装',flag)

# 删除app
driver.remove_app('com.tencent.mobileqq')
flag = driver.is_app_installed('com.tencent.mobileqq')
print('删除后',flag)



