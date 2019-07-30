import requests

from WeixinPro.contact.token import Weixin


class User:

    def create(self,data=None):
        res = requests.post('https://qyapi.weixin.qq.com/cgi-bin/department/create',
                          params={"access_token": Weixin.get_token()},
                          json=data
                          ).json()
        return res


    def list(self,department_id=1,fetch_child=0):
        res = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/simplelist',
                         params={"access_token": Weixin.get_token(),
                                 "department_id": department_id,
                                 "fetch_child": fetch_child}
                         ).json()
        return res