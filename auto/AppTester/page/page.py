from lib.appController import driver_queue
from lib.pyapp import Pyapp
import threading

# driver 多线程运行是进行线程之间的数据隔离
local = threading.local()


# 配置在实例化时，去mq中获取创建好的driver，如果调试page则需要传递driver
class BasePage(object):
    def __init__(self, driver=None):
        if driver is None:
            local.driver = driver_queue.get()
            local.pyapp = Pyapp(local.driver)
        else:
            local.driver = driver
            local.pyapp = Pyapp(driver)

    def quit(self):
        local.app.quit()

    def reset_package(self):
        local.pyapp.reset()


class QQ_Login_Page(BasePage):
    def login(self):
        local.pyapp.click('android=>new UiSelector().text("登 录")')

    def username(self):
        local.pyapp.type('content=>请输入QQ号码或手机或邮箱', 3408467505)

    def passwd(self):
        local.pyapp.type('content=>密码 安全', 'besttest123')

    def login_check(self, name):
        return local.pyapp.wait_and_save_exception('android=>new UiSelector().text("登 录")', name)



class Page(QQ_Login_Page):
    pass
