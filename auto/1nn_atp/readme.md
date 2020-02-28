#atp接口自动化框架
***

###程序说明：
    这个接口自动化框架，用来跑接口自动化的。
    
###实现功能如下：  
    1、读取excel
    2、调用接口
    3、校验结果
    4、发送报告
###依赖软件：
    程序运行需要使用requests、xlrd、nnlog、yagmail、xlutils模块
    安装命令：pip install xlrd
    安装命令：pip install requests
            pip install nnlog
            
    
###程序运行：
    python bin/start.py

    
###程序结构：
	atp/
	├── README
	├── atp #api主程目录
	│   ├── bin #szz_api 执行文件 目录
	│   │   ├── __init__.py
	│   │   ├── start.py  #启动目录
	│   ├── config #配置文件
	│   │   ├── setting.py #存放数据库配置和程序启动端口号
	│   ├── lib #主要程序逻辑都 在这个目录里
	│   │   ├── __init__.py
	│   │   ├── api.py  #主要业务逻辑
	│   │   ├── op_db.py  #操作数据库公共方法
	│   │   └── check_data.py #检查数据模块
	│   ├── data  #用户数据存储的地方
    │   │   ├── init.sql  # 建数据库表
    │   │   ├── res_msg.py  #返回信息
	│   │   └── __init__.py

	

