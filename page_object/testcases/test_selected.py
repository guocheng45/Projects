
import pytest

from page_object.pages.App import App
from page_object.pages.MainPage import MainPage


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()

    def test_price(self):
        assert self.mainPage.gotoSelected().gotoHS().getPriceByName("科大讯飞")==28.83
