# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/28 23:49
# @File   : 01unit_test.py

import unittest  # 导入unittest模块
import HTMLTestRunner


# 导入生成报告的模块，html生成的是方便给自己看的，
# xml生成的报告是以后给jekens用的，能自动识别测试报告内容


class MyTest(unittest.TestCase):  # 定义一个测试用例的类
    def testa(self):
        # 定义一个测试用例，注意，测试用例必须test开始，不然不会当做是测试用例
        '''a'''  # 描述，会同测试用例标题一并显示在测试报告里
        self.assertEqual(1, 1)
        # 测试用例断言，比较预期结果与实际结果，这里1==1，pass

    def testhaha(self):
        '''b'''
        self.assertEqual(2, 1)
        # 测试用例断言，比较预期结果与实际结果，这里2==1，Fail

    def testb(self):
        '''c'''
        self.assertEqual(3, 2)
        # 测试用例断言，比较预期结果与实际结果，这里3==1，Fail


class MyTest2(unittest.TestCase):
    def testc(self):
        '''d'''
        self.assertEqual(1, 1)

    def testhaha(self):
        '''e'''
        self.assertEqual(2, 1)

    def testd(self):
        '''f'''
        self.assertEqual(3, 2)


if __name__ == '__main__':
    # unittest.main()
    # 运行所有的测试用例，运行下面的代码时这个要注释

    suite = unittest.TestSuite()  # 定义一个测试套件
    # suite.addTest(MyTest('testa'))
    # suite.addTest(MyTest('testb'))
    # 添加测试用例方法一：往测试套件里新增一条测试用例
    # 测试用例只能用一种方法，同时两种会报错

    suite.addTest(unittest.makeSuite(MyTest))
    suite.addTest(unittest.makeSuite(MyTest2))
    # 添加测试用例方法二：往测试套件里新增这个类下的所有测试用例

    fw = open('report.html', 'wb')
    # 定义一个文件对象，给后面的HTMLTestRunner生成测试报告用
    # 注意打开方式必须是wb

    runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='Testing', description='desc')
    # 生成测试报告方法一：HTMLTestRunner，需要指定文件对象和标题

    # runner = xmlrunner.XMLTestRunner(output='.')
    # 生成测试报告方法二：xmlrunner，这个方法只要指定测试报告目录就可以

    runner.run(suite)
    # 运行，注意上述方法我写一起了，运行的话只能运行一种，另一个要注释
