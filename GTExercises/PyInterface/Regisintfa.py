#-*- coding: UTF-8 -*-

#————urllib库有一个很智能的毛病。data不给值，访问方式就是GET，data给了值，方式就会变成POST；
#用post方法请求api：这种方式把参数放在请求内容中传递，比较安全
import urllib,urllib2
class RegisIntfa:
    
    def CN_regist_username(self,Uname,gid):         #注意方法中要有self才能使方法作为类方法
        url = 'http://testapi.ktplay.cn:3011/2/user/account/login_by_nickname'        #接口url链接
        body={"game_id":4398,"username":'',"password":'123456'}        #接口要传的参数
        body["game_id"]=gid
        body["username"]= Uname
        body=urllib.urlencode(body)     #把参数进行编码
        request=urllib2.Request(url,body)# 用Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
        response = urllib2.urlopen(request)  # 用urlopen打开上一步返回的结果，得到请求后的响应内容
        apicontent = response.read()  #将响应内容用read()读取出来
        print(apicontent)
        ret =apicontent.find('username')  #位置从0开始算，如果没找到则返回-1。
        print(ret)
        return ret
#     if ret >=0:
#         return ret
#     else:
#         return 
    def EN_regist_username(self,Uname,gid):
        url = 'http://testapi.ktplay.com:4011/2/user/account/login_by_nickname'        #接口url链接
        body={"game_id":4401,"username":'',"password":'123456'}        #接口要传的参数
        body["game_id"]=gid
        body["username"]=Uname
        body=urllib.urlencode(body)     #把参数进行编码
        request=urllib2.Request(url,body)# 用Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
        response = urllib2.urlopen(request)  # 用urlopen打开上一步返回的结果，得到请求后的响应内容
        apicontent = response.read()  #将响应内容用read()读取出来
        print(apicontent)
        ret =apicontent.find('username')  #位置从0开始算，如果每找到则返回-1。
        print(ret)
        return ret

#     names = 'gzc1'
#     CN_regist_username(names,4398) 
    
   



