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
print(str.startswith("python"))     # 判断是否以XX开头，是返回true，不是返回false
b="20"
print(b.isdecimal())        # 字符串是否只包含十进制字符返回True，否则返回False
print(str.upper())          # 它的大写
print(str.title())          # 返回"标题化"的字符串,就是说所有单词都是以大写开始

str0 = 'python 蟒蛇'
print(str0.replace(str0[0:6],"java".upper()))       # 替换str0[0:6] 从0开始6结束不包括6
print(str0.replace('python','java'))                # 替换old为new

# s1 = "-"
# s2 = ""
# seq = ("l", "i", "n", "d", "a") # 字符串序列
# print(s1.join(seq))     # 替换中间的 输出 l-i-n-d-a
# print(s2.join(seq))
#
# str4 = "编号 标题 测试数据 测试结果"
# no,title,test_data,test_result=str4.split(" ")   # 拆分数据
# print(test_result)
#
# #格式输出
# print("Hi,%s,you hava $%d." %('linda',100000))
#
# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))  # 保留小数点后1位
# print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
#
# # print中%s的用法
# string = "good"  #类型为字符串
# print("string=%s" %string)   #输出的打印结果为 string=good