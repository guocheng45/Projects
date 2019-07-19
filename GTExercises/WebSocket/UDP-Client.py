# -*- coding: utf-8 -*- 
# import socket
# port=7000
# host='ws://testchatc1.ktplay.cn'
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.sendto(b'{"cmd":"login", "token":"", "uid":100, "r":""}',(host,port))

import sys
import json
d = {'first': 'One', 'second':2}
#dump和dumps的唯一区别是dump会生成一个类文件对象，dumps会生成字符串，同理load和loads分别解析类文件对象和字符串格式的JSON
s=json.dumps(d)   #将字典加工成json字符串
print s
s1=json.loads(s)  #额特么现在也不明白这是把他整成啥了，先不用吧！输出：{u'second': 2, u'first': u'One'}
print s1



dic_str={'cmd':'msg','type':1, 'to_uid':400279519, 'msg':'zheshishenme dongxi sa ?', 'metadata':'', 'r':1.2335}
print sys.argv #这是一个数组的嘛，然后0是python文件，后一个参数。。。
if len(sys.argv) != 3:
    print 'parameters not right'
    sys.exit()
i = int(sys.argv[2])-1
r=i
messges='hello'+str(i)
dic_str['to_uid']=int(sys.argv[1])
dic_str['msg']=messges
dic_str['r']=r
print dic_str
send_str = json.dumps(dic_str)
print send_str

#'{"cmd":"msg","type":1, "to_uid":400279519, "msg":"zheshishenme dongxi sa ?", "metadata":"", "r":1.2335}'