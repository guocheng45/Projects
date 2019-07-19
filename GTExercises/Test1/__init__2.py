#coding: UTF-8
#运算符重载
'''
class Vector:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2
'''
# class Life:  
#     #构造函数 
#     def __init__(self, name='name'):   
#         print 'Hello', name   
#         self.name = name 
#     #析构方法  
#     def __del__(self):   
#         print 'Goodby', self.name   
#   
# brain = Life('Brain') #call __init__   
# 
# test_list = [1,3,4,'Hongten',3,6,23,'hello',2]
# for i in range(1,len(test_list)):
#     #print len(test_list)
#     print i
#     print test_list[i],','
#     #print(test_list[i],end=',')
# 
# print()   
# print('#####################################')

# a = [11,22,33,44,11,22]  
# b = set(a)  
# print b
# c = [i for i in b]  
# print c

# nums = set([1,1,2,3,3,4])
# print nums
# print len(nums)

# for i in range(2):
#     print i
# for i in range(3,5):
#     print i

# import math
# print math.floor(5.5)#Return a float is the largest integral value <= x.

class Person:
    def __init__(self):
        pass
    def getAge(self):
        print __name__
p =Person()
p.getAge()