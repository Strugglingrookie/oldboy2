from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('http://ui.imdsx.cn/html/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0,1600)")


s = driver.find_elements_by_css_selector('select[name="city"]')[0]
# 返回第一个选中的optionElement对象
print(Select(s).first_selected_option)
# 返回所有选中的optionElement对象
print(Select(s).all_selected_options)
Select(s).select_by_index(3) # 选项索引 0开始
time.sleep(1)
Select(s).select_by_value('1') # value属性值
time.sleep(1)
Select(s).select_by_visible_text("北京") # 文本
time.sleep(1)

many_s = driver.find_elements_by_css_selector('select[name="city"]')[1]
# 多选
Select(many_s).select_by_index(3)
Select(many_s).select_by_value('1')
time.sleep(1)
# 取消所有选中的option
# Select(many_s).deselect_all()
Select(many_s).deselect_by_index(3)
Select(many_s).deselect_by_value('1')
Select(many_s).deselect_by_visible_text('辽宁')


