# coding: UTF-8
# counter = 1
# def adds():
#     global counter
#     for i in (1,2,3):
#         counter +=1
# adds()
# print counter


# 加r和不加''r是有区别的
# 'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子
# 在字符串赋值的时候 前面加'r'可以防止字符串在时候的时候不被转义 原理是在转义字符前加'\'
# print r'\tt'
# Output:'\tt'
# 
# print '\tt'
# Output:'t' 

# import math
# 
# print math.floor(5.6)

a = []
def fun(a):
    a.append(1)
fun(a)
print a

