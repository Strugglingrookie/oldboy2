from appium import webdriver
import time
# https://www.cnblogs.com/bluestorm/p/4886662.html
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = '.BrowserActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps["noReset"] = "True"
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print(driver.network_connection)
from appium.webdriver.connectiontype import ConnectionType
driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
e = driver.find_element_by_id('url')
e.send_keys('http://ui.imdsx.cn')
time.sleep(2)
driver.press_keycode(66)
# t = driver.current_activity
# print(t)
# driver.find_element_by_android_uiautomator('new UiSelector().text("新用户")').click()
# t = driver.current_activity
# print(t)
# driver.start_activity('com.tencent.mobileqq','.activity.RegisterPhoneNumActivity')
# driver.wait_activity()
# driver.background_app(2)
# swipe
# d = driver.get_window_size()
# height = d.get('height')
# width = d.get('width')
# sx = width * 0.5
# sy = height * 0.85
# ex = width * 0.5
# ey = height * 0.25
# driver.swipe(sx, sy, ex, ey, duration=500)
# driver.swipe(sx, ey, ex, sy, duration=500)

# desired_caps = {}
# desired_caps['platformName'] = 'IOS'
# desired_caps['platformVersion'] = '10.3.3'
# desired_caps['deviceName'] = 'iphone'
# desired_caps['udid'] = '22f0e7d4909bdadd3aa242b2e7ebdbe21ce4800d'
# desired_caps['bundleId'] = 'com.zcbl.BeiJingJiaoJing'
# desired_caps["automationName"] = "XCUITest"
# desired_caps["unicodeKeyboard"] = "True"
# desired_caps["resetKeyboard"] = "True"
# desired_caps["noReset"] = "True"

