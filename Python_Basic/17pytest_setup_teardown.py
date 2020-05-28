# 1.setup_function、teardown_function 2.setup_class、teardown_class 3.setup_method、teardown_method 4.setup_module、teardown_module

import pytest

def setup_module():
    print("setup_module():在模块最之前执行\n")

def teardown_module():
    print("teardown_module：在模块之后执行")

# 函数级的（setup_function、teardown_function）只对函数用例生效，而且不在类中使用
def setup_function():
    print("setup_function():每个方法之前执行")

def teardown_function():
    print("teardown_function():每个方法之后执行")

def test_01():
    print("正在执行test1")
    x="this"
    assert 'h' in x

def test_02():
    print("正在执行test2")
    x="hello"
    assert hasattr(x,"hello")       # 这是啥意思？？？

def add(a,b):
    return a+b

def test_add():
    print("正在执行test_add()")
    assert add(3,4)==7

if __name__ == '__main__':
    pytest.main("-s","17pytest_setup_teardown.py")      # -s为了显示用例的打印信息   -q只显示结果不显示过程


# 类中方法级的类前类后，方法前方法后执行

class TestMethod(object):

    def setup_class(self):
        print("\n setup_class(self)：每个类之前执行一次\n")

    def teardown_class(self):
        print("teardown_class(self)：每个类之后执行一次")

    def setup_method(self):
        print("setup_method(self):在每个方法之前执行")

    def teardown_method(self):
        print("teardown_method(self):在每个方法之后执行\n")

    def add(self,a,b):
        print("加减法")
        return a+b

    def test_01(self):
        print("正在执行test1")
        x="this"
        assert "h" in x

    def test_02(self):
        print("正在执行test2")
        assert self.add(3,4)==7