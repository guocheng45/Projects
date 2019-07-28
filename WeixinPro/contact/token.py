import requests
import yaml
import logging

class Weixin:
    logging.basicConfig(level=logging.DEBUG)
    _token="xxx"
    @classmethod
    def get_token(cls):
        if len(cls._token)==0:
            cls._token = "xxxxxxx"
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
            requests.get(url,params={"corpid": "", "corpsecret": ""})
        else:
            return cls._token
