import unittest
import requests
from BeautifulReport import BeautifulReport
# import parameterized
from parameterized import parameterized

def get_data(file_name):
    data = [ ]
    with open(file_name,encoding='utf-8') as fr:
        for line in fr:
            line = line.strip()
            if line:
                data.append(line.split(','))
    return data

class LoginCase(unittest.TestCase):
    url = 'http://api.nnzhp.cn/api/user/login'

    @parameterized.expand(get_data('users.txt'))

    def test_login1(self,username,password,check):
        '''正常登陆的用例'''
        data = {'username':username,'passwd':password}
        result = requests.post(self.url,data).text
        self.assertIn(check,result,msg='没有返回%s'%check)



suite = unittest.makeSuite(LoginCase)  #把这个类里面的测试用例到加入到集合里面

bf = BeautifulReport(suite)
bf.report(description='好看的测试报告',filename='new_report.html')


# f = open('report.html','wb')
# runner = HTMLTestRunner.HTMLTestRunner(f,description='这个是测试报告描述',title='这个是报告标题')
# runner.run(suite)
# f.close()

