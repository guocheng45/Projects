from WeixinPro.contact.token import Weixin
from WeixinPro.contact.user import User
import requests
import json
import logging
import time

class TestUser:

    @classmethod
    def setup_class(cls):
        # todo: creat depart
        cls.user = User()

    def test_create(self):
        uid = "seveniruby_" + str(time.time())
        data = {
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid + "@testerhome.com"
        }
        r = self.user.create(data)
        logging.debug(r)
        assert r['errcode'] == 0

    def test_list(self):
        r = self.user.list(1, 0)
        r = self.user.list(department_id=65)
        logging.debug(r)
        assert r['errcode'] == 0
