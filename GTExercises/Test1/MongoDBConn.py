#coding: UTF-8
'''
mongo DBConn类
'''
#import pymongo
from pymongo import MongoClient

class DBConn:
    client=None
    #services="mongodb://192.168.1.54:30000"
    
    #连接数据库
    client =MongoClient('192.168.139.54',30000)
    #print client
    db_name= 'ktsg_record'
    db=client[db_name]   #选择数据库
    #print "当前数据库中的集合名称：",db.collection_names()
    #print "当前数据库名称：",db.name
    find_table=db['world_phones']
    collect=db.world_phones   #选择数据库中的集合
        
    #collect.find_one()        #集合中查询   
    #print "当前集合名称：",collect.name   
    #print "显示当前查询内容：",list(collect.find_one())  #显示的是当前集合中的字段
    #print "collect.find显示：",list(collect.find({"_id":"+82-0162611828"})) #显示除了被查集合的id字段的所有字段
    #print "collect.find显示：",list(collect.find())  #显示当前集合中所有的成员值
        
    #查询特定键
    #select code from world_phones where _id='+82-0162611828'
    #for code in db.world_phones.find({"_id":"+82-0162611828"},["code"]):
    #    print "这是结果:",code
    #    print "code值：",code['code']
    #    print "_id值：",code['_id']
        
    #    print "查询内容显示完毕！"
        

        
    #查询特定键code方法
    def select_code(self,phoneNum):
        phone_id=phoneNum
#        print "phone_id的值为：",phone_id
        #phone_code = None
        #phone_id="+86-15001106951"#raw_input()
        phone_code = 0
        #print DBConn.collect.find({"_id":phone_id},["code"])
        for code in DBConn.collect.find({"_id":phone_id},["code"]):
            #for循环如果数据库中查不到这个手机号会直接结束for循环，原理未知
            phone_code=code['code']
            #print "验证码是：",phone_code
        if phone_code !=0 and phone_code != '':
            print "phone_code：",phone_code
            return phone_code
        elif phone_code == 0:
            print 'database have no this phonenumber！'
            phone_code = 'phonenumber error！'
            return phone_code
        else:
            print "this phone has null code!"
            phone_code = 'null code'
            return phone_code
        
    #关闭数据库
    def close(self):
        return self.client.disconnect()
    
    def getconn(self):
        return self.client