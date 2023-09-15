import socket

HOST = '127.0.0.1'  # 服务端IP地址
PORT = 8888  # 服务端端口号

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口号
server_socket.bind((HOST, PORT))

# 开始监听，最大连接数为5
server_socket.listen(5)
print('Server is listening on {}:{}'.format(HOST, PORT))

# 等待客户端连接
client_socket, client_address = server_socket.accept()
print('Client connected from {}:{}'.format(client_address[0], client_address[1]))

while True:
    # 接收客户端发送的数据
    data = client_socket.recv(1024)
    print('Received data:', data.decode())
    print(repr(data.decode()))

    # 向客户端发送数据
    # 客户端发送的数据等于 exit ，退出循环
    if not data or data.decode('utf-8') == 'exit':
        break
    client_socket.send('收到数据'.encode())

# 关闭客户端连接
client_socket.close()
print("连接关闭")

