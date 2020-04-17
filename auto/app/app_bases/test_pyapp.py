from lib.pyapp import Pyapp
from appium import webdriver
import time,threading,queue

drivers = queue.Queue()

desired_caps1 = {}
desired_caps1['platformName'] = 'Android'
desired_caps1['platformVersion'] = '5.1.1'
desired_caps1['deviceName'] = 'emulator-5556'
desired_caps1['appPackage'] = 'com.tencent.mobileqq'
desired_caps1['appActivity'] = '.activity.SplashActivity'
desired_caps1["unicodeKeyboard"] = "True"
desired_caps1["resetKeyboard"] = "True"
desired_caps1["noReset"] = "True"

desired_caps_out1 = {}
desired_caps_out1['url'] = 'http://127.0.0.1:7001/wd/hub'
desired_caps_out1['desired_caps'] = desired_caps1

desired_caps2 = {}
desired_caps2['platformName'] = 'Android'
desired_caps2['platformVersion'] = '5.1.1'
desired_caps2['deviceName'] = 'emulator-5558'
desired_caps2['appPackage'] = 'com.tencent.mobileqq'
desired_caps2['appActivity'] = '.activity.SplashActivity'
desired_caps2["unicodeKeyboard"] = "True"
desired_caps2["resetKeyboard"] = "True"
desired_caps2["noReset"] = "True"

desired_caps_out2 = {}
desired_caps_out2['url'] = 'http://127.0.0.1:7002/wd/hub'
desired_caps_out2['desired_caps'] = desired_caps2

desired_caps = [desired_caps_out1, desired_caps_out2]


def driver(conf):
    print('开始启动 %s' %conf)
    driver = webdriver.Remote(conf['url'], conf['desired_caps'])
    drivers.put(driver)
    print('启动成功 %s' % conf)

def fun():
    driver=drivers.get()
    pyapp = Pyapp(driver)
    pyapp.click('android=>new UiSelector().resourceId("com.tencent.mobileqq:id/btn_login")')
    pyapp.type('content=>请输入QQ号码或手机或邮箱','12345678')
    pyapp.type('content=>密码 安全','87654321')
    pyapp.click('id=>com.tencent.mobileqq:id/login')

# print('删除前：',pyapp.is_app_installed('com.tencent.mobileqq'))
# pyapp.remove_app('com.tencent.mobileqq')
# print('删除后：',pyapp.is_app_installed('com.tencent.mobileqq'))
# pyapp.install_app('E:\Automantic\win\qq.apk')
# print('安装后：',pyapp.is_app_installed('com.tencent.mobileqq'))

driver_threads = []
for conf in desired_caps:
    t = threading.Thread(target=driver,args=(conf,))
    driver_threads.append(t)

for t in driver_threads:
    t.start()
    t.join()

for driver in range(drivers.qsize()):
    t=threading.Thread(target=fun)
    t.start()

while threading.active_count() != 1:
    continue

print('done!')