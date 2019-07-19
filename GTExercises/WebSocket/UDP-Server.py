# -*- coding: utf-8 -*- 
import socket
import sys

host = ''
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(10)
conn,addr = s.accept()   #accept方法返回一个含有两个元素的 元组(connection,address)。
print 'Connected with ' + addr[0] + ':' + str(addr[1])

# #UDP的东西
# port=8081
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #从指定的端口，从任何发送者，接收UDP数据
# s.bind(('',port))
# print('正在等待接入...')
# while True:
#     #接收一个数据
#     data,addr=s.recvfrom(1024)
#     print('Received:',data,'from',addr)

# Echo server program
# import socket
#  
# HOST = ''                 # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(1)
# conn, addr = s.accept()
# print 'Connected by', addr
# while 1:
#     data = conn.recv(1024)
#     if not data: break
#     conn.sendall(data)
# conn.close()
# # Echo client program
# import socket
#  
# HOST = 'daring.cwi.nl'    # The remote host
# PORT = 50007              # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# s.sendall('Hello, world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)