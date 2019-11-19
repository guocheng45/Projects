from page_object.pages.HysAPP import App


class TestPlaceOrder(object):

    # 炒个栗子
    def test_placeorder1(self):
        # 如要判断就加上断言
        assert App.main().gotoHyspage().place_order_B2CBuyNow()