from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings' # android 独有
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps["noReset"] = "True"
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# size = driver.get_window_size()
# height = size.get("height")
# width = size.get("width")
# # 像上滑动的操作
# sx = width*0.5
# sy = height *0.9
# ex = width*0.5
# ey = height*0.1
# print(size)
# driver.swipe(sx,sy,ex,ey,duration=500)







# from appium.webdriver.connectiontype import ConnectionType
# print(driver.network_connection)
# # driver.set_network_connection(ConnectionType.DATA_ONLY)
# # print(driver.network_connection)



# element = driver.find_element_by_id('com.android.browser:id/url')
# element.send_keys('http://ui.imdsx.cn/uitester/')
# import time
# time.sleep(2)
# # 执行按键码
# driver.press_keycode(66)
# # driver.keyevent()
# print(driver.current_context)
# print(driver.contexts)
#
#
# driver.switch_to.context(driver.contexts[-1])
# driver.find_element_by_css_selector('#i1').send_keys(111)













# driver.close_app()
# import time
# time.sleep(2)
# print('app已关闭，准备开启。')
# driver.launch_app()
# driver.background_app()
# print(driver.current_activity)
# driver.find_element_by_xpath('//*[@text="新用户"]').click()
# print(driver.current_activity)
# driver.start_activity('com.tencent.mobileqq','.activity.RegisterPhoneNumActivity')
# driver.wait_activity('.activity.RegisterPhoneNumActivity',10)
# driver.reset()


# driver.quit()


# 判断这个包是否安装了
# flag= driver.is_app_installed('com.tencent.mobileqq')
# print('删除前：%s'%flag)
# driver.remove_app('com.tencent.mobileqq')
# flag= driver.is_app_installed('com.tencent.mobileqq')
# print('删除后：%s'%flag)
#
# driver.install_app(r'C:\Users\bjhouyafan\Desktop\QQ_818.apk')
# flag= driver.is_app_installed('com.tencent.mobileqq')
# print('安装后：%s'%flag)





# # element = driver.find_element_by_id('com.tencent.mobileqq:id/btn_login')
# # element = driver.find_element_by_android_uiautomator('new UiSelector().text("登 录")')
# import time
# time.sleep(2)
# element = driver.find_element_by_xpath('//*[@text="登 录"]')
# time.sleep(2)
# element.click()
# # accessibility_id  与 content-desc对应
# e1 = driver.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱')
# e1.send_keys(1111111)
# driver.set_value()