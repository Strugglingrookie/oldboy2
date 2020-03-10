# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/6 17:44
# @File   : 02selenium_api.py


import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://ui.imdsx.cn/uitester/')
driver.maximize_window()
driver.execute_script('window.scrollTo(0,0)')

ele = driver.find_element_by_css_selector('#dis1')
ele.click()


time.sleep(3)
driver.quit()