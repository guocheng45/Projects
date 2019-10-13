#用于设置那个用例先跑

import time
import pytest

value =0

@pytest.mark.run(order=2)
def test_add1():
    print("第一个方法")
    time.sleep(2)
    assert value==10

@pytest.mark.run(order=1)
def test_add2():
    print("第二个方法")
    time.sleep(2)
    global value        # 一定注意这个global 不然赋值的不是全局变量
    value=10
    assert value ==10