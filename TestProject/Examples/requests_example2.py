# -*- coding: utf-8-*-
"""
安装：pip install requests
"""
import requests

s = requests.Session()

url_login = "http://sup.pre.yyjzt.com/mobile/salesman/mobileLogin.json"
data_login = {"loginName":"wumeng","loginPwd":"123456","appVersion":"2.4.2","imei":"dced90296131e146","model":"DUK-AL20","systemVersion":"dced90296131e146"}

rs_login = s.post(url_login, data=data_login)

url_search = 'http://sup.pre.yyjzt.com/mobile/salesman/searchSecondLevelCust.json'
data_search = {"branchId": "FDG", "danwBh": "E420115104X001HA", "danwNm": "DWI35526279", "page": 1, "pageSize": 30}

rs_search = s.get(url_search, params=data_search)

print(rs_search.json())

