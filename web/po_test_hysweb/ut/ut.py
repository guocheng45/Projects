def re_print1():
    for i in range(1,10):
        for j in range(i,10):
            print(i, "*", j, "=",(i*j), end=' ')        # 倒三角
        print()

def re_print2():
    for i in range(1,10):
        for j in range(1,i+1):
            print(j, "*", i, "=",(i*j), end=' ')        # 正三角
            # print('{}*{} = {}\t'.format(j, i, i * j), end="")  # 也可用
        print()

# re_print1()
# re_print2()

# list 增加元素
def list_add():
    li1 = []
    li1.append('1')
    li1.append('2')
    print(li1)
    print(li1[0])

# list_add()

# 递归
def zero(n):        # 整个程序是先一层层进去，然后在一层层出来。——意指最后一个函数是0结束了返回上层函数...
    n = n//2        # / 是除法，例如：2/3 = 0.6666。而//是表示取整的除法
    print('pr1:',n)
    if n == 0:
        return 'Done'
    zero(n)
    print('pr2:',n)

# zero(10)        # # 5 2 1 0 1 2 5

# 阶乘  n! = n * (n-1)  从1乘到n  n需大于0的整数
def factorial(n):
    if n == 1:
        return 1    # 到了等于1的时候最底层的函数就会结束，一层一层的出来
    return n * factorial(n-1)

print(factorial(9))

# 二分查找      在有序的队列里面找某个元素，先判断中间位置元素，在判断剩余元素的中间元素...