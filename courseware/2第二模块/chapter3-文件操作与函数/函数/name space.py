#_*_coding:utf-8_*_




level = 'L0'
n = 22


def func():
    level = 'L1'
    n = 33
    print(locals())

    def outer():
        n = 44
        level = 'L2'
        print(locals(),n)

        def inner():
            level = 'L3'
            print(locals(),n) #此外打印的n是多少？


        inner()


    outer()


func()