# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/13 21:27
# @File   : thread_page.py


from lib.pyse import Pyse


class BasePage():
    def __init__(self):
        self.d = Pyse('chrome')
        self.driver = self.d.driver

    def url(self):
        self.d.open("http://ui.imdsx.cn/uitester/")

    def top(self):
        self.d.js("window.scrollTo(0,0)")

    def quit(self):
        self.d.quit()


class IdTest(BasePage):
    def test_id(self):
        self.d.type("css=>#i1","Web aotu test!")

    def check_id(self,name):
        return self.d.wait_and_save_exception("css=>#i1",name)


class Page(IdTest):
    pass


if __name__ == '__main__':
    mytest = Page()
    mytest.url()
    mytest.top()
    mytest.test_id()
    mytest.check_id('mytest')
