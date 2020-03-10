from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://ui.imdsx.cn/uitester/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0,0)")


'''
# switch_to.window
handles = driver.window_handles
print("创建新tab前的 tab有",handles)
# 正常定位到该tab页面的元素和操作
ele = driver.find_element_by_css_selector('#i1')
ele.send_keys("old tab")

new_tab = driver.find_element_by_link_text("新建标签页面")
new_tab.click()
new_handles = driver.window_handles
print("创建新tab后的 tab有",new_handles)

# 创建了新页面后发现这个正常操作
ele.send_keys("创建新tab后再来操作")

# switch_to 切换到新的tab页面后 正常定位和操作元素
driver.switch_to.window(new_handles[-1])
new_ele = driver.find_element_by_css_selector('#newtag')
new_ele.send_keys('write in new_tab')
'''

# switch_to.frame()
# 有两种切换到ifrme的方式
# 1 先定位到iframe这个元素，然后切换到这个元素
# my_iframe = driver.find_element_by_css_selector('[name="top-frame"]')
# driver.switch_to.frame(my_iframe)
# ele = driver.find_element_by_css_selector("#newtag")
# ele.send_keys('input into top-frame')

# 2 直接通过iframe的 name id切换
# driver.switch_to.frame('top-frame')
# ele = driver.find_element_by_css_selector("#newtag")
# ele.send_keys('input into top-frame')

# 多层iframe切换
# driver.switch_to.frame('top-frame')
# driver.switch_to.frame('baidu-frame')
# ele = driver.find_element_by_css_selector("#kw")
# ele.send_keys('input into baidu-frame')


# switch_to.alert()
ele = driver.find_element_by_css_selector('#alert')
ele.click()
# driver.switch_to.alert.text 获取alert文本内容
print(driver.switch_to.alert.text)

# accept 确认alert弹框
time.sleep(1)
driver.switch_to.alert.accept()

# dismiss 取消alert弹框
ele.click()
time.sleep(1)
driver.switch_to.alert.dismiss()