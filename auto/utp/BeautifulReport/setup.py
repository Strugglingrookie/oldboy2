#coding=utf-8
#!/usr/bin/env python
import sys,os,shutil
page_dir = 'site-packages'
for i in sys.path:
    if i.endswith(page_dir):
        page_path = i
name = 'BeautifulReport'
base_path = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(base_path,name)
target = os.path.join(page_path,name)
if os.path.exists(target):
    if sys.version_info[0]==3:
        tag = input('BeautifulReport模块已经安装过，是否要重新安装？\n'
                    '输入yes or no\n'
                    '输入其他值默认不重新安装\n'
                    '请输入：')
    else:
        tag = raw_input('BeautifulReport模块已经安装过，是否要重新安装？'
                    '输入yes or no'
                    '输入其他值默认不重新安装')
    if tag =='yes':
        shutil.rmtree(target)
        shutil.copytree(src, target)
else:
    shutil.copytree(src, target)
    print('success!')




