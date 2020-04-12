from lib.pyse import Pyse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.connectiontype import ConnectionType


class Pyapp(Pyse):
    def __init__(self,driver):
        self.d = driver

    @property
    def driver(self):
        return self.d

    def swipe_up(self,n=1,t=500):
        '''屏幕向上滚动'''
        l = self.d.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.85
        y2 = l['height'] * 0.5
        for i in range(n):
            self.d.swipe(x1,y1,x1,y2,t)

    def swipe_down(self, n=1, t=500):
        '''屏幕向下滚动'''
        l = self.d.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.5
        y2 = l['height'] * 0.85
        for i in range(n):
            self.d.swipe(x1, y1, x1, y2, t)

    def swipe_left(self,n=1,t=500):
        '''屏幕向左滚动'''
        l = self.d.get_window_size()
        y1 = l['height'] * 0.5
        x1 = l['width'] * 0.5
        x2 = l['width'] * 0.85
        for i in range(n):
            self.d.swipe(x1,y1,x2,y1,t)

    def swipe_right(self,n=1,t=500):
        '''屏幕向右滚动'''
        l = self.d.get_window_size()
        y1 = l['height'] * 0.5
        x1 = l['width'] * 0.85
        x2 = l['width'] * 0.5
        for i in range(n):
            self.d.swipe(x1,y1,x2,y1,t)

    def element_wait(self, css, secs=10):
        '''
        Waiting for an element to display.

        Usage:
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif by == "content":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.ACCESSIBILITY_ID, value)))
        elif by == "android":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, value)))
        elif by == "ios":
            WebDriverWait(self.driver, secs, 1).until(
                EC.presence_of_element_located((By.IOS_PREDICATE, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self,css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        elif by == "content":
            element = self.driver.find_element_by_accessibility_id(value)
        elif by == "android":
            element = self.driver.find_element_by_android_uiautomator(value)
        elif by == "ios":
            element = self.driver.find_element_by_ios_predicate(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class',"
                "'link_text','xpath','css','content','android','ios'.")
        return element

    def element_wait_click(self, css, secs=10):
        '''
        Waiting for an element to display.

        Usage:
        driver.element_wait("css=>#el",10)
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, value)))
        elif by == "content":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, value)))
        elif by == "android":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.ANDROID_UIAUTOMATOR, value)))
        elif by == "ios":
            WebDriverWait(self.driver, secs, 1).until(EC.element_to_be_clickable((By.IOS_PREDICATE, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def click(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait_click(css)
        el = self.get_element(css)
        el.click()

    def key_code(self, code):
        '''
        :param code: 按键码
        :return:
        '''
        self.d.press_keycode(code)

    def hide_keyboard(self):
        self.d.hide_keyboard()

    def background_app(self, second):
        self.d.background_app(second)

    @property
    def current_context(self):
        return self.d.current_context

    @property
    def context(self):
        return self.d.context

    @property
    def contexts(self):
        return self.d.contexts

    def switch_web_view(self):
        context_names = self.contexts
        if context_names > 1:
            self.d.switch_to.context(context_names[-1])

    def switch_native_app(self):
        context_names = self.contexts
        self.d.switch_to.context(context_names[0])

    def set_network(self, network):
        '''
        1、WIFI 2、数据流量 3、飞行模式 4、无网 5、全部打开
        '''
        if network == 1:
            self.d.set_network_connection(ConnectionType.WIFI_ONLY)
        elif network == 2:
            self.d.set_network_connection(ConnectionType.DATA_ONLY)
        elif network == 3:
            self.d.set_network_connection(ConnectionType.AIRPLANE_MODE)
        elif network == 4:
            self.d.set_network_connection(ConnectionType.NO_CONNECTION)
        elif network == 5:
            self.d.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        return self

    def launch_app(self):
        return self.d.launch_app()

    def close_app(self):
        return self.d.close_app()

    def reset(self):
        return self.d.reset()

    def is_app_installed(self, package):
        return self.d.is_app_installed(package)

    def remove_app(self,package):
        self.d.remove_app(package)

    def install_app(self,package):
        self.d.install_app(package)

    def set_value(self, element, value):
        self.d.set_value(element, value)

    def lock(self, s):
        self.d.lock(s)

    def wait_and_save_exception(self, css, name):
        try:
            self.element_wait(css, secs=5)
            return True
        except Exception as e:
            from lib.path import APPPICTUREPATH
            import threading
            self.get_windows_img(APPPICTUREPATH.format(threading.current_thread().getName()) + name + '.jpg')
            return False