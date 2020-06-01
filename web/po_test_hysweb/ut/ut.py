

def re_print1():
    for i in range(1, 10):
        for j in range(i, 10):
            print(i, "*", j, "=", (i * j), end=' ')  # 倒三角
        print()


def re_print2():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, "*", i, "=", (i * j), end=' ')  # 正三角
            # print('{}*{} = {}\t'.format(j, i, i * j), end="")  # 也可用
        print()


# re_print1()
# re_print2()

# list 增加元素
def list_add():
    li1 = []
    li1.append('1')
    li1.append('2')
    li1.remove('2')
    print(li1)
    print(li1[0])


# list_add()

# 递归
def zero(n):  # 整个程序是先一层层进去，然后在一层层出来。——意指最后一个函数是0结束了返回上层函数...
    n = n // 2  # / 是除法，例如：2/3 = 0.6666。而//是表示取整的除法
    print('pr1:', n)
    if n == 0:
        return 'Done'
    zero(n)
    print('pr2:', n)


# zero(10)        # # 5 2 1 0 1 2 5

# 阶乘  n! = n * (n-1)  从1乘到n  n需大于0的整数
def factorial(n):
    if n == 1:
        return 1  # 到了等于1的时候最底层的函数就会结束，一层一层的出来
    return n * factorial(n - 1)


# print(factorial(9))

# 二分查找      在有序的队列里面找某个元素，先判断中间位置元素，在判断剩余元素的中间元素...
data1 = list(range(100))
# print("data1:", data1)

def b_search(num, low, high, data):
    mid = int((low + high) / 2)
    # if low == high:
    #     print("can not find it")
    #     return
    if data[mid] > num:
        print(data[mid], "bigger than num")
        return b_search(num, low, mid - 1, data)
    elif data[mid] < num:
        print(data[mid], "lower than num")
        return b_search(num, mid + 1, high, data)
    elif data[mid] == num:
        print("find it", data[mid])
    else:
        print("can not find it")
        return -1


# b_search(99,0,len(data1),data1)

# 冒泡排序
def bubble_sort():
    nums = [6, 5, 4, 3, 2, 1]
    print("===========:", len(nums))
    for i in range(len(nums) - 1):  # 从0 开始到len-1结束不包括len-1,共计len-1次
        for j in range(len(nums) - 1 - i):  # 每次循环都从0开始到len-1-i结束
            if nums[j] > nums[j + 1]:
                nums[j + 1] = nums[j] + nums[j + 1]
                nums[j] = nums[j + 1] - nums[j]
                nums[j + 1] = nums[j + 1] - nums[j]

    print("==========nums:", nums)

# bubble_sort()
#判断字符串是否对称，字符串如：“abcdedcba”
def is_sym():
    list1 = "abcddcba"
    list_len = len(list1)
    if list_len%2 !=0:
        print("不对称!")
    else:
        ranges = int(len(list1)/2)      # 4
        print("ranges:", ranges)
        for i in range(ranges):
            print(i)
            if list1[i] != list1[list_len-1-i] :
                print('不对称！')
                break
            elif list1[i] == list1[list_len-1-i] and i == ranges-1 :
                print("字符串对称！", "list1[i]=", list1[i], "list1[list_len-1-i]=", list1[list_len - 1 - i])


class baseClass:
    def test1(self, num):
        print(num)


class sonClass(baseClass):
    def test2(self,num):
        super().test1(num)     #super还是引用的父类，除非重写才是覆盖父类
        print(num+1)
    def test1(self, num):
        print(num+1)


# son = sonClass()
# son.test1(11)
# son.test2(123)

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))      # next相当于下一步

# l= [1,2,3,4]
# print(l[2:])
#
# s=''
# for i in l:
#     s+=str(i)
# print(s)

def tes_tuple():
    tuple1 = ('龙猫','泰迪','叮当猫')
    tuple1 = tuple1[:2]+('小猪佩奇',)+tuple1[2:]        #注意[:2]取前2   [2:]舍弃前2
    print("tuple1:",tuple1)

    tuple1 = ('龙猫','泰迪','小猪佩奇','叮当猫')
    tuple1 = tuple1[:2]+tuple1[3:]          #注意[:2]取前2   [3:]舍弃前3
    print("tuple2:",tuple1)

# a=tes_tuple()

l = [2,1,2,3,4,5,6,6,5,4,3,2,1]
print(list(set(l)))
print(list({}.fromkeys(l).keys()))

### 海量数据找前几的数     如： 使用生成器生成1000万个随机整数，求最大的1000个数
import random
import time

num= 1000*10000
print(num)
def gen_num(n):
    for i in range(n):
        yield random.randint(0,n)
# l = gen_num(num)
# start_time = time.time()
# l = list(set(l))
# result = l[-1000:]
# dura_time = time.time()-start_time
# print("消耗时间：",dura_time ,"\n",result)   # 耗时37.52秒   很耗内存
#
# import heapq
# start_time = time.time()
# result = heapq.nlargest(1000,l)
# dura_time = time.time()-start_time
# print("消耗时间：",dura_time ,"\n",result)   # 耗时22.05秒   比上面的少了15秒

### 两数之和     l=[1,2,3,4,5,6,7,8] 数据不重复，target=6，快速找出数组中两个元素之和等于target 的数组下标。
list1 = [1,2,3,4,5,6,7,8]
target = 6
# for a in list1:
#     if a >=6:
#         break
#     b = target - a
#     print("运行了几次？")
#     if a < b < target and b in list1:              # 可以直接作为一个判断，     b in setl
#         print("%s + %s = %s" % (a,b,target))      # print("a=%s, b=%s, c = %s" %(a,b,c))
#         print("a 的位置：%s \n b的位置：%s" % (list1.index(a),list1.index(b)))

def foo(x, *args, a=4, **kwarg): #使用默认参数时，注意默认参数的位置要在args之后kwargs之前
    print(x)
    print(a)
    print(args)
    print(kwarg)
print('=====================================')
foo(1, *(5, 6, 7, 8),**{"y": 2, "z": 3})            # 使用时，最好前加* 或**便于程序识别那个是那个
foo(1, *(5, 6, 7, 8), **{"y": 2, "z": 3}, a=6)
foo(1,*(2,3,4),a=5,**{"y":2,"z":3})