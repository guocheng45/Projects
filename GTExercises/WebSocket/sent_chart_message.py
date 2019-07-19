#-*- coding: utf-8 -*-
# from socket import *
# 
# class TcpClient:
#     #测试，连接本机
#     HOST='127.0.0.1'
#     #设置侦听端口
#     PORT=1122 
#     BUFSIZ=1024
#     ADDR=(HOST, PORT)
#     def __init__(self):
#         self.client=socket(AF_INET, SOCK_STREAM)
#         self.client.connect(self.ADDR)
# 
#         while True:
#             data=input('>')
#             if not data:
#                 break
#             #python3传递的是bytes，所以要编码
#             self.client.send(data.encode('utf8'))
#             print('发送信息到%s：%s' %(self.HOST,data))
#             if data.upper()=="QUIT":
#                 break            
#             data=self.client.recv(self.BUFSIZ)
#             if not data:
#                 break
#             print('从%s收到信息：%s' %(self.HOST,data.decode('utf8')))
#             
#             
# if __name__ == '__main__':
#     client=TcpClient()

import sys
import json
import time
from websocket import create_connection    #证明可用。。。
ws = create_connection("ws://testchatc1.ktplay.cn:7000")
print "Sending 'request login'..."
ws.send('{"cmd":"login", "token":"mlvud8-TeYfCk6FUr3LiexxkuHhWofPeR7Le9dH2JX0wJ3KBSa9TtOBvXz3QA9bguwHz3zCez5b75mvXmXrL5Q", "version":2, "r":0.1212}')
print "Sent"
print "Reeiving..."
result =  ws.recv()  #输出一个内容是json的字符串
dic1 = eval(result)  #使用eval将json字符串转化为字典
error_code = dic1.get('err')   #在字典中查询error码；此处说明dic.get是一个宽泛的获取值不会出错直接取value则有可能出错
#然后对错误码进行判断登录是否成功
print "error_code '%s'" % error_code
if error_code == '':
    print 'login success'
else:
    print 'Falied:',error_code
    sys.exit()
def send_message(send_str):
    ws.send(send_str)
    result =  ws.recv()
    dic1 = eval(result)  #使用eval将json字符串转化为字典
    error_code = dic1.get('err')   #在字典中查询error码；此处说明dic.get是一个宽泛的获取值不会出错直接取value则有可能出错
    #然后对错误码进行判断登录是否成功
    if error_code == '':
        print "send message success"
    else:
        print 'message failed:',error_code
        
print sys.argv #这是一个数组的嘛，然后0是python文件，后一个参数。。。
if len(sys.argv) != 3:
    print 'parameters not right'
    sys.exit()
#i = int(sys.argv[2])-1
times1 = int(sys.argv[2])
to_uid = int(sys.argv[1])
for i in range(times1):
    messges='hello'+str(i)
    r=i
    dic_str={'cmd':'msg','type':1, 'to_uid':400013689, 'msg':'zheshishenme dongxi sa ?', 'metadata':'', 'r':1.2335}
    dic_str['to_uid']=to_uid
    dic_str['msg']=messges
    dic_str['r']=r
    #print dic_str
    send_str = json.dumps(dic_str)
    time.sleep(0.5)
    #print send_str
    send_message(send_str)
    print 'sent ',i+1
    
ws.close()
