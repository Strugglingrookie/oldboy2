# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 8:37
# @Author  : Xiao


# 自定义异常
class XgError(BaseException):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    raise XgError("自定义的异常！")

except Exception as e:
    print(e)

#3 异常
#强调一：错误发生的条件如果是可以预知的，此时应该用if判断去预防异常
AGE=10
age=input('>>: ').strip()

if age.isdigit():
    age=int(age)
    if age > AGE:
        print('太大了')


#强调二：错误发生的条件如果是不可预知的，此时应该用异常处理机制，try...except
try:
    f=open('a.txt','r',encoding='utf-8')

    print(next(f),end='')
    print(next(f),end='')
    print(next(f),end='')
    print(next(f),end='')

    print(next(f),end='')
    print(next(f),end='')
    print(next(f),end='')
    f.close()
except StopIteration:
    print('出错啦')

print('====>1')

#多分支：被监测的代码块抛出的异常有多种可能性，并且我们需要针对每一种异常类型都定制专门的处理逻辑
try:
    print('===>1')
    # name
    print('===>2')
    l=[1,2,3]
    # l[100]
    print('===>3')
    d={}
    d['name']
    print('===>4')

except NameError as e:
    print('--->',e)

except IndexError as e:
    print('--->',e)

except KeyError as e:
    print('--->',e)

print('====>afer code')

#万能异常：Exception,被监测的代码块抛出的异常有多种可能性，
# 并且我们针对所有的异常类型都只用一种处理逻辑就可以了，那就使用Exception
try:
    print('===>1')
    # name
    print('===>2')
    l=[1,2,3]
    l[100]
    print('===>3')
    d={}
    d['name']
    print('===>4')

except Exception as e:
    print('异常发生啦：',e)

print('====>afer code')

try:
    print('===>1')
    # name
    print('===>2')
    l=[1,2,3]
    # l[100]
    print('===>3')
    d={}
    d['name']
    print('===>4')

except NameError as e:
    print('--->',e)

except IndexError as e:
    print('--->',e)

except KeyError as e:
    print('--->',e)

except Exception as e:
    print('统一的处理方法')


print('====>afer code')

#其他结构
try:
    print('===>1')
    # name
    print('===>2')
    l=[1,2,3]
    # l[100]
    print('===>3')
    d={}
    d['name']
    print('===>4')

except NameError as e:
    print('--->',e)

except IndexError as e:
    print('--->',e)

except KeyError as e:
    print('--->',e)

except Exception as e:
    print('统一的处理方法')

else:
    print('在被检测的代码块没有发生异常时执行')

finally:
    print('不管被检测的代码块有无发生异常都会执行')

# print('====>afer code')

# finally的应用
try:
    f=open('a.txt','r',encoding='utf-8')
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))

    print(next(f))
    print(next(f))
finally:
    f.close()
