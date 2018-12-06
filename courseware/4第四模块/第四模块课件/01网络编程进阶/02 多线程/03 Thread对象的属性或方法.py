from threading import Thread,currentThread,active_count,enumerate
import time

def task():
    print('%s is ruuning' %currentThread().getName())
    time.sleep(2)
    print('%s is done' %currentThread().getName())

if __name__ == '__main__':
    t=Thread(target=task,name='子线程1')
    t.start()
    # t.setName('儿子线程1')
    # t.join()
    # print(t.getName())
    # currentThread().setName('主线程')
    # print(t.isAlive())


    # print('主线程',currentThread().getName())

    # t.join()
    # print(active_count())
    print(enumerate())