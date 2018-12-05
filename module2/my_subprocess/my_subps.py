# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/30


import os,subprocess
# print(os.system("uname -a"))  #返回的数值表示命令执行状态，0表示执行成功,非0表示失败  操作系统里可以用echo $? 输出上一条命令的执行状态
# print(os.popen("uname -a").read())  #popen返回的值是命令执行结果，read()方法读取返回的结果
# print(os.popen("du -h").read())  #popen返回的值是命令执行结果，read()方法读取返回的结果

#subprocess 跟操作系统进行交互，os.system()类似
#subprocess模块，等于是让操作系统开了一个新的进程，但进程之间的数据是不能共享的，也就是命令执行得到的结果，python这个进程是拿不到的
#那么这里想拿到命令执行结果就需要用到操作系统合格中间管道了，类似与复制粘贴，先复制内容到操作系统内存，再从操作系统内存拷贝出来

# a = subprocess.run(["df","-h"])  #直接执行，不指定操作系统管道
# print(a.stdout)  #因为执行的时候没指定操作系统管道接收命令执行结果，所以这里读取的时候会报错

# a = subprocess.run(["df","-h"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)  #直接执行，不指定操作系统管道
# print(a.stdout)  #因为执行的时候指定了操作系统管道接收命令执行结果，所以这里读取的时候会报错
# print(a.stderr)  #有错的话会在这里现实

#不指定check,进程执行命令,选项出错的时候，python不会raise异常
# a = subprocess.run(["df","-hasd"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# print(a.stdout)  #输出为空
# print(a.stderr)  #这里会打印异常情况

# a = subprocess.run(["df","-hasd"],stderr=subprocess.PIPE,check=True)  #指定check,进程执行命令选项出错的时候，python直接raise异常

#当有管道符的时候，命令不能再用list，直接写成字符串，但是需要指定shell=True
# a = subprocess.run(["df -h | grep Size"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
# print(a.stdout)


#Popen  后台运行程序，和python主程序并行运行，不会影响python主程序的运行
# a = subprocess.run("sleep 10",shell = True,stdout=subprocess.PIPE)  #python主程序和shell命令是串行的，这里等待10s，python主程序才继续往下运行
# a = subprocess.Popen("sleep 10",shell = True,stdout=subprocess.PIPE)  #直接运行下一句了，和python主程序并行
# print(a.poll())  #获取命令执行结果，不影响python主程序，两边是并行的
# def sayhi():
#     print("run...  HELLO!")
# a = subprocess.Popen("sleep 10",shell = True,stdout=subprocess.PIPE,preexec_fn=sayhi) #preexec_fn在运行shell命令前，执行函数
# a = subprocess.Popen("echo $PWD;sleep 2",shell = True,cwd="/tmp",stdout=subprocess.PIPE,preexec_fn=sayhi) #cwd指定运行shell命令的目录
# a = subprocess.Popen("echo $PWD;sleep 2",shell = True,stdout=subprocess.PIPE,preexec_fn=sayhi) #cwd不指定则在启动python文件的当前目录
# a = subprocess.Popen("echo $PWD;sleep 100",shell = True,stdout=subprocess.PIPE,preexec_fn=sayhi)
# a.wait()  #等待命令执行完再继续往下走
# print(a.stdout.read())
# print(a.pid)  #获取进程id
# a.kill()  #杀掉进程  类似于 os.kill(pid,signal)
# a.terminate()  #终止进程
#communicate 可以和进程进行交互。发送数据到stdin,并从stdout接收输出，然后等待任务结束。但是只能交互一次
# a = subprocess.Popen('python3 guess_age.py',stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
# a.communicate(b'22')
# a.send_signal() #发信号




