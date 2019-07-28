from contact.token import Weixin
import requests
import json
import logging

class TestWeixin:
    @classmethod
    def setup_class(cls):
        Weixin.get_token()
        print(Weixin.token)

    def setup(self):
        pass

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