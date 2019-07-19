# -*- coding: UTF-8 -*-

#————urllib库有一个很智能的毛病。data不给值，访问方式就是GET，data给了值，方式就会变成POST；
#用post方法请求api：这种方式把参数放在请求内容中传递，比较安全
import urllib,urllib2
from hashlib import md5
def return_user_token(username):
    url = 'http://testapi.ktplay.cn:3011/2/user/account/login_by_nickname'        #接口url链接
    body={"game_id":4398,"username":'',"password":'qqqqqq'}        #接口要传的参数
    body["username"]=username
    #print body
    body = urllib.urlencode(body)
    request = urllib2.Request(url,body)
    response = urllib2.urlopen(request)
    apicontent = response.read()
    flag = apicontent.split('"')[-4]     #获取字符串倒数第二个“和倒数第一个“之间的字符
    if flag == 'user_token':
        user_token = apicontent.split('"')[-2]     #此乃user_token
        print(user_token)
        return user_token
    else:
        return False

#print 'SS:',ss
# s= 'qwertyuiop'
# print s.find('u')
# print len(s)
def ret_md5(str):
    m = md5()
    m.update(str)
    return m.hexdigest()
sign = ret_md5('yoping.cn'+str(4398))
def submit_score(user_token,scores):
    url = 'http://testapi.ktplay.cn:3011/2/leaderboard/score/submit'        #接口url链接
    body={"game_id":4398,"user_token":'',"leaderboard_id":'liang1',"scores":'12',"sign":''}        #接口要传的参数
    body["user_token"]=user_token
    body["scores"]=scores
    body["sign"]=sign
    #print body
    body = urllib.urlencode(body)
    request = urllib2.Request(url,body)
    response = urllib2.urlopen(request)
    apicontent = response.read()
    print('apicontent:', apicontent)
    returns = apicontent.split('"')[1]
    #print 'returns:',returns
    if returns=='game_id':
        print('success!' + scores)
        return True
    else:
        print('failed!')
        return False
# user_token = return_user_token('gzc1')
# scores = '11'
# submit_score(user_token, scores)
for i in range(1,301):
    user_name = 'gtest'+str(i)
    user_token = return_user_token(user_name)
    scores = str(i)
    res = submit_score(user_token, scores)
    if res ==True:
        i=i+1
    else:
        break
    

# url = 'http://testapi.ktplay.cn:3011/2/leaderboard/score/submit'        #接口url链接
# body={"game_id":4398,"user_token":'',"leaderboard_id":'qwe123',"scores":'12',"sign":''}        #接口要传的参数
# body["user_token"]=user_token
# body["sign"]=sign
# body = urllib.urlencode(body)
# request = urllib2.Request(url,body)
# response = urllib2.urlopen(request)
# apicontent = response.read()
# print 'apicontent:',apicontent

# url = 'http://testapi.ktplay.cn:3011/2/leaderboard/score/submit'        #接口url链接
# body={"game_id":4398,"user_token":'',"leaderboard_id":'qwe123',"scores":0}        #接口要传的参数
# body["username"]='adasda'
# print body
# body=urllib.urlencode(body)     #把参数进行编码
#     
# request=urllib2.Request(url,body)# 用Request来发送POST请求，指明请求目标是之前定义过的url，请求内容放在data里
#     
# response = urllib2.urlopen(request)  # 用urlopen打开上一步返回的结果，得到请求后的响应内容
#     
# apicontent = response.read()  #将响应内容用read()读取出来
#     
# print  apicontent  #打印读取到的内容