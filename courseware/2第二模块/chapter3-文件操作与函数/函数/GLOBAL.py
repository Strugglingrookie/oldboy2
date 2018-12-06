#_*_coding:utf-8_*_

#name = "Alex Li"


def change_name():
    global name
    name = "Alex 又名 金角大王,路飞学城讲师"
    print("after change", name)


change_name()

print("在外面看看name改了么?", name)
