from lib.pyapp import Pyapp
from appium import webdriver


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

# pyapp.click('android=>new UiSelector().resourceId("com.tencent.mobileqq:id/btn_login")')
# pyapp.type('content=>请输入QQ号码或手机或邮箱','12345678')
# pyapp.type('content=>密码 安全','87654321')
# pyapp.click('id=>com.tencent.mobileqq:id/login')

# print('删除前：',pyapp.is_app_installed('com.tencent.mobileqq'))
# pyapp.remove_app('com.tencent.mobileqq')
# print('删除后：',pyapp.is_app_installed('com.tencent.mobileqq'))
# pyapp.install_app('E:\Automantic\win\qq.apk')
# print('安装后：',pyapp.is_app_installed('com.tencent.mobileqq'))

print('done')