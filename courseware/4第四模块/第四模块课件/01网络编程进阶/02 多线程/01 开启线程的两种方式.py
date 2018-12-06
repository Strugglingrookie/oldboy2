# import time
# import random
# from threading import Thread
#
# def piao(name):
#     print('%s piaoing' %name)
#     time.sleep(random.randrange(1,5))
#     print('%s piao end' %name)
#
# if __name__ == '__main__':
#     t1=Thread(target=piao,args=('egon',))
#     t1.start()
#     print('主线程')
#


import time
import random
from threading import Thread

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print('%s piaoing' %self.name)

        time.sleep(random.randrange(1,5))
        print('%s piao end' %self.name)

if __name__ == '__main__':
    t1=MyThread('egon')
    t1.start()
    print('主')