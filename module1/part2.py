# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 16:31
# @Author  : Xiao

# 需求：
# 可依次选择进入各子菜单
# 可从任意一层往回退到上一层
# 可从任意一层退出程序
# 所需新知识点：列表、字典

# 踩分点:
# 1. 实现功能70分；
# 2. 只用一个while循环，且整体代码量多于15行需求全部完成给85分(数据源dict不算代码量)；
# 3. 只用一个while循环，且整体代码量少于15行90分。

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

location = []  #用户当前所在位置，类似于目录
while True:
    tmp_menu = menu
    for i in location:
        tmp_menu = tmp_menu[i]
    print("当前目录下的子菜单有：\033[1;31;42m %s \033[0m"%'    '.join(list(tmp_menu.keys())))
    choice = input("输入q退出/b返回上级菜单或输入菜单名称进入子菜单:\n").strip()
    if choice.upper() == "Q":
        exit()
    elif  choice.upper() == "B" and len(location)>=1:
        del location[len(location)-1]
    elif tmp_menu.get(choice):
        location.append(choice)
    else:
        print("当前位置在顶级菜单或者最底菜单,或者您输入的子菜单不存在，不能输入\033[1;31;43m %s \033[0m！"%choice)