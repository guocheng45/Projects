# 列表：以中括号开头结尾，数据通过逗号隔开，使用引号
book=["python","java","appium","seleium"]
print(book)         # 打印整个列表
print(book[1])      # 打印列表第二个元素
print(len(book))    # 打印列表的长度
book.append("today history")        # 在列表最后追加
book.append("tomorrow history")     # 同上
print(book)

print(book.pop(2))        # 获取并删除第三个参数
book.insert(2,"furture history")    # 在第三个位置插值
book.extend(book)         # 列表最后追加一个列表
book.remove("tomorrow history")     # 列表中删除指定值
book.pop()          # 获取并移除列表最后一个
print(book)
print("索引位置：",book.index('java'))      # 从列表中找出某个值第一个匹配项的索引位置

print(book.copy()*4+book)       # book copy4次再加一次
print(book.copy().clear())      # 删除了book的全部copy
print(book)                     # book仍然存在

# list 字符拼接
l2 = ['a','dd','s','df']
print(''.join(l2))      # addsdf   注意list中是int类型则不可以拼接

book = ['Google', 'testerhome', 'testing-studio', 'Baidu']
book.reverse()                  # 列表倒序
print("列表翻转后：",book)
book.sort()                     # 列表正序
print("列表排序后：",book)

ids = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
print(list(set(ids)))       # 去重,捎带正序排序
print(list({}.fromkeys(ids).keys()))        # 保持原顺序
ids = list(set(ids))  # list去重,捎带正序排序
print(ids)
ids.sort()  # 正序排序
print(ids)
ids.reverse()   # 倒序排序
