#api接口自动化系统
***

###程序说明：
    实现接口自动化测试
    
###实现功能如下：  
    1、读取excel
    2、调用接口
    3、校验结果
    4、发送邮件
    
###依赖软件：
    程序运行需要使用requests、xlrd、xlutils、yagmail、jsonpath、flask模块
    安装命令：
        pip install requests
        pip install xlrd
        pip install xlutils
        pip install yagmail
        pip install jsonpath
        pip install flask
            
            
###程序运行：
    # 启动api server
    python bin/flask_server.py
    
    # 单线程运行
    python bin/start.py
    
    # 多线程运行
    python bin/start_threads.py
    
###程序结构：
	atp/
	├── README
	├── atp #api主程序目录
	│   ├── bin #atp 执行文件 目录
	│   │   ├── __init__.py
	│   │   ├── flask_server.py  #启动api接口服务端
	│   │   ├── start.py  #单线程执行测试用例
	│   │   └── start_threads.py  #多线程执行测试用例(excel维度)
	│   ├── config #配置文件
	│   │   └── settings.py #存放host/邮箱等基础配置信息
	│   ├── lib #主要程序逻辑都 在这个目录里
	│   │   ├── utils.py  #工具箱 如写结果/校验结果
	│   │   ├── read_case.py  #读取测试用例
	│   │   ├── log_write.py  #写日志
	│   │   ├── request_send.py  #写日志
	│   │   └── parse_response.py #检查数据模块
	│   ├── cases  #测试用例存放目录
	│   ├── logs  #日志文件存放目录
	│   └── report  #执行结果存放目录

	