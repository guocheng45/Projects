# set是Python中的集合
set1={1,2,3}
set2=set1
set3=set('hello')   # 直接给集合3赋值，随机存储不重复值，如下结果
print(set3)         # {'h', 'l', 'e', 'o'}
set3.add(1)         # 给set3最后增加值
print(set1,set3)    # {1, 2, 3} {1, 'h', 'o', 'e', 'l'}
#set3.clear()        # 集合3被干掉
print(set3)         # 打印结果 set()

de =set3.pop()      # 获取和删除集合的最后一个元素
print(set3)
set3.remove('l')    # 查找并删除集合中的l,如果不存在则会KeyError
print(set3)

a= set1&set3        # 获取两个集合的交集
print(a)

b=set1|set3         # 获取两个集合的并集
print(b)