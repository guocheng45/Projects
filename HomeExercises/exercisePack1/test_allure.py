from operator import add

import pytest
import allure
@allure.feature('测试求和功能')       # 每个大的功能模块可以定义为一个feature
class TestAllure():
    @allure.story('测试整数的求和功能')      # 大功能下的一个子功能

    @allure.issue("http://192.168.1.1:8080/mantis")     # 缺陷提交到管理系统上
    @allure.testcase("http://192.168.1.1:8080/testlink")        # 指定用例的url
    @allure.severity('minor')       # 测试用例的优先级
    def test_int(self):
        """
        测试用例test_int，测试目的：证书求和功能正常
        """
        with allure.step('第一步相加'):      # 每个步骤就是一个step
            assert 2==2
        with allure.step('第二步'):      # 每个步骤就是一个step
            assert 2==3
        with allure.step('第三步'):      # 每个步骤就是一个step
            assert 4==5

    @allure.story('测试小数的求和功能')      # 大功能下的一个子功能
    @allure.issue("http://192.168.1.1:8080/mantis")     # 缺陷提交到管理系统上
    @allure.testcase("http://192.168.1.1:8080/testlink")        # 指定用例的url
    @allure.severity('minor')       # 测试用例的优先级
    def test_float(self):
        """
        测试用例test_float，测试目的：小数求和功能正常
        """
        assert 4.3==4.7
        file=open('./test.png','rb').read()
        allure.attach('test_img',file,allure.attachment_type.PNG)       # 增加附加信息图片