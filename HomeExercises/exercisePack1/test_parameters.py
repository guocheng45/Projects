#目的是减少测试用例的条数

import pytest

@pytest.mark.parametrize("x,y",[
    (3+5,9),
    (2+4,6),
    (6*9,42),
    ("testerhome","testerhome")
])
def test_add(x,y):
    assert x==y