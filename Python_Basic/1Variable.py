
my_int = 10

my_str = "I'm love Python"          # 字符串 ，单引，双引，三引号都行，三引号不赋值算注释

my_tuple = ("python", 33, 8.3, 8.8)     # 元组，固定长度不能变

my_list = ["python", 12, 2.3, 9.7, 12]      # 列表，可变长度，有序

my_dict = {'name': 'linda', 'age': 88}      # 字典，无顺序，按key-value方式存储

# 一行可以写多个语句，用;分开就行

my_set = {1, 2, 3}; print(dir(my_set))      # 集合，元素无重复

my_bool = True

a = b = c = 1           # 一个值给多个变量赋值

a, b, c = 1, 2, "linda"         # 同时多个值赋值给多个变量

# a1 = str(a)     # 强制转换从int到str
# print(type(a1))
# print(type(int(a1)))        # str 转 int
# print(tuple(my_list))       # list与tuple元组转换
# print(list(my_tuple))
# print(set(my_list1))        # 列表转成set变成不重复的
# print(set(my_dict))         # 字典类型转成set只有key值
# print(list(my_dict.values()))       # 字典转成列表，key,value可以单转
# print(list(my_dict))
# my_tuple1 = ('one', 1), ('two', 2), ('three', 3)
# my_list_tuple = [('one', 1), ('two', 2), ('three', 3)]
# # print(my_tuple1)
# print(type(my_list_tuple))
# print(dict(my_list_tuple))

# 将对象 x 转换字符串

b = {"name": "linda", "age": 18}
str_b = repr(b)
print(str_b[0:10])