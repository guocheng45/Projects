import pytest

from page_object.pages.App import App
from page_object.pages.MainPage import MainPage


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()

    def setup_method(self):
        self.mainPage :MainPage=TestSelected.mainPage
        self.searchPage=self.mainPage.gotoSearch()

    def test_is_selected_stock(self):
        self.searchPage.search("alibaba")
        assert self.searchPage.isInSelected("BABA")==True
        assert self.searchPage.isInSelected("1688")==False

    def test_price(self):
        main = MainPage()
        assert main.gotoSelected().getPriceByName("科大讯飞")==28.83

    def test_add_stock(self):
        pass

    @pytest.mark.parametrize("key,code",[
        ("招商银行","SH600036"),
        ("平安银行", "SZ000001"),
        ("pingan", "SH601318")
    ])
    #上面的'参数化'可用于下面方法的循环调用
    #判断SH600036股票是否存在
    def test_is_selected_stock_hs(self,key,code):
        self.searchPage.search(key)
        assert self.searchPage.isInSelected(code)==False

    def teardown_method(self):
        self.searchPage.cancel()

    def test_add_stock_hs(self):
        key='招商银行'
        code='SH600036'
        searchPage = self.searchPage.search(key)
        if searchPage.isInSelected(code)==True:         #判断是否已经选择了，选择了就取消选择
            searchPage.removeFromSelected(code)

        searchPage.addToSelected(code)
        assert searchPage.isInSelected(code)==True

    def back(self):
        self.find()
        # WebDriverWait