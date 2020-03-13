from lib.pyse import Pyse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.connectiontype import ConnectionType


class Pyapp(Pyse):
    def __init__(self, driver):
        self.d = driver

    @property
    def driver(self):
        return self.d

    def swipe_up(self, t=500, n=1):
        """向上滑动屏幕"""
        l = self.d.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.85  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.d.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t=500, n=1):
        """向下滑动屏幕"""
        l = self.d.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.d.swipe(x1, y1, x1, y2, t)

    def swipe_left(self, t=500, n=1):
        """向左滑动屏幕"""
        l = self.d.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        for i in range(n):
            self.d.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t=500, n=1):
        """向右滑动屏幕"""
        l = self.d.get_window_size()
        x1 = l['width'] * 0.05
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.d.swipe(x1, y1, x2, y1, t)

    def get_element(self, css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        self.element_wait(css)

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            element = self.d.find_element_by_id(value)
        elif by == "name":
            element = self.d.find_element_by_name(value)
        elif by == "class":
            element = self.d.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.d.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.d.find_element_by_xpath(value)
        elif by == "css":
            element = self.d.find_element_by_css_selector(value)
        elif by == 'content':
            element = self.d.find_element_by_accessibility_id(value)
        elif by == 'android':
            element = self.d.find_element_by_android_uiautomator(value)
        elif by == 'ios':
            element = self.d.find_element_by_ios_predicate(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def get_elements(self, css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        self.element_wait(css)

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            elements = self.d.find_elements_by_id(value)
        elif by == "name":
            elements = self.d.find_elements_by_name(value)
        elif by == "class":
            elements = self.d.find_elements_by_class_name(value)
        elif by == "link_text":
            elements = self.d.find_elements_by_link_text(value)
        elif by == "xpath":
            elements = self.d.find_elements_by_xpath(value)
        elif by == "css":
            elements = self.d.find_elements_by_css_selector(value)
        elif by == 'content':
            elements = self.d.find_elements_by_accessibility_id(value)
        elif by == 'android':
            elements = self.d.find_elements_by_android_uiautomator(value)
        elif by == 'ios':
            elements = self.d.find_elements_by_ios_predicate(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return elements

    def element_wait(self, css, secs=8):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.ID, value)))
        elif by == "name":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.NAME, value)))
        elif by == "class":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.d, secs, 1).until(EC.presence_of_element_located((MobileBy.CSS_SELECTOR, value)))
        elif by == "content":
            WebDriverWait(self.d, secs, 1).until(
                EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, value)))
        elif by == 'android':
            WebDriverWait(self.d, secs, 1).until(
                EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, value)))
        elif by == 'ios':
            WebDriverWait(self.d, secs, 1).until(
                EC.presence_of_element_located((MobileBy.IOS_PREDICATE, value)))
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def random_action(self, css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]
        try:
            if by == "id":
                return EC.visibility_of_element_located((MobileBy.ID, value))
            elif by == "name":
                return EC.visibility_of_element_located((MobileBy.NAME, value))
            elif by == "class":
                return EC.visibility_of_element_located((MobileBy.CLASS_NAME, value))
            elif by == "link_text":
                return EC.visibility_of_element_located((MobileBy.LINK_TEXT, value))
            elif by == "xpath":
                return EC.visibility_of_element_located((MobileBy.XPATH, value))
            elif by == "css":
                return EC.visibility_of_element_located((MobileBy.CSS_SELECTOR, value))
            elif by == "content":
                return EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, value))
            elif by == 'android':
                return EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, value))
            elif by == 'ios':
                return EC.visibility_of_element_located((MobileBy.IOS_PREDICATE, value))
            else:
                raise NameError(
                    "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        except Exception as e:
            pass

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
