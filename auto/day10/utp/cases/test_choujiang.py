import unittest
from utlis.request import MyRequest
from utlis.db import my
from cases.base_case import BaseCase
import requests

class TestChoujiang(BaseCase):
    username = 'caozn667118'
    password = 'aA123456'

    def tearDown(self):
        my.execute_one('delete from app_myuser where username = "%s";'%self.username)


    def test_choujiang(self):
        '''测试正常抽奖流程'''
        self.register(self.username,self.password) #注册
        userid,sign = self.login(self.username,self.password) #登录
        data = {'userid':userid,'sign':sign}
        req_obj = MyRequest('/api/product/choice','get',data)
        print(req_obj.text)


    def test_choujiang2(self):
        '''测试抽奖次数过多的'''
        pass


