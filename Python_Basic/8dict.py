# 对字典的操作，字典与json格式近似，常用
ages = {
    'linda': 18,
    'leimeng': 51,
    'yujian': 31
}
print(ages.get("linda",88))     # 获取linda的值，如果字典中有linda显示字典中的值，如果没有，则显示88
ages["dalu"]=33         # 连赋值带增加字段
ages["yujian"]=55       # 给存在的参数赋值
print(ages)
del ages['leimeng']     # 删除指定字段
print(ages)

# key in dict
D = {'username': 'linda', 'age': 12, 'salary': 10000000}
print("循环出来key,再通过key可能输入值")
for key in D:
    print(key,'=>',D[key])

print("只循环出值")
for value in D.values():
    print(value)

print("同时循环出key与value，断言返回key的值与。。。通常用在接口测试中的json的响应断言")
for key,value in D.items():
    print(key,':',value)
    assert D[key]==value