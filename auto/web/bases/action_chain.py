from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('http://ui.imdsx.cn/uitester/')
driver.maximize_window()
driver.execute_script('window.scrollTo(0,0)')


div = driver.find_element_by_css_selector('#a')
ele = driver.find_element_by_css_selector('#dis1')
# is_displayed 判断元素是否可见
print(ele.is_displayed()) # False 元素不可见

# 实例化指令链 ActionChains
action = ActionChains(driver)
# move_to_element 鼠标移动到指定元素 div   click 点击元素ele
action.move_to_element(div).click(ele).perform() # 正常弹窗
print(ele.is_displayed()) #True

# drag_and_drop
# 将source元素拖放至target元素处，参数为两个elementObj
ActionChains(driver).drag_and_drop(source=source, target=target)

# 将一个source元素 拖动到针对source坐上角坐在的x y处 可存在负宽度的情况和负高度的情况
ActionChains(driver).drag_and_drop_by_offset(source, x, y)

# 这种也是拖拽的一种方式，都是以源元素的左上角为基准，移动坐标
ActionChains(driver).click_and_hold(dom).move_by_offset(169, 188).release().perform()

# move_to_element

# 鼠标移动到某一个元素上,结束elementObj
ActionChains(driver).move_to_element(e)

# 鼠标移动到制定的坐标上，参数接受x，y
ActionChains(driver).move_by_offset(e['x'], e['y'])


# click
# 单击事件,可接受elementObj
ActionChains(driver).click()

# 双击事件,可接受elementObj
ActionChains(driver).double_click()

# 点击鼠标右键
ActionChains(driver).context_click()

# 点击某个元素不松开,接收elementObj
ActionChains(driver).click_and_hold()

# # 某个元素上松开鼠标左键,接收elementObj
ActionChains(driver).release()


# key_down与key_up

# 有时我们需要模拟键盘操作时，那么就需要用到ActionChains中的key操作了，
# 提供了两个方法，key_down与key_up，模拟按下键盘的某个键子，与松开某个键子，接收的参数是按键的Keys与elementObj。
# 可以与send_keys连用（例：全选、复制、剪切、粘贴）

# key_down 模拟键盘摁下某个按键 key_up 松开某个按键，与sendkey连用完成一些操作，每次down必须up一次否则将出现异常
ActionChains(driver).key_down(Keys.CONTROL,dom)\
    .send_keys('a').send_keys('c').key_up(Keys.CONTROL)\
    .key_down(Keys.CONTROL,dom1).send_keys('v')\
    .key_up(Keys.CONTROL).perform()