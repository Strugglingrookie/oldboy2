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
    程序运行需要使用requests、xlrd、xlutils、yagmail模块
    安装命令：pip install requests
            pip install xlrd
            pip install xlutils
            pip install yagmail
            
###程序运行：
    python bin/start.py
    
###程序结构：
	atp/
	├── README
	├── atp #api主程目录
	│   ├── bin #atp 执行文件 目录
	│   │   ├── __init__.py
	│   │   ├── start.py  #启动目录
	│   ├── config #配置文件
	│   │   ├── settings.py #存放数据库配置和程序启动端口号
	│   ├── lib #主要程序逻辑都 在这个目录里
	│   │   ├── read_case.py  #读取测试用例
	│   │   ├── log_write.py  #写日志
	│   │   └── check_data.py #检查数据模块
	│   ├── cases  #测试用例
	│   ├── logs  #执行日志
	│   ├── report  #执行结果

	