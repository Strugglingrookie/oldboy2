from lib.pyapp import Pyapp
from lib.appController import drivers_queue
from conf.settings import logger
import threading


local = threading.local()

class BasePage():
    def __init__(self,driver=None):
        if not driver:
            try:
                local.driver = drivers_queue.get()
                local.pyapp = Pyapp(local.driver)
            except Exception as e:
                logger.error('获取Driver出错：%s' % e)
        else:
            local.pyapp = Pyapp(driver)

    def quit(self):
        local.pyapp.quit()


class ThreadPage(BasePage):
    def login_btn(self):
        local.pyapp.click('android=>new UiSelector().resourceId("com.tencent.mobileqq:id/btn_login")')

    def account(self):
        local.pyapp.type('content=>请输入QQ号码或手机或邮箱', '3418666179')

    def password(self):
        local.pyapp.type('content=>密码 安全', '3280789xg')

    def login(self):
        local.pyapp.click('id=>com.tencent.mobileqq:id/login')

    def check(self,name):
        return local.pyapp.wait_and_save_exception('android=>new UiSelector().text("开始验证")', name)

class Page(ThreadPage):
    pass


if __name__ == '__main__':
    # from appium import webdriver
    # desired_caps = {}
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5.1.1'
    # desired_caps['deviceName'] = 'emulator-5554'
    # desired_caps['appPackage'] = 'com.tencent.mobileqq'
    # desired_caps['appActivity'] = '.activity.SplashActivity'
    # desired_caps["unicodeKeyboard"] = "True"
    # desired_caps["resetKeyboard"] = "True"
    # desired_caps["noReset"] = "True"
    # driver = webdriver.Remote('http://127.0.0.1:7071/wd/hub', desired_caps)
    from lib.appController import Controller
    c = Controller()
    c.server_start()
    c.check_server()
    c.driver_start()
    page = Page()
    page.login_btn()
    page.account()
    page.password()
    page.login()
    page.check('test')






