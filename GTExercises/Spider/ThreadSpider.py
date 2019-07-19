#coding=utf-8
# s = u'\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'
# print (s)
import requests
from bs4 import BeautifulSoup
import random
header = [{'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},{'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}]
# header 是用来伪装成浏览器发送请求，一般加上最好，header 信息可以通过浏览器查看，也可在网上搜索得到。
url = 'https://www.miaobige.com/read/6588/2731453.html'
req = requests.get(url,headers = header[random.randint(0,4)])   # 向目标网站发送 get 请求
result = req.content
result = result.decode('gbk')    #  查看网页源代码 看到 charset=gbk，即网页是用的 gbk 编码，故要用 gkb 的编码方式来解码，否则中文就会乱码。
print(result)

# for read in reads:
#     s = read.decode('unicode_escape')
#     print('read:', s)