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
# 下面一行的注解：预留一个空的字符串'',.join方法后续拼接，  快速生成多个随机数的方法（x for i in range(8)）x非i 所以只是沿用了x的展示次数
rad_str=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)for i in range(8))
print(rad_str+'@163.com')