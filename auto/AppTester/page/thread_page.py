from lib.appController import driver_queue
import threading
from lib.pyapp import Pyapp
from lib.logger import logger

local = threading.local()


class BasePage(object):
    def __init__(self, driver=None):
        try:
            local.driver = driver_queue.get()
            local.pyapp = Pyapp(local.driver)
        except Exception as e:
            logger.error('获取Driver出错：%s' % e)

    def quit(self):
        local.pyapp.quit()


class ThreadPage(BasePage):
    def url(self):
        local.pyapp.type('id=>url', 'http://ui.imdsx.cn')

    def enter(self):
        local.pyapp.key_code(66)

    def check(self,name):
        return local.pyapp.wait_and_save_exception('android=>new UiSelector().text("修改手势密码")', name)

class Page(ThreadPage):
    pass
