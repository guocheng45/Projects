# coding=utf-8
from po_test_hysapp.pages.HysAPP import HysApp
import pytest
import allure
import time


@allure.feature("测试APP搜索页")
class TestSearch(object):

    @classmethod
    def setup_class(cls):  # 类执行一下，如启动APP
        cls.mainPage = HysApp.main()  # 可能有问题-没问题
        # cls.profile = HysApp.main().gotoProfile()   # 也可以如此写

    def setup_method(self):  # 设置等于自己的mainPage，可以直接调用？
        # self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP           可能搞错了
        self.SearchPage = self.mainPage.gotoSearchpage()    # 不同的页面的测试不要放在一个页面，初始化的时候会乱点其他页面
        pass

    def teardown_method(self):
        # 如返回至初始页可放置在此
        self.SearchPage.search_back()
        pass

    @classmethod
    def teardown_class(cls):
        # time.sleep(2)
        pass

    # 炒个栗子
    # def test_placeorder1(self):
    #     # 如要判断就加上断言
    #     assert self.mainPage.gotoHyspage().place_order_B2CBuyNow()
    #     assert "something" in self.mainPage.gotoProfile().getErrorMsg()
    # 下一步
    # 再一个assert

    @allure.story("测试B2C搜索")
    @allure.severity('Trivial')  # 我这里定三个等级：Trivial、Normal、Blocker
    @allure.testcase('')
    @allure.issue('')
    @pytest.mark.parametrize("kw",["感冒","发烧"])
    def test_01_search_goodsB2C(self,kw):
        with allure.step("输入关键字进行搜索"):
            self.SearchPage.search_goodsB2C(kw)
            self.SearchPage.screenshots()
        with allure.step("检查搜索结果"):
            result = self.SearchPage.judge_Searchresult()
        assert result == True

    # # 由于setup_method设置的暂不可应用于O2O搜索（原理上说不属于同一个页面）
    # @allure.story("测试O2O搜索")
    # @allure.severity('normal')
    # @allure.testcase("http://www.testlink.com/id=002")
    # @allure.issue("http://www.jira.com/id=002")
    # @pytest.mark.parametrize('kw',['感冒','发烧'])
    # def test_02_search_goodsO2O(self,kw):      # 一个行为只在结束断言    就最后一步截图吧
    #     with allure.step("输入关键字进行搜索"):
    #         self.SearchPage.search_goodsO2O(kw)
    #         self.SearchPage.screenshots()
    #     with allure.step("检查搜索结果"):
    #         result = self.SearchPage.judge_Searchresult()
    #     assert result == True

    @allure.story("B2C搜索by历史记录")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_03_search_by_record(self):
        with allure.step("点击历史进行搜索"):
            self.SearchPage.search_by_record()
            self.SearchPage.screenshots()
        with allure.step("检查搜索结果"):
            result = self.SearchPage.judge_Searchresult()
        assert result == True

    @allure.story("测试搜索列表加购物车")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_04_addto_Carts(self):
        with allure.step("进行B2C搜索"):
            self.SearchPage.search_goodsB2C("感冒")
        with allure.step("找到商品加购物车"):
            result = self.SearchPage.addto_Carts()
        # 需要有一个判断
        assert result is True