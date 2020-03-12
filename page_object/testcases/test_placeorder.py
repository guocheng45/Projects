# coding=utf-8
from page_object.pages.HysAPP import HysApp
from page_object.pages.HysBase import HysBase
from page_object.pages.HysMainPage import HysMainPage
import pytest
from page_object.pages.HysPage import HysPage
import allure

@allure.feature("测试好药师APP搜索")
class TestPlaceOrder(object):

    @classmethod
    def setup_class(cls):  # 类执行一下，如启动APP
        cls.mainPage = HysApp.main()  # 可能有问题-没问题
        # cls.hysPage = HysApp.main().gotoHyspage()   # 也可以如此写

    def setup_method(self):  # 设置等于自己的mainPage，可以直接调用？
        # self.mainPage:HysMainPage=TestPlaceOrder.mainPage    # 意指，还等于mainpage,再次启动APP           可能搞错了
        # self.ProfilePage = self.mainPage.gotoProfile()    # 不同的页面的测试不要放在一个页面，初始化的时候会乱点其他页面
        self.Hyspage = self.mainPage.gotoHyspage()

    def teardown_method(self):
        # 如返回至初始页可放置在此
        self.Hyspage.search_back()


    @classmethod
    def teardown_class(cls):
        pass

    # 炒个栗子
    # def test_placeorder1(self):
    #     # 如要判断就加上断言
    #     assert self.mainPage.gotoHyspage().place_order_B2CBuyNow()
    #     assert "something" in self.mainPage.gotoProfile().getErrorMsg()
    # 下一步
    # 再一个assert

    @allure.story("测试登录功能")
    @allure.severity('normal')
    @allure.testcase("http://www.testlink.com/id=001")
    @allure.issue("http://www.jira.com/id=001")
    @pytest.mark.parametrize("phone,pwd,msg", [("15001106951", "123456", "成功"), ("15001106951", "abc123", "错误")])
    def test_01_login(self, phone, pwd, msg):
        if self.ProfilePage.is_login_app() == 0:
            assert str(self.ProfilePage.login_app(phone, pwd).getToastMsg()).__contains__(msg)
        else:
            assert str(self.ProfilePage.logout_app().login_app(phone, pwd).getToastMsg()).__contains__(msg)

    @allure.story("测试搜索功能")
    @allure.severity('blocker')
    @allure.testcase("http://www.testlink.com/id=002")
    @allure.issue("http://www.jira.com/id=002")
    @pytest.mark.parametrize("kw,jr", [("感冒", "//*[contains(@text,'感')]"), ("发烧", "//*[contains(@text,'发')]")])
    def test_02_search(self, kw, jr):
        with allure.step("使用关键字进行搜索"):
            result = self.Hyspage.search_goodsB2C(kw)
        with allure.step("获取搜索结果的长度"):
            search_resault = result.judge_Searchresult(jr)
        assert search_resault > 1

    def test_03_placeOrder(self):           # 一个行为只在结束断言
        self.Hyspage.cart_goods_isChecked()
        # 精确找到某品  断言找到了某品（万一网络问题查无结果？）
        a = "search goods"
        assert a==2
        if a==2:
            # 加入购物车  断言加购成功11
            b="add to cart"
            assert b==3
            if b==3:
                # 跳转购物车  断言跳转购物车成功
                c="jump cart"
                assert c==4
                if c==4:
                    d="is all select"
                    assert d==5
                    if d==5:
                        e="select goods"
                        assert e==6
                        if e==6:
                            f="click commit"
                            assert f==7
                            if f==7:
                                g="order commit"
                                assert g==8
                                if g==8:
                                    print("下单成功")
                                    h="return mainpage"
                                else:
                                    print("下单失败")
                            else:
                                print("click commit failure")
                        else:
                            print("select goods failure")
                    else:
                        print("all select failure")
                else:
                    print("jump cart failure")
            else:
                print("add to cart failure")
        else:
            print("search goods failure")

            # 判断购物车中全选按钮是否选中  选中则点一次取消，
            # 然后选中某品  断言弹框提示成功？？？
            # 点击购物车提交  断言跳转提交订单页成功？？
            # 点击提交订单页提交  断言跳转收银台成功？？
            # 返回到首页
