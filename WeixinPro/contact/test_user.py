from WeixinPro.contact.token import Weixin
from WeixinPro.contact.user import User
import requests
import json
import logging

class TestUser:

    @classmethod
    def setup_class(cls):
        #todo: creat depart
        cls.user=User()


    def test_create(self):
        data={
            "name":"广州研发中心",
            "parentid":"1",
            "order": "1",
            "id": "2"
        }
        # r=requests.post('https://qyapi.weixin.qq.com/cgi-bin/department/create',
        #               params={"access_token":Weixin.get_token()}
        #               ,json=data).json

        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/department/list',
                          params={"access_token": Weixin.get_token()}
                          , json=data).json

        logging.info(json.dumps(r,indent=2))


    def test_list(self):
        pass