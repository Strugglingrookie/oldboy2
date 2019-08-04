from django.shortcuts import render
import  datetime


def index(request):
    # 模板变量
    n_bool = True
    digits = 123
    string = 'hello world!'
    lis = [1,2,3,'a']
    dic = {'name': 'xg','age':18, 'height':180}
    lis2 = []
    filesize = 12345678
    now = datetime.datetime.now()
    ops = "<script type='text/javascript'>alert('js脚本强制弹窗')</script>"
    class Person:
        def __init__(self,name,age):
            self.name = name
            self.age = age
    jack = Person('jack',22)
    rose = Person('rose',25)
    person_lis = [jack,rose]
    # person_lis = []
    # return render(request, 'index.html',{'digits':digits,'string':string,'lis':lis,'dic':dic,'jack':jack,'rose':rose,'person_lis':person_lis})
    # 如果变量太多，字典就很长了，所以这里可以写成locals() 将当前名称空间的变量都传给模板。
    return render(request, 'index.html',locals())