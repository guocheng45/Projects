import pytest

class Test_Base_grammar():

    def test_value_exist(self):
        #1、查找列表中某个值是否在列表中
        a= 'f'
        b= ['a','b','c','d']
        i=len(b)
        print (i)
        for c in b:
            if a==c:
                print("find it!")
                break
            elif i>1:
                print("go on")
            else:
                print("not exist!")
            i=i-1

    def test_jump_letter(self):
        #2、跳过某个字母不输出
        for letter in 'python':
            if letter=='h':
                continue
            print("当前字母：",letter)

    #while 循环 将偶数与奇数分开
    def test_while_split(self):
        l1=[12, 37, 5, 42, 8, 3]
        even=[]
        odd=[]
        #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        while len(l1)>0:
            i=l1.pop()
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        print('even:',even,'odd:',odd)
        return even,odd

    #4、把key循环出来?????
    def test_cyc_key(self):
        D=[213,123,34,5,54]
        for key in D:
            print(key,'=>',D[key])
        for value in D.values():
            print(value)
        for key, value in D.items():
            print(key, ':', value)
            assert D[key] == value
        return D

    def foo(x,*args,a=4,**kwargs):   #使用默认参数时，注意默认参数的位置要在args之后kwargs之前
        print("=======================================")
        print(x)
        print(args)
        print(a)
        print(kwargs)
        print("=======================================")
    #方法参数的使用
    def test_foo(self):
        self.foo(1, (5, 6, 7, 8), {"y": 2, "z": 3})
        self.foo(1, *(5, 6, 7, 8), **{"y": 2, "z": 3}, a=6)     # 此为正确用法
        # .== == == == == == == == == == == == == == == == == == == =
        # < Python_Basic.test_base_grammar.Test_Base_grammar
        # object
        # at
        # 0x00000000036918D0 >
        # (1, (5, 6, 7, 8), {'y': 2, 'z': 3})
        # 4
        # {}
        # == == == == == == == == == == == == == == == == == == == =
        # == == == == == == == == == == == == == == == == == == == =
        # < Python_Basic.test_base_grammar.Test_Base_grammar
        # object
        # at
        # 0x00000000036918D0 >
        # (1, 5, 6, 7, 8)
        # 6
        # {'y': 2, 'z': 3}
        # == == == == == == == == == == == == == == == == == == == =

    #多变量一起赋值
    def test_assign(self):
        a, b, c = 1, 2, "linda"
        print(a, b, c)
        return a,b,c

    #python变量直接交换值，牛逼
    def test_exchange(self):
        x,y=1,2
        x,y=y,x
        print(x,y)
        return x,y

    # 组合两个列表
    def test_combina_list(self):
        a=[1,2,3,4]
        b=[5,6,7,8]
        for a,b in zip(a,b):
            print(a,b)
        return a,b


    def test_moreinput(self):
        # 输入多个相同的只需要乘法          结果：.abcabcabcabc
        str='abc'
        print(str*4)

        # 简洁写法：10以内偶数
        li = [x for x in range(10) if x % 2 == 0]

        # 反转list列表
        lists=[1,2,3,4,5,6]
        print(list(reversed(lists)))

        # 列表排序
        lists=[6,5,4,3,2,1]
        print(list(sorted(lists)))

        # 列表元素出现的次数
        from collections import Counter
        lists=[2,4,6,7,8,5,3,2,1,3,6]
        my_couter=Counter(lists)
        print(my_couter.most_common())

        # 快速添加数据小技巧
        ls = [1, 2, 3, 4]
        list1 = [i for i in ls if i > 2]
        print('list1:',list1)
        tuple1 = (2, 4, 6)
        dict1 = {x: x ** 2 for x in tuple1}
        print('dict1:', dict1)
        # dict2 = {x: 'item' + str(x ** 2) for x in tuple1}
        # print('dict2:', dict2)
        set1 = {x for x in 'hello world' if x not in 'low level'}
        print('set1:', set1)

        return 1