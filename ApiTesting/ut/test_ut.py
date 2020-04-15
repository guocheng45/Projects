from pprint import pprint
import requests

proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}

def test_request():
    r = requests.get("https://www.cnblogs.com/lshedward/p/9959845.html")
    pprint(r)
    print(r.status_code)


def test_get():
    r = requests.get("http://httpbin.testing-studio.com/get", params={
        "a": 1,
        "b": 2
    })
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("http://httpbin.testing-studio.com/post", data={
        "a": 1,
        "b": 2
    },
                      headers={"h": "headdemo"},
                      proxies=proxies,
                      verify=False)     # 设置Charles代理，认证关闭，不然会报错————目的是抓包调试
    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["H"] == "headdemo"


def test_upload():
    r = requests.post("http://httpbin.testing-studio.com/post",
                      files={"file": open('__init__.py', 'rb')},
                      proxies=proxies,
                      verify=False
                      )  # 设置Charles代理，认证关闭，不然会报错————目的是抓包调试

    print(r.json())
    print(r.text)
    assert r.status_code == 200


def test_hook():            # 不懂
    def modify_response(r, *args, **kwargs):
        r.decode_content = "demo content"
        return r

    r = requests.get("http://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2
                     },
                     hooks = {"response":[modify_response]}
                     )
    print(r.json())
    print(r.decode_content)
    assert r.status_code == 200
