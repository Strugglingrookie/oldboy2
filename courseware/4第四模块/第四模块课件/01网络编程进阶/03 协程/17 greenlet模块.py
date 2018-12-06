#pip3 install greenlet
from greenlet import greenlet
import time

def eat(name):
    print('%s eat 1' %name)
    time.sleep(10)
    g2.switch('egon')
    print('%s eat 2' %name)
    g2.switch()

def play(name):
    print('%s play 1' %name )
    g1.switch()
    print('%s play 2' %name )


g1=greenlet(eat)
g2=greenlet(play)

g1.switch('egon')