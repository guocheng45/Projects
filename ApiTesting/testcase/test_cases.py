import requests
import logging
import pytest
import json

class TestRequsts(object):
    logging.basicConfig(level=logging.INFO)
    url = "https://testerhome.com/api/v3/topics.json?limit=2"
    def test_get(self):
        r = requests.get(self.url)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))

    def test_post(self):
        r=requests.post(self.url,data={"a":1,"b":2},
                        header={"a": "a1", "b": "b2"},
                        proxies={"http":"http://127.0.0.1:8888","https":"https://127.0.0.1:8888"},
                        verify=False)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_cookies(self):
        pass
        #assert r.json()["data"]["catagory"]
    def test_xuqiu_quote(self):
        cookie = {"xq_a_token":	"5806a70c6bc5d5fb2b00978aeb1895532fffe502","u":"3446260779"}
        t_url = "https://101.201.175.228/v5/stock/portfolio/stock/list.json"
        t_params = {"category":1,"pid":-1,"size":10000,"x":1.3,"page":1}
        t_header = {"User-Agent": "Xueqiu Android 11.19","Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
                    "Host": "stock.xueqiu.com"}
        r= requests.get(t_url,params=t_params,cookies=cookie,headers=t_header,verify=False)
        logging.info(json.dumps(r.json(), indent=2))