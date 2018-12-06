#_*_coding:utf-8_*_


def func():


    n = 10

    def func2():

        print("func2:",n )

    return func2


f = func()
print(f)
f()