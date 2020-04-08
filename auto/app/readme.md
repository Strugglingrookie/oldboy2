#app ui自动化测试框架
***

###程序说明：
    基于python unittest appium selenium pyse pyapp htmltestrunner
    设计总体思想page object，将每个页面抽象成对象，页面里每一个功能点抽象成函数
    优点：
    1 page obj 思想使得 case和元素解耦，利于维护
    2 WebDriverWait 增强了系统的稳定性，避免因为网络或者环境问题导致的异常
    3 wait_activity 等待activity出现，避免因为网络或者环境问题导致的异常
    4 二次开发 htmltestrunner ，增加用例执行失败的页面截图
    5 多线程同一个case 同时运行多个手机
    6 yaml 文件夹控制手机的配置信息
    7 通过代码实现appium的服务器自启
    8 
    
###实现功能如下：  
    1、继承unittest编写测试用例
    2、加载测试用例python文件
    3、HTMLTestRunner执行测试用例并生成测试报告
    
###依赖软件：
    程序运行需要使用unittest、HTMLTestRunner、selenium、appium模块
    安装命令：
        pip install selenium
        pip install unittest
                     
###程序运行：
    # 单线程运行
    python bin/main.py
    
    
###程序结构：
	auto/
	├── README
	├── web #upt主程序目录
	│   ├── bin #utp 执行文件 目录
	│   │   ├── __init__.py
	│   │   └──  main.py  #单线程执行测试用例
	│   ├── config #配置文件
	│   │   └── settings.py #存放host/邮箱等基础配置信息
	│   ├── lib #主要程序逻辑都 在这个目录里
	│   │   ├── pyse.py  #selenium 二次封装
	│   │   ├── tools.py  #工具模块 
	│   │   ├── log_write.py  #写日志
	│   │   └── HTMLTestRunner.py  #生成测试报告
	│   ├── page  #页面抽象目录
	│   │   └── page.py  #一个页面对应一个类，一个功能对应一个函数
	│   ├── test_case  #导入page.py,用unittest封装好的测试用例
	│   ├── log  #日志文件存放目录
	│   └── report  #执行结果存放目录
	│   │   └── picture  #存放用例执行失败的页面截图
	└── └── data  #存放参数化数据

	