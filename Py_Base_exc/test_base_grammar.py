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

    def test_foo(self):
        self.foo(1, (5, 6, 7, 8), {"y": 2, "z": 3})
        self.foo(1, *(5, 6, 7, 8), **{"y": 2, "z": 3}, a=6)     # 此为正确用法
        # .== == == == == == == == == == == == == == == == == == == =
        # < Py_Base_exc.test_base_grammar.Test_Base_grammar
        # object
        # at
        # 0x00000000036918D0 >
        # (1, (5, 6, 7, 8), {'y': 2, 'z': 3})
        # 4
        # {}
        # == == == == == == == == == == == == == == == == == == == =
        # == == == == == == == == == == == == == == == == == == == =
        # < Py_Base_exc.test_base_grammar.Test_Base_grammar
        # object
        # at
        # 0x00000000036918D0 >
        # (1, 5, 6, 7, 8)
        # 6
        # {'y': 2, 'z': 3}
        # == == == == == == == == == == == == == == == == == == == =

