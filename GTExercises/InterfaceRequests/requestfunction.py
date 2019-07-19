# coding=utf-8
# 接口请求的get方法
import json

import requests

'''
req = requests.get('http://httpbin.org/get')

#传参
url = 'http://httpbin.org/get'
param = {'key1': 'value1', 'key2': 'value2', 'key3': None}
req = requests.get(url, param)

param = {'key1': 'value1', 'key2': ['value2', 'value3']}
req = requests.get('http://httpbin.org/get', param)
print(req.url)


# r.raw返回原始socket respons，需要加参数stream=True
r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)
resault = r.raw.read(10)
print(resault)

url = 'http://httpbin.org/cookies'
headers = {'user-agent': 'my-app/0.0.1'}
# 传递headers
r = requests.get(url, headers=headers)
# 传递cookies
r = requests.get(url, cookies=dict(cookies_are='working'))
'''
'''
#保存的图片的保存成功
url = "http://wx4.sinaimg.cn/large/d030806aly1fq1vn8j0ajj21ho28bduy.jpg"
rsp = requests.get(url, stream=True)
with open('1.jpg', 'wb') as f:
    for i in rsp.iter_content(chunk_size=2048):  # 边下载边存硬盘, chunk_size 可以自由调整为可以更好地适合您的用例的数字
        f.write(i)
'''

# POST请求
url = 'http://httpbin.org/post'
datas = {'key': 'value'}
r = requests.post(url, datas)
print('r1:',r.text)

#传递一个 string形式的参数

#r = requests.post(url,data=json.dumps(datas))
#or use this
r = requests.post(url,json=datas)
print('r2:',r.text)

#files1 = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
files2 = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
files3 = {'file':open('events.txt','rb')}
r3 = requests.post(url,files2)
print('r3.status_code:',r3.status_code)
print('r3.headers:',r3.headers)
print('r3.cookies:',r3.cookies)

requests.get('http://github.com', timeout=0.001)