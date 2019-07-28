from contact.token import Weixin



class TestDepartment:
    @classmethod
    def setup_class(cls):
        Weixin.get_token()
        print(Weixin.token)

    def test_weixintoken(self):
        pass

    