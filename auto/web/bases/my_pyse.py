from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Pyse():
    def __init__(self,browser='chrome'):
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            option = webdriver.ChromeOptions()
            option.add_argument("--start-maximized")
            driver = webdriver.Chrome(chrome_options=option)
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        elif browser == 'edge':
            driver = webdriver.Edge()
        try:
            self.driver = driver
        except Exception:
            raise NameError(
                "Not found %s browser." % browser)

    def element_wait(self,css,time_out=10,poll=0.5):
        '''
        Waiting for an element to display.
        :param css: "css=>#el" 用css定位方式定位id=e1的元素
        :param time_out: 超时时间，超过10s还没出现抛异常
        :param poll: 步长，默认每隔0.5s查询一次
        :return: 等到元素函数结束没有返回值，超时时间内还没等到就报错。
        '''
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")
        by,value = css.split('=>')
        by = by.lower()
        if by == 'id':
            WebDriverWait(self.driver,time_out,poll).until(EC.presence_of_element_located((By.ID,value)))
        elif by == 'class':
            WebDriverWait(self.driver, time_out, poll).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == 'name':
            WebDriverWait(self.driver, time_out, poll).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == 'xpath':
            WebDriverWait(self.driver, time_out, poll).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == 'css':
            WebDriverWait(self.driver, time_out, poll).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif by == 'link_text':
            WebDriverWait(self.driver, time_out, poll).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == 'partial_link_text':
            WebDriverWait(self.driver, time_out, poll).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self,css):
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")
        by, value = css.split('=>')
        by = by.lower()
        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        elif by == 'link_text':
            element = self.driver.find_element_by_link_text(value)
        elif by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self,url):
        self.driver.get(url)

    def max_window(self):
        self.driver.maximize_window()

    def set_window(self,wide,high):
        self.driver.set_window_size(wide,high)

    def type(self,css,text):
        self.element_wait(css)
        element = self.get_element(css)
        element.send_keys(text)

    def clear(self,css):
        self.element_wait(css)
        element = self.get_element(css)
        element.clear()

    def click(self,css):
        self.element_wait(css)
        element = self.get_element(css)
        element.click()

    def right_click(self,css):
        self.element_wait(css)
        element = self.get_element(css)
        ActionChains(self.driver).context_click(element).perform()

    def move_to_element(self,css):
        self.element_wait(css)
        element = self.get_element(css)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self,css):
        self.element_wait(css)
        element = self.get_element(css)
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self,source_css,target_css):
        self.element_wait(source_css)
        self.element_wait(target_css)
        source = self.get_element(source_css)
        target = self.get_element(target_css)
        ActionChains(self.driver).drag_and_drop(source,target).perform()

    def click_text(self,text):
        text = "partial_link_text=>%s"%text
        self.element_wait(text)
        element = self.get_element(text)
        element.click()

    def close(self,css):
        self.driver.close()

    def quit(self,css):
        self.driver.quit()

    def submit(self,css):
        self.element_wait(css)
        element = self.get_element(css)
        element.submit()

    def F5(self):
        self.driver.refresh()

    def js(self,script):
        self.driver.execute_script(script)

    def get_attribute(self,css,attribute):
        self.element_wait(css)
        element = self.get_element(css)
        att = element.get_attribute(attribute)
        return att

    def get_text(self,css):
        self.element_wait(css)
        element = self.get_element(css)
        return element.text

    def get_display(self,css):
        self.element_wait(css)
        element = self.get_element(css)
        return element.is_displayed()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_window_img(self,file_path):
        self.driver.get_screenshot_as_file(file_path)

    def wait(self,time_out=10):
        self.driver.implicitly_wait(time_out)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self,css):
        self.element_wait(css)
        iframe = self.get_element(css)
        self.driver.switch_to.frame(iframe)

    def switch_to_frame_out(self):
        self.driver.switch_to.default_content()

    def open_new_window(self,css):
        original_window = self.driver.current_window_handle
        self.element_wait(css)
        element = self.get_element(css)
        element.click()
        handles = self.driver.window_handles
        for handle in handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)

    def wait_and_save_exception(self,css,file_path):
        try:
            self.element_wait(css)
            return True
        except Exception as e:
            self.get_window_img(file_path)
            return False

    def select_by_value(self,css,value):
        self.element_wait(css)
        element = self.get_element(css)
        Select(element).select_by_value(value)

    def select_by_index(self,css,index):
        self.element_wait(css)
        element = self.get_element(css)
        index = int(index)
        Select(element).select_by_value(index)


if __name__ == '__main__':
    driver = Pyse('chrome')
    driver.open('http://ui.imdsx.cn/uitester/')
    driver.js('window.scrollTo(0,0)')
    driver.type('css=>#i1','id from my_pyse')