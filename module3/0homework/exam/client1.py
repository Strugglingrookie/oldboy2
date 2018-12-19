import socket,struct,json


server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_socket.connect(("127.0.0.1",8081))  # 主动初始化TCP服务器连接
while True:
    msg = input(">>>>:").strip()
    if not msg: continue
    msg_bytes = msg.encode()
    server_socket.send(msg_bytes) # 发送的数据必须是bytes类型

    header_len_bytes = server_socket.recv(4) # 接收4个字节的数据头信息
    header_len = struct.unpack("i",header_len_bytes)[0] # struct.unpack解压数据，得到数据头信息长度
    header_str = server_socket.recv(header_len).decode("utf-8") # 根据上面的长度接收数据头信息
    header = json.loads(header_str,encoding="utf-8")
    file_size = header["file_size"] # 根据数据头信息得到本次要接收的数据大小
    recv_size = 0
    res = b''
    while recv_size < file_size:  # 当接收到的数据小于本次数据长度时就一直接收
        res += server_socket.recv(10) # 将每次接收到的数据拼接
        recv_size = len(res) # 实时记录当前接收到的数据长度
    res = res.decode("GBK") # 这里是windows，搜索一GBK格式打印返回数据
    print(res)

server_socket.close()