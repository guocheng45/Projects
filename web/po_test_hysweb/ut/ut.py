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