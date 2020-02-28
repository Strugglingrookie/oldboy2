import requests
import unittest
from urllib.parse import urljoin
import jsonpath
def get_value(d,k):
    '这个函数是用来从返回结果里面获取key的'
    result = jsonpath.jsonpath(d,'$..%s'%k)
    if result:
        return result[0]
    return ''

class AddProduct(unittest.TestCase):
    base_url = 'http://api.nnzhp.cn'

    def login(self):
        print('test_login')
        uri = '/api/user/login'
        url = urljoin(self.base_url,uri)

        data = {'username':'niuhanyang','passwd':
                'aA123456'}
        response = requests.post(url,data).json()
        user_id = get_value(response,'userId')
        sign = get_value(response,'sign')
        return user_id,sign

    def test_choice(self):
        print('test_choice')
        user_id,sign = self.login()
        uri = '/api/product/choice'
        url = urljoin(self.base_url,uri)
        response = requests.get(url,{'userid':user_id,'sign':sign}).json()
        print(response)

unittest.main()
