# -*- coding:utf-8 -*-
# __author__="X1gang"
# Date:2018/11/30


# with open("contact.txt","r") as f:
#     for i in f:
#         print(i.split())  #split默认所有空字符，如空格 tab 换行

import re

# 引子
# f = open("contact.txt","r")
# data = f.read()
# res = re.findall(r"1[0-9]{10}",data)
# print(res)
# f.close()

# # re常用匹配语法------------------------------------------------------------------------------------------------------
# import re
#
#
# s = "abc1d3e"
# #match 从头开始匹配，只会匹配一次，返回的是一个对象  re.match(pattern, string, flags=0)
# res = re.match(r"[0-9]",s)  #None 因为第一个不是数字
# res = re.match(r"[0-9]","1sef")  #第一个字符是1，所以可以匹配到
# res = re.match(r"\w",s)  # 第一个字符是a，所以可以匹配到
#
# #search 全局匹配，找到就返回，返回的是一个对象 re.search(pattern, string, flags=0)
# res = re.search(r"[0-9]",s)  # 全局存在数字1，所以可以匹配到 <re.Match object; span=(3, 4), match='1'> 这个3就是匹配到的索引
# #因为match和search返回的是对象，所以需要用group方法取之取值，但如果不存在匹配的值，group会报错，所以需要加一层判断
# if res:
#     print(res.group())
#
# #findall 找到字符串中所有符合表达式的值，返回的是一个列表 re.findall(pattern, string, flags=0)
# res = re.findall(r"[0-9]",s)  # ['1', '3']
# print(res)
#
# #split 以匹配的字符当作列表分割符 re.split(pattern, string, maxsplit=0, flags=0)
# res = re.split("\d+","123asd456qwe789zxc")  #实质是和findall的方法相反 结果['', 'asd', 'qwe', 'zxc']
# res = re.split("\d+","poi123asd456qwe789zxc",2)  #分割两次 结果['poi', 'asd', 'qwe789zxc']
# res = re.split("\d+|-|#","123asd456qwe789zxc-asd#jack")  #以数字或者-号或者#号分割 结果['', 'asd', 'qwe', 'zxc', 'asd', 'jack']
# res = re.split("\|","12qwe789|zxck")  #以|符分割，但是|是语法，需要\转义 结果 ['12qwe789', 'zxck']
# res = re.split("\\\\","12qwe789\zxck")  #以\符分割，但是\是mac的路径，需要\\\转义,少一个\都会报错 结果 ['12qwe789', 'zxck']
#
# #sub 匹配到的字符串替换成新的字符串 re.sub(pattern, repl, string, count=0, flags=0)
# res = re.sub("\d+","--","123xiao456gang789yang",2) #将数字替换成--，只替换前两个匹配的数字 结果 --xiao--gang789yang
#
# #fullmatch 整个字符串匹配成功才返一个对象 否则返回None re.fullmatch(pattern, string, flags=0)
# res = re.fullmatch("\w+@\w+\.(com|cn|edu)","xg@163.edu")
#
# #compile  返回的是一个规则对象，供其他方法调用 re.compile(pattern, flags=0)
# #如果匹配规则用的特别频繁，用compile提高效率。（compile等于是把规则先编译好了，后面调用，不需要每次用的时候都重新编译）
# pattern = re.compile("\w+@\w+\.(com|cn|edu)")
# res = pattern.fullmatch("xg@163.edu")
# print(res)


# 常用表达式规则------------------------------------------------------------------------------------------------------
import re


s = "abc1d3e"
# res = re.search(r'..',"\n!#%^")  # .匹配任意一个字符，除了\n
# res = re.search(r'^asd',"asd!#%^")  # ^匹配开头   ^等于是把search变成了match
# res = re.search(r'b$',"bsaaad!#%^b")  # $匹配结尾 匹配以b结尾
# res = re.search(r'a*',"gfdaaasd!#%^b")  # *匹配前一个字符 0次或多次 匹配结果为空
# res = re.search(r'a*',"aaagfdd!#%^b")  # *匹配前一个字符 0次或多次 匹配结果为 aaa
# res = re.search(r'ab+',"aaabbbgfdd!#%^b")  # +匹配前一个字符(贪婪匹配) 1次或多次 匹配结果为 abbb
# res = re.search(r'ab?',"aabbbgfdd!#%^b")  # ?匹配前一个字符 1次或0次,优先0次，找到a就返回 匹配结果为 a
# res = re.search(r'ab?',"abbbgfdd!#%^b")  # {}匹配前一个字符 1次或0次,优先0次，找到a就返回 匹配结果为 ab
# res = re.search(r'b{3}',"abbbbbgfdd!#%^b")  # {m}匹配前一个字符m次(必须m次)  匹配结果为 bbb
# res = re.search(r'b{2,4}',"abbbbbgfdd!b")  # {n,m}匹配前一个字符n到m次，找到符合n-m次且不能往后匹配即返回  匹配结果为 bbbb
# res = re.search(r'b{2,4}',"abbasdbbbbbbfdd")  # {n,m}匹配前一个字符n到m次，找到符合n-m次且不能往后匹配即返回  匹配结果为 bb
# res = re.search(r'Xg|xg',"Xg")  # | 或，匹配Xg或xg
# res = re.search(r'(X|x)g',"Xg")  # | 或，匹配Xg或xg
# res = re.search(r'[a-z]+[0-9]+',"xg123")  # (...) 分组匹配 匹配结果 xg123
# res = re.search(r'([a-z]+)([0-9]+)',"xg123")  # (...) 分组匹配 匹配结果 需要用groups查看分组匹配结果 如果还是用group，结果仍然是xg123
# print(res.groups())  #结果为 ('xg', '123')  一个小括弧就是一个组
# res = re.search("\Axg","xg123") #\A 从开头开始匹配，加了\A等于^,使得search 类似于 match  结果 xg
# res = re.search("\Zxg","123xg") #\Z 匹配字符结尾，加了\A等于$, 结果 xg
# res = re.search("\d","xg123") #\d 匹配数字 等价于 [0-9] 结果 1
# res = re.search("\d+","xg123") #\d 匹配数字 等价于 [0-9] 结果 123
# res = re.search("\D+","xg123") #\D 匹配非数字 结果 xg
# res = re.search("\w+","xg123#¥%¥#$") #\w匹配字母/数字 等价于 [A-Za-z0-9] 结果 xg123
# res = re.search("\W+","xg123#¥%¥#$") #\W匹配非 字母/数字 等价于 特殊字符 结果 #¥%¥#$
# res = re.search("\s","xg123\ndb456") #s匹配空白字符\t \n \r 结果 \n
# res = re.findall("\s","xg123\ndb456\tkj789\r") #s匹配空白字符\t \n \r 结果 ['\n', '\t', '\r']
res = re.search("(?P<province>\d{3})(?P<city>\d{3})(?P<year>\d{4})","430522199910258888") #分组匹配有一个groupdict的方法直接拿到一个字典
print(res.groupdict())  #得到一个字典，在后面的djgon会用来解析url  结果 ： {'city': '522', 'year': '1999', 'province': '430'}
# print(res)


# re Flags标识位------------------------------------------------------------------------------------------------------
import re


#re.I 忽略大小写
print(re.search("x","Xg"))  # 结果 None
print(re.search("x","Xg",re.I))  # 结果 X

# re.M 多行模式，改变'^'和'$'的行为
print(re.search('foo.$','foo1\nfoo2\n').group())  #结果foo2,匹配的时候忽略掉了 \n，当作一行来处理
print(re.search('foo.$','foo1\nfoo2\n',re.M).group())  #结果foo1  当做两行来处理

# s 改变.的行为  .本来是匹配除了换行符意外的所有字符，加上这个s标志后，可以匹配换行符
print(re.search('.','\n'))  # 结果 None
print(re.search('.','\n',re.S))  #结果  \n

# x 表达式可以写注释
print(re.search('. #test','xg'))  # 结果 None
print(re.search('.','xg',re.S))  #结果  x

import re


# 1.验证手机号是否合法
pattern = re.compile("^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$")
while True:
    phone = input(">>:")
    res = pattern.fullmatch(phone)
    print(res)

# 2.验证邮箱是否合法
pattern = re.compile("\w+@\w+\.(com|cn|edu)$")
while True:
    email = input(">>:")
    res = pattern.fullmatch(email)
    print(res)

# 3.开发一个简单的python计算器，实现加减乘除及拓号优先级解析
# 用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，
# 必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必须与真实的计算器所得出的结果一致
# re.search(r'\([^()]+\)',s).group()#可拿到最里层的括号中的值
# '(-40/5)'
val = "1 - 2 * ( 60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
def cal(val):
    try:
        while True:
            tmp = re.findall("\([^\(\)]+\)",val)
            if tmp :
                for i in tmp :
                    val = val.replace(i,str(eval(i)))
                    print(val)
            else:
                res = eval(val)
                print(res)
                break
    except Exception as e:
        print(e,"\n",val)
cal(val)
