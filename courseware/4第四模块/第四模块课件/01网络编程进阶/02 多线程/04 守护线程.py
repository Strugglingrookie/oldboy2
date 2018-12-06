# from threading import Thread
# import time
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t=Thread(target=sayhi,args=('egon',))
#     # t.setDaemon(True) #必须在t.start()之前设置
#     t.daemon=True
#     t.start()
#
#     print('主线程')
#     print(t.is_alive())
#


from threading import Thread
import time

def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.daemon=True
    t1.start()
    t2.start()
    print("main-------")


    '''
    123
    456
    main-------
    end123
    end456
    
    '''
