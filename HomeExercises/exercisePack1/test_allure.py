
'''
import pytest
import allure
@allure.feature('测试求和功能')       # 每个大的功能模块可以定义为一个feature
class TestAllure:
    @allure.story('测试整数的求和功能')      # 大功能下的一个子功能
    # @allure.issue("http://192.168.1.1:8080/mantis")     # 缺陷提交到管理系统上
    # @allure.testcase("http://192.168.1.1:8080/testlink")        # 指定用例的url
    @allure.severity('minor')       # 测试用例的优先级
    def test_int(self):
        """
        测试用例test_int，测试目的：证书求和功能正常
        """
        with allure.step('第一步相加'):      # 每个步骤就是一个step
            assert 2==2
        with allure.step('第二步'):      # 每个步骤就是一个step
            assert 3==3
        with allure.step('第三步'):      # 每个步骤就是一个step
            assert 5==5

    @allure.story('测试小数的求和功能')      # 大功能下的一个子功能
    # @allure.issue("http://192.168.1.1:8080/mantis")     # 缺陷提交到管理系统上
    # @allure.testcase("http://192.168.1.1:8080/testlink")        # 指定用例的url
    @allure.severity('minor')       # 测试用例的优先级
    def test_float(self):
        """
        测试用例test_float，测试目的：小数求和功能正常
        """
        assert 4.7==4.7
        # file=open('./test.png','rb').read()
        # allure.attach('test_img',file,allure.attachment_type.PNG)       # 增加附加信息图片


# if __name__ == '__main__':
#     pytest.mian('-s TestAllure')


import allure
import pytest


@allure.feature('这里是一级标签')
class TestAllure():

    @allure.title("用例标题0")
    @allure.description("这里是对test_0用例的一些详细说明")
    @allure.story("这里是第一个二级标签")
    def test_0(self):
        pass

    @allure.title("用例标题1")
    @allure.story("这里是第一个二级标签")
    def test_1(self):
        pass

    @allure.title("用例标题2")
    @allure.story("这里是第二个二级标签")
    def test_2(self):
        pass

@allure.title("用例标题0")
@allure.description("这里是对test_0用例的一些详细说明")
@allure.story("这里是第一个二级标签")
def test_0():
    pass


@allure.title("用例标题1")
@allure.story("这里是第一个二级标签")
def test_1():
    pass


@allure.title("用例标题2")
@allure.story("这里是第二个二级标签")
def test_2():
    pass
'''

import allure
import pytest
@allure.feature("测试Dome")
class TestDome(object):

    @allure.step("定义被测函数")
    def func(self, x):
        return x+1

    @allure.story("被测场景")
    @allure.severity("blocker")
    @allure.step("断言结果")
    def test_func(self):
        # with allure.MASTER_HELPER.step("断言结果"):
        allure.attach("预期结果", "{}".format(self.func(3)))
        allure.attach("实际结果", "{}".format(5))
        assert self.func(3) == 5

