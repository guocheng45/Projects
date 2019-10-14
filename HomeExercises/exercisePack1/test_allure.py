from operator import add

import pytest
import allure
@allure.feature('测试求和功能')
class TestAllure():
    @allure.story('')

    def test_int(self):
        """
        测试用例test_int，测试目的：证书求和功能正常
        """
        with allure.step('第一步相加'):
            assert 1==2