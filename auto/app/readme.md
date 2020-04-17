#app ui自动化测试框架
***

###程序说明：
    基于python unittest selenium appium pyse pyapp htmltestrunner
    设计总体思想page object，将每个页面抽象成对象，页面里每一个功能点抽象成函数
    优点：
    1 page obj 思想使得 case和元素解耦，利于维护
    2 WebDriverWait 增强了系统的稳定性，避免因为网络或者环境问题导致的异常
    3 wait_activity 等待activity出现，避免因为网络或者环境问题导致的异常
    4 二次开发 htmltestrunner ，增加用例执行失败的页面截图
    5 多线程同一个case 同时运行多个手机
    6 yaml 控制手机的配置信息
    7 通过代码实现appium的服务器自启,adb自启
    8 根据yml配置启动对应device数量的线程数，并发运行case，每个device生成一个测试报告
    9 错误的case，会将当前app的页面截图保存，方便后续定位问题
    
###实现功能如下：  
    1、继承unittest编写测试用例
    2、加载测试用例python文件
    3、HTMLTestRunner执行测试用例并生成测试报告
    4、appium服务自启，多个driver同时运行case，生成对应测试报告
    
###依赖软件：
    程序运行需要使用unittest、HTMLTestRunner、selenium、appium模块
    安装命令：
        pip install selenium
        pip install unittest
        pip install appium_python_client
                     
###程序运行：
    # 多线程运行
    python bin/thread_main.py
    
    
###程序结构：
	auto/
	├── README
	├── app # app主程序目录
	│	│   ├── appCase  # 导入page.py,用unittest封装好的测试用例
	│   ├── bin # app 执行文件 目录
	│   │   └──  thread_main.py  #多线程执行测试用例
	│   ├── conf # 配置文件
	│   │   ├── appController.yml # appium启动ip/port以及手机配置、待测app信息
	│ 	│   └── settings.py # 存放路径、日志等基础配置信息
	│   ├── lib #主要程序逻辑都 在这个目录里
	│   │   ├── appController.py  # qppium服务启动、driver启动
	│   │   ├── HTMLTestAppRunner.py  # 生成测试报告
	│   │   ├── log_write.py  # 写日志
	│   │   ├── pyapp.py  # 基于 pyse 的二次封装，增加appium的方法
	│   │   ├── pyse.py  # selenium 的二次封装 
	│   │   ├── result.py   # 存放生成测试报告的数据
	│   │   └── tools.py   # 工具模块
	│   ├── log  #日志文件存放目录
	│   ├── page  #页面抽象目录
	│   │   └── thread_page.py  #一个页面对应一个类，一个功能对应一个函数
	│   └── report  #执行结果存放目录
	│   │   ├── error_pictures  # 存放用例执行失败的页面截图
	└── └── └── html_report  # 存放测试报告

	