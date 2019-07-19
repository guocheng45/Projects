# -*- coding: utf-8-*-
"""
安装：pip install requests
"""
import requests

url_login = "http://sup.pre.yyjzt.com/mobile/salesman/mobileLogin.json"
data_login = {"loginName":"wumeng","loginPwd":"123456","appVersion":"2.4.2","imei":"dced90296131e146","model":"DUK-AL20","systemVersion":"dced90296131e146"}

rs_login = requests.post(url_login, data=data_login)
header = rs_login.headers
cookies = header['Set-Cookie'].split(';')[0]

url_search = 'http://sup.pre.yyjzt.com/mobile/salesman/searchSecondLevelCust.json'
data_search = {"branchId": "FDG", "danwBh": "E420115104X001HA", "danwNm": "DWI35526279", "page": 1, "pageSize": 30}
headers = {
    'Cookie': cookies,
}

rs_search = requests.get(url_search, params=data_search, headers=headers)

print(rs_search.json())

