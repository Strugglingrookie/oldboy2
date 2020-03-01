#单元测试自动化系统
***

###程序说明：
    实现接口自动化测试
    
###实现功能如下：  
    1、继承unittest编写测试用例
    2、加载测试用例python文件
    3、BeautifulReport执行测试用例并生成测试报告
    4、发送邮件
    
###依赖软件：
    程序运行需要使用requests、unittest、yagmail、jsonpath、flask、pymysql、parameterized模块
    安装命令：
        pip install requests
        pip install unittest
        pip install yagmail
        pip install jsonpath
        pip install flask
        pip install pymysql
        pip install parameterized
            
            
###程序运行：
    # 启动api server
    python bin/flask_server.py
    
    # 单线程运行
    python bin/start.py
    
    
###程序结构：
	atp/
	├── README
	├── atp #upt主程序目录
	│   ├── bin #utp 执行文件 目录
	│   │   ├── __init__.py
	│   │   ├── flask_server.py  #启动api接口服务端
	│   │   └──  start.py  #单线程执行测试用例
	│   ├── config #配置文件
	│   │   └── settings.py #存放host/邮箱等基础配置信息
	│   ├── lib #主要程序逻辑都 在这个目录里
	│   │   ├── operate.py  #操作数据库
	│   │   ├── tools.py  #工具模块 如校验json子集等
	│   │   ├── log_write.py  #写日志
	│   │   └── request_send.py  #写日志
	│   ├── cases  #测试用例py文件存放目录
	│   ├── logs  #日志文件存放目录
	│   └── report  #执行结果存放目录
	└── └── data  #存放参数化数据

	