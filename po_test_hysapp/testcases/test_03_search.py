# coding=utf-8
from po_test_hysapp.pages.HysAPP import HysApp
import pytest
import allure


@allure.feature("测试APP搜索页")
class TestSearch(object):

    @classmethod
    def setup_class(cls):  # 类执行一下，如启动APP
        # cls.mainPage = HysApp.main()  # 可能有问题-没问题
        cls.profile = HysApp.main().gotoProfile()   # 也可以如此写

    def setup_method(self):  # 设置等于自己的mainPage，可以直接调用？
        # self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP           可能搞错了
        # self.ProfilePage = self.mainPage.gotoProfile()    # 不同的页面的测试不要放在一个页面，初始化的时候会乱点其他页面
        pass

    def teardown_method(self):
        # 如返回至初始页可放置在此
        # self.Hyspage.back()
        pass

    @classmethod
    def teardown_class(cls):
        # time.sleep(2)
        # cls.driver.quit()
        pass

    # 炒个栗子
    # def test_placeorder1(self):
    #     # 如要判断就加上断言
    #     assert self.mainPage.gotoHyspage().place_order_B2CBuyNow()
    #     assert "something" in self.mainPage.gotoProfile().getErrorMsg()
    # 下一步
    # 再一个assert

    @allure.story("测试是否已登录")
    @allure.severity('Trivial')  # 我这里定三个等级：Trivial、Normal、Blocker
    @allure.testcase('')
    @allure.issue('')
    def test_01_islogin(self):
        with allure.step("个人页是否登录"):
            result = self.profile.is_login_app()
            self.profile.screenshots()
        assert result == "not logged"

    @allure.story("测试登录后，跳转个人设置")
    @allure.severity('normal')
    @allure.testcase("http://www.testlink.com/id=002")
    @allure.issue("http://www.jira.com/id=002")
    def test_02_jump_avatar(self):      # 一个行为只在结束断言    就最后一步截图吧
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951","123456")
        with allure.step("跳转个人设置"):
            result = self.profile.click_avatar()
        assert result == "test_郭志成"

    @allure.story("测试登录后，跳转充值")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_03_jump_recharge(self):
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951", "123456")
        with allure.step("跳转充值"):
            result = self.profile.click_recharge()
        assert result is True

    @allure.story("测试登录后，跳转我的订单")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_04_jump_myOrders(self):
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951", "123456")
        with allure.step("跳转我的订单"):
            result = self.profile.click_myorder()
        assert result is True

    @allure.story("测试登录后，跳转待付款")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_05_jump_payment(self):
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951", "123456")
        with allure.step("跳转待付款"):
            result = self.profile.click_payment()
        assert result is True

    @allure.story("测试登录后，跳转我的需求")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_06_jump_needs(self):
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951", "123456")
        with allure.step("跳转我的需求"):
            result = self.profile.click_needs()
        assert result is True

    @allure.story("测试登录后，跳转我的优惠券")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_07_jump_myCoupon(self):
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951", "123456")
        with allure.step("跳转我的优惠券"):
            result = self.profile.click_mycoupon()
        assert result is True

    @allure.story("测试登录后，跳转地址管理")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_08_jump_manager_address(self):
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951", "123456")
        with allure.step("跳转地址管理"):
            result = self.profile.click_manager_address()
        assert result is True

    @allure.story("测试登录后，跳转我的收藏")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_09_jump_mycollection(self):
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951", "123456")
        with allure.step("跳转我的收藏"):
            result = self.profile.click_mycollection()
        assert result is True

    @allure.story("测试登录后，跳转会员中心")
    @allure.severity("normal")
    @allure.testcase('')
    @allure.issue('')
    def test_10_jump_members(self):
        with allure.step("查看是否已登录"):
            login_status = self.profile.is_login_app()
        if login_status == "not logged":
            with allure.step("未登录，先登录"):
                self.profile.gotoLogin().login_success_byuser("15001106951", "123456")
        with allure.step("跳转会员中心"):
            result = self.profile.click_members()
        assert result is True
