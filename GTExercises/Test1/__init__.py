#coding: UTF-8

#这一行必须放在源码首行否则写了中文就报错
#!/user/bin/python
import os
'''
name =raw_input('ewqeqweqwewqe')
if name.endswith('123'):
    print'654321'
elif name.endswith('111'):
    print '123456'
else:
    print'456345'
'''
'''
def hello(he):
    return 'hello,%s'%he

if __name__=='__main__':
    print 'what is you name?'
    he =raw_input("my name is:")
    so_i_say =hello(he)
    print so_i_say;
'''
'''
print 'hello world'
print "hello world"

print 1+3

print 2**3
'''
'''
print 'what is you name?'
name=raw_input("my name is:")
print "Hello,"+name
#治疗窗口闪现问题
raw_input("press any key to exit")
'''
"hello world"
#获取网址的域名
'''
url =raw_input('enter the URL:')
domain =url[11:-4]
print 'the domain is '+domain
'''
'''
g1=[1,3,5,7,9]
g1[1:2]=[]
print g1 #只是开始的干掉了，结束的留下了
'''
'''
pi=3.1415926
print '%-10f'%pi    #左对齐，字段宽10，浮点型
print'**********'
print '%10f'%pi     #非左对齐，字段宽10，浮点型
print'**********'
print '%-10.2f'%pi  #左对齐，字段宽10，精确小数点后2位，浮点型

seq=[1,2,3,4,5]
sep='+'
seq.join(sep)
print seq
print sep
'''
'''
#字典使用
names=['Ali','Beti','cale','Luozi']
numbers=['1234','2345','4567','5678']
print numbers[names.index('Luozi')]

print 'age:',42

#赋值方法
values=1,2,3
x,y,z=values
print x,y,z,values

#断言使用
age=2
assert 0<age<100,'The age must be realistic'

age=raw_input('input your name:')
if 0<age and age<100:
    print 'you have '+age+'years old'
else:
   assert 0<age<100,'The age must be realistic' 

#异常处理实例
def temp_convert(var):
    try:
        return int(var)
    except ValueError,Argument:
        print "The argument does not contain numbers\n",Argument
temp_convert("xyz")

#循环语句使用
#while的使用
i=1
while i<=100:
    print i
    i=i+1
#for的使用
'''
words=['this','is','an','ex','parrot']
for word in words:
    print word
'''
1231
#确保用户输入姓名
name=''
while not name or name.isspace():
    name=raw_input('Please enter your name:')
print 'Hello %s'%name
'''
'''
# 打开一个文件
fo = open("foo.txt", "wb")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace  #一般程序员用不到，暂时忽略。
fo.close()
print "是否已关闭",fo.closed
print "文件名：",fo.name
fo=open("foo.txt","r+")  #r+打开文件用于读写，位置定在文件的开头
fo.write( "www.runoob.com!\nVery good site!\n")
fo=open("foo.txt","r+")
str1=fo.read(10)
position=fo.tell()
print "现在位置在：",position
print "读取的字符串是：",str1
str1=fo.read(10)
print "现在读取的字符串是：",str1
fo.seek(0,0)#指针被定回文件开头seek（偏移量，偏移起始位置）
str1=fo.read(10)
print "现在读取的是：",str1
fo.close()


str=os.rename("test2.txt", "test1.txt")
print str   #不返回None
'''
#os.mkdir(path)
# os.chdir("C:\Users\KTplay\Downloads")
# fo=open("new1.txt","r+")
# fo.write("woshi")
# fo=open("new1.txt","r+")
# str1=fo.read(10)
# print str1
# os.chdir("C:\Users\KTplay\Downloads")
# str2=os.getcwd()
# print str2
# os.rmdir("newpack")#这个目录必须是空的，且存在





