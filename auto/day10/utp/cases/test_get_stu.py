import unittest
from utlis.request import MyRequest
from parameterized import parameterized
from utlis.tools import get_data_form_text

class TestStudentInfo(unittest.TestCase):
    @parameterized.expand(get_data_form_text('stus'))
    def test_stu_info(self,stu_name):
        data = {'stu_name':stu_name}
        url = '/api/user/stu_info'
        req_obj = MyRequest(url,'get',data)
        self.assertIn(stu_name,req_obj.text,'学生不存在')




