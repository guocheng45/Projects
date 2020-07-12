# coding=utf-8
# import time
# import os
#
# # 生成测试报告的名字是根据当前的时间和文件名全名的
# report_time=time.strftime('%Y%m%d%H%M%S',time.localtime())
# print(report_time+os.path.basename(__file__))       # 2019092614523713random.py

import random
import string

# 将序列中的某个随机取出来做为测试数据。序列可以是列表，字符串等
course=['python','java','appium','selenium']
random_couse=random.choice(course)
print(random_couse)

# 大写小写字母和数字随机拼接为测试数据
# 下面一行的注解：预留一个空的字符串'',.join方法后续拼接，  快速生成多个随机数的方法（x for i in range(8)）\
# x非i 所以只是沿用了x的展示次数
rad_str=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for i in range(8))
print(rad_str+'@163.com')

def use_random():
    import random
    print(random.randint(1,10))                 # 生成一个1-10的随机数，概率一样
    print(random.random())                      # 生成一个0-1的浮点数
    print(random.choice([1,3,5,6,7,9]))         # 从序列中随机取出一个数，概率一样
    print(random.choice(['剪刀','石头','布']))   # 随机取字符，概率一样
    ou = random.randrange(0,100,2)
    print(ou)                                   # 随机获取0-100间的偶数，概率一样
    ji = random.randrange(0, 100, 2)-1
    print(ji)        # 随机获取0-100的奇数，概率一样
    print(random.choice('adadhasdhkahfkhfk'))   # 获取随机字符
    print(random.sample('dadsahdkahdusiwyiyriwyr',5))       # 随机生成指定数量的字符——输出：['a', 'y', 'a', 'i', 'r']
    print(''.join(random.sample('dadsahdkahdusiwyiyriwyr', 5)))       # 随机生成指定数量的字符，并拼接成一个字符串，\
    # 输出：ikwyy

    print(random.sample('abcde', 5))        # 随机获取5个不同的随机值
    print(random.sample(range(100), 10))    # 在0-100中随机获取10个不同的数

    a = [1, 3, 5, 6, 7]  # 将序列a中的元素顺序打乱
    random.shuffle(a)
    print(a)

use_random()