import time
import threading
import queue
import subprocess
import os
from conf.settings import logger,LOG_DIR,APP_PICTUREPATH
from lib.tool import Tool
from appium import webdriver


# 多线程数据隔离
local = threading.local()
# 存放driver队列
drivers_queue = queue.Queue()
# 存放手机设备名称队列
devices_name_queue = queue.Queue()
# 查看当前手机配置
# logger.debug(Tool().app_data)

class Controller():
    def __init__(self):
        self.tool = Tool()
        # 配置信息
        self.yml = self.tool.app_data
        # 所有手机配置信息
        self.devices = self.yml.get('devices')
        # 测试app信息 包名 入口等
        self.app = self.yml.get('tester')
        # Android or IOS
        self.device_type = self.yml.get('device_type')
        # 启动的服务端口列表，用于校验服务是否成功启动
        self.ports = []

    def kill_servers(self):
        """
        每次运行之前杀掉之前所有的服务
        adb如果重启  夜游神将不会被查到
        """
        logger.debug('执行[KILL SERVER]操作:%s' % subprocess.getoutput("taskkill /F /IM node.exe /t"))
        logger.debug('关闭ADB服务！%s' % subprocess.run(["adb","kill-server"],stdout=subprocess.PIPE).stdout)

    def server_start_command(self, **kwargs):
        '''
        根据kwargs中ip、端口等信息 启动appium服务
        '''
        command = 'appium -a {ip} -p {port} -U {deviceName} -g {log}'.format(ip=kwargs.get('ip'),
                                                                             port=kwargs.get('port'),
                                                                             deviceName=kwargs.get(
                                                                                 'deviceName'),
                                                                             log=kwargs.get('log_path'))
        logger.debug('启动服务执行的命令：%s' % command)
        subprocess.Popen(command, stdout=open(kwargs.get('log_path'), 'a+'), stderr=subprocess.PIPE, shell=True)

    def server_start(self):
        '''
        根据配置的手机信息，启动对应的appium服务
        '''
        # 每次启动前 清掉上一次还存活的端口
        self.kill_servers()
        logger.debug('启动ADB服务！%s' % subprocess.getoutput("adb start-server"))
        # 启动的server加入到这个列表，用来等待所有服务启动起来之后才往下运行
        server_threads = []
        for device in self.devices.get(self.device_type):
            # 将手机操作log加载到配置中
            log_path = {'log_path': os.path.join(LOG_DIR, '%s.log' % device.get('name'))}
            device.update(log_path)
            logger.debug("每个手机的信息：%s" % device)
            # 提取校验服务启动成功的端口
            self.ports.append(device.get('port'))
            # 启动多线程开启服务
            t = threading.Thread(target=self.server_start_command, kwargs=device)
            server_threads.append(t)
            t.start()
        for i in server_threads:
            i.join()


    def check_server(self):
        '''
        校验所有appium服务是否启动成功
        :return: True
        '''
        while True:
            for port in self.ports:
                # 通过查看是否有返回值来确定是否启动
                res = subprocess.getoutput("netstat -ano | findstr %s" % port)
                # 如果有 则从list中删除这个端口 直到这个list为空时 代表启动成功 跳出循环
                if res:
                    logger.debug('检验appium服务启动：%s' % res)
                    self.ports.remove(port)
                else:
                    logger.debug('端口 [%s] 服务启动失败5秒钟后尝试' % port)
            if not self.ports:
                break
            time.sleep(5)
        logger.debug('全部appium服务启动成功！')
        return True

    def driver_start_command(self,**kwargs):
        '''
        driver启动命令
        :param kwargs: 被测app配置，如包名，入口等
        :return:
        '''
        local.desired_caps = {'platformName': '', 'platformVersion': '', 'deviceName': '',
                              "unicodeKeyboard": "True",
                              "resetKeyboard": "True", 'udid': '', 'noReset': 'True'}
        local.desired_caps.update(kwargs)
        port = local.desired_caps.get('port')
        ip = local.desired_caps.get('ip')
        url = 'http://{ip}:{port}/wd/hub'.format(port=port,ip=ip)
        logger.debug('url:%s 开始启动'%url)
        driver = webdriver.Remote(url, local.desired_caps)
        logger.debug('url:%s 启动成功' % url)
        # 通过消息对列传递driver驱动
        drivers_queue.put(driver)
        # 存放手机名称的对列(用于后续对线程名进行区分)
        devices_name_queue.put(local.desired_caps.get('name'))
        # 创建错误图片存放的路径
        app_picture_path = APP_PICTUREPATH.format(local.desired_caps.get('name'))
        # 如果存在则清除目录下的所有内容
        if os.path.exists(app_picture_path):
            # 调用写好的clear方法
            self.tool.app_clear(app_picture_path)
        else:
            # 如果不存在path 则递归创建目录
            os.makedirs(app_picture_path)

    def driver_start(self):
        driver_threads = []
        for device_app in self.devices.get(self.device_type):
            # 将测试的app信息增加到 手机的配置文件中
            device_app.update(self.app)
            # 多线程启动
            t = threading.Thread(target=self.driver_start_command, kwargs=device_app)
            driver_threads.append(t)
            t.start()
        for i in driver_threads:
            i.join()
        # 所有driver启动成功后 返回driver的mq
        return drivers_queue


if __name__ == '__main__':
    c = Controller()
    c.server_start()
    c.check_server()
    c.driver_start()

