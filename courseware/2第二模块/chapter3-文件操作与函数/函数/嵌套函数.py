#_*_coding:utf-8_*_

name = "Alex"


def change_name():
    name = "Alex2"

    def change_name2():
        name = "Alex3"
        print("第3层打印", name)

    change_name2()  # 调用内层函数
    print("第2层打印", name)


change_name2()
print("最外层打印", name)