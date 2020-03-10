# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/6 8:41
# @File   : 01location.py


from selenium import webdriver


driver = webdriver.Chrome()  # 创建浏览器server
driver.get("http://ui.imdsx.cn/uitester/")  # 打开url
driver.maximize_window() # 放大浏览器窗口
driver.execute_script('window.scrollTo(0,0)') # 执行js脚本

'''
# 18 钟定位方式 8种单数 8钟复数 2种上层定位方式
# 1 id定位
driver.find_element_by_id('i1').send_keys('id from my se')
# 2 class定位
driver.find_element_by_class_name('classname').send_keys('classname from my se')
# 3 name
driver.find_element_by_name('name').send_keys('name from my se')
# 4 xpath
xobj = driver.find_element_by_xpath('//input[@placeholder="请通过XPATH定位元素"]')
xobj.send_keys('xpath from my se')
# 5 css_selector
driver.find_element_by_css_selector('#i1').send_keys('css from my se')
# 6 tag_name 会重复，只取第一个，一般不用
driver.find_element_by_tag_name('input').send_keys('tag_name from my se')
# 7 link_test 标签的文本
driver.find_element_by_link_text('跳转大师兄博客地址').click()
# 8 partial_linx_text 标签文本模糊匹配
driver.find_element_by_partial_link_text('大师兄').click()
'''

# 复数定位
elements = driver.find_elements_by_id('i1')
print(elements)
ele = elements[0]
ele.send_keys('复数定位')

# 底层定位 上面的单数和复数定位都是调用的下面两个方法
driver.find_element('class name','classname').send_keys('底层find_element')
driver.find_elements('id','i1')[0].send_keys('底层find_elements')



