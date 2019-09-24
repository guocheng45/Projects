# 关于字符串的操作
str = 'python 蟒蛇'
print(dir(str))

print(type(str))

print(str.count("l"))   #搜索里面的l的数量 count
print(str.find("o"))    #查找字符串中o的位置
print(str.capitalize()) #首字母变大写
print(str.encode("gb2312")) #编码格式

print(str[0:-1])        # 输出第一个到倒数第二个的所有字符（-1代表最后一个，左闭右开）
print(str[0])           # 输出字符串第一个字符
print(str[2:5])         # 输出第三到第五个字符  右开，所以没有第六个字符
print(str[2:])          # 输出从第三个开始的后的所有字符
print(str*2)            # 输出字符串两次
print(str+"zhazha")     # 连接字符串

print(len(str))         # 字符串的长度

