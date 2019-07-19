#-*- coding: utf-8 -*-
import socket  #for sockets
import sys   #for exit
import json

try:
    #create an AF_INET, STREAM socket (TCP)++++++++++++++++创建SOCKET+++++++++++
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
    print 'Failed to create socket . Error code:'+str(msg[0])+'Error message:'+msg[1]
    sys.exit()
print 'socket Created'

#+++++++++++++++++++++++++连接服务器+++++++++++++++++++++
host = 'testchatc1.ktplay.cn'
port = 7000
#get remote_ip 
# try:
#     remote_ip = socket.gethostbyname(host)
# except socket.gaierror:
#     #could not resolve
#     print 'Hostname could not be resolved. Exiting'
#     sys.exit()
# print 'Ip address of ' + host + ' is ' + remote_ip
#Connect to remote server
remote_ip='10.210.3.160'
#ss = s.settimeout(10)    #timeout是一个浮点数，单位是秒。值为None表示没有超时期。
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
pii = s.connect((remote_ip,port))   #建立连接后又把连接给关闭了，，，，
print '这是连接服务器的信息：',pii
print 'socket Connect to '+host+' on ip '+remote_ip


# message = '{"cmd":"login", "token":"M2bSNDUSnpLavvam5F4X7fFhaq6YatOEaYNFvRs571usjp7Sk_cxZSBp8kOp8FaaFaLzrSAGSVSGXtMjSN_RGQ", "version":2, "r":0.1212}'
# # print message 
# # print "Send: {}".format(message)
# print '这是message:',message
# try:
#     #+++++++++++++++++++++++++++++发送消息+++++++++++++++++++++++++++
#     sendalls = s.sendall(message)
#     print '这是发送后的返回数据：',sendalls   #成功返回None，失败则抛出异常。
# except socket.error:
#     #发送失败
#     print 'Send failed'
#     sys.exit()
# print 'send successfully'
#  
# #+++++++++++++++++++++++++++++接收消息+++++++++++++++++++++++++++
# received = s.recv(5000)   #括号中的数字为要接收的最大数据量
# print '信息开始\n'+received+'信息结束'
#jresp = json.loads(received)    #decoded  JSON object

 
#+++++++++++++++++++++++++++++关闭socket++++++++++++++++++++++++
#s.close()

#{"cmd":"login", "version":"2","token":"M2bSNDUSnpLavvam5F4X7fFhaq6YatOEaYNFvRs571usjp7Sk_cxZSBp8kOp8FaaFaLzrSAGSVSGXtMjSN_RGQ","r":0.000000}
#{"cmd":"login", "token":"M2bSNDUSnpLavvam5F4X7fFhaq6YatOEaYNFvRs571usjp7Sk_cxZSBp8kOp8FaaFaLzrSAGSVSGXtMjSN_RGQ", "version":2, "r":"0.1212"}
#M2bSNDUSnpLavvam5F4X7fFhaq6YatOEaYNFvRs571usjp7Sk_cxZSBp8kOp8FaaFaLzrSAGSVSGXtMjSN_RGQ

