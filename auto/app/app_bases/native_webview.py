from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = 'com.android.browser.BrowserActivity'
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps["noReset"] = "True"
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print(driver.contexts)
try:
    ele1 = driver.find_element_by_id('android:id/button1')
    ele1.click()
except:
    pass

time.sleep(2)
ele2 = driver.find_element_by_id('com.android.browser:id/url')
ele2.clear()
ele2.send_keys('http://ui.imdsx.cn/uitester/')

time.sleep(2)
ele2.click()
driver.press_keycode(66)

time.sleep(2)
print(driver.contexts)

print(driver.current_context)
driver.switch_to.context(driver.contexts[-1])
print(driver.current_context)

time.sleep(2)
# driver.find_element_by_css_selector('#i1').send_keys('123456789')
