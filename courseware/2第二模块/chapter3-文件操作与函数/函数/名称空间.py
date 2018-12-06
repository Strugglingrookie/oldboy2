#_*_coding:utf-8_*_




n = 10

def func():
    n = 20
    print('func:',n )

    def func2():
        #n = 30
        print('func2',n)

        def func3():
            print("func3:",n)

        func3()

    func2()


func()


