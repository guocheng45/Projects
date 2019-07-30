
import requests
import json
import logging

from WeixinPro.contact.token import Weixin


class TestWeixin:
    @classmethod
    def setup_class(cls):
        Weixin.get_token()
        print(Weixin.token)

    def setup(self):
        pass


    def test_get_token(self):
        print(Weixin.get_token())
        assert Weixin.get_token() !=""