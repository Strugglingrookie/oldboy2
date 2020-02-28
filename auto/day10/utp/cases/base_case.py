import unittest
from utlis.request import MyRequest
from utlis.tools import get_value
class BaseCase(unittest.TestCase):
    def login(self,username,passwd):
        data = {'username':username,'passwd':passwd}
        req_obj = MyRequest('/api/user/login','post',data)
        userid = get_value(req_obj.result,'userId')
        sign = get_value(req_obj.result,'sign')
        self.assertIn('userId',req_obj.text)
        return userid,sign

    def register(self,username,password):
        data = {'username':username,'pwd':password,'cpwd':password}
        req_obj = MyRequest('/api/user/user_reg','post',data)
        self.assertIn('成功',req_obj.text)


    def clear_data(self):
        print('清理数据')





