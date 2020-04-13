# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/3/13 21:27
# @File   : thread_page.py

import os,sys,time
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)
from lib.pyse import Pyse
from my_faker import PARAMS_MAP


class BasePage():
    def __init__(self):
        self.d = Pyse('chrome')
        self.driver = self.d.driver

    def add_cookies(self):
        cookies = '136a3d03-9748-4f83-a54f-9b2a93f979a0=1e348032-82cd-46e3-b419-4ef8acb912dc;'
        self.d.set_cookies(cookies)

    def url(self):
        self.d.open("https://testyyfax8446.yylending.com/web/user/index.html")

    def top(self):
        self.d.js("window.scrollTo(0,0)")

    def quit(self):
        self.d.quit()

    def close(self):
        self.d.close()


class Safe(BasePage):
    def my_info(self):
        self.d.click("css=>.nav-title-icon.yyicon-user-nav-info")

    def safe_authen(self):
        self.d.click("link_text=>安全认证")

    def deposit(self):
        self.d.click("link_text=>开通银行存管")

    def bankcard(self):
        self.d.type("css=>#deposit_bankcard", PARAMS_MAP['bankcard']())

    def name(self):
        self.d.type("css=>#deposit_name",PARAMS_MAP['name']())

    def idcard(self):
        self.d.type("css=>#deposit_idcard",PARAMS_MAP['card']())

    def next(self):
        self.d.click("css=>#deposit_create_btn")

    def switch_window(self):
        self.d.switch_window()

    def mobile(self):
        self.d.type("css=>#mobile", '13310830003')

    def verify_click(self):
        self.d.click("css=>#sendSmsVerify")

    def verify_code(self):
        self.d.type("css=>#smsCode",'123456')

    def password(self):
        self.d.type("css=>#password", 'a123456')

    def confirm_password(self):
        self.d.type("css=>#confirmPassword", 'a123456')

    def known(self):
        self.d.click("link_text=>我知道了")

    def agree(self):
        self.d.click("css=>#nextButton")

    def check_charge(self,name):
        return self.d.wait_and_save_exception("link_text=>去充值",name)


class Page(Safe):
    pass


if __name__ == '__main__':
    page = Page()
    page.url()
    page.add_cookies()
    page.url()
    page.my_info()
    page.safe_authen()
    page.deposit()
    page.bankcard()
    page.name()
    page.idcard()
    page.next()
    page.switch_window()
    page.mobile()
    page.verify_click()
    page.verify_code()
    page.password()
    page.confirm_password()
    page.known()
    page.agree()
    page.check_charge('check_charge')
    time.sleep(15)
    page.quit()
