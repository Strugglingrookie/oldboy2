from socket import *
from threading import Thread

def communicate(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()



server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    print('starting...')
    conn, addr = server.accept()
    print(addr)

    t=Thread(target=communicate,args=(conn,))
    t.start()

server.close()
