from socket import *
from threading import Thread,currentThread

def client():
    client=socket(AF_INET,SOCK_STREAM)
    client.connect(('127.0.0.1',8090))


    while True:
        client.send(('%s hello' %currentThread().getName()).encode('utf-8'))
        data=client.recv(1024)
        print(data.decode('utf-8'))

    client.close()


if __name__ == '__main__':
    for i in range(500):
        t=Thread(target=client)
        t.start()