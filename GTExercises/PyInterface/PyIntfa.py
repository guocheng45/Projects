# -*- coding: UTF-8 -*-

#————urllib库有一个很智能的毛病。data不给值，访问方式就是GET，data给了值，方式就会变成POST；
#用post方法请求api：这种方式把参数放在请求内容中传递，比较安全
import urllib,urllib2
   
url = 'http://testapi.ktplay.cn:3011/2/user/account/login_by_nickname'        #接口url链接
body={"game_id":4398,"username":'gzc1',"password":'123456'}        #接口要传的参数
body=urllib.urlencode(body)     #把参数进行编码
    
request=urllib2.Request(url,body)# 用Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
    
response = urllib2.urlopen(request)  # 用urlopen打开上一步返回的结果，得到请求后的响应内容
    
apicontent = response.read()  #将响应内容用read()读取出来
    
print  apicontent  #打印读取到的内容
#....................................
#import urllib2
#url_save = 'ws://210.12.123.69:7000'
#body = {'uid':'','token':''}
#try:
#    s_save = urllib2.urlopen(url_save).read()
#    print s_save  
#except urllib2.HTTPError, e:
#    print e.code
#except urllib2.URLError, e:
#    print str(e)
#import websocket
#ws=websocket.WebSocket()
#ws.connect("ws://111.207.130.132:7000/",http_proxy_host="111.207.130.132",http_proxy_port=7000,header=["User-Agent: MyProgram","x-custom: header"])
#result =  ws.recv()
#print "Received '%s'" % result

# from websocket import create_connection
# ws = create_connection("ws://echo.websocket.org/")
# print "Sending 'Hello, World'..."
# ws.send("Hello, World")
# print "Sent"
# print "Reeiving..."
# result =  ws.recv()
# print "Received '%s'" % result
# ws.close()
# 
# 
# ws = create_connection("ws://111.207.130.132:7000/")
# print "Sending login request"
# ws.send("Hello, World")
# print "Sent"
# print "Reeiving..."
# result =  ws.recv()
# print "Received '%s'" % result
# ws.close()