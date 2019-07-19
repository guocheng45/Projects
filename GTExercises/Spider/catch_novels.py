#coding=utf-8
import time

import requests
from bs4 import BeautifulSoup
import random
import re
import lxml

class CatchNovel():

    def get_content(self,url): #根据URL获取HTML中的小说内容
        header = [{'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
                {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
                {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
                {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},{'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}]
        # header 是用来伪装成浏览器发送请求，一般加上最好，header 信息可以通过浏览器查看，也可在网上搜索得到。
        #url = 'https://www.75txt.org/51/51921/26907483.html'
        req = requests.get(url,headers = header[random.randint(0,4)]) # 向目标网站发送 get 请求
        #req.encoding = 'gb18030' #hi,gays it is helpful！thank for https://www.cnblogs.com/mengyu/p/6759671.html
        soup=BeautifulSoup(req.text,'lxml') #解析lxml
        tags = soup.findAll('div')
        tags_a = soup.findAll('a')  #返回类型是一个bs4
        print(type(tags_a))
        print(type(tags_a))
        #next_url = self.use_a_getnext(tags_a)

        content = ''
        for i in tags:
            id = i.get('id')
            # str(step['action']).lower()
            if id=='chaptercontent':
                content = i.text
                break

        title = soup.title.string   #获取到标题
        print(title+'complete!') # 打印文章的标题
        print('content:',content) #打印文章的content
        self.write_to_file(title,content)   #调用方法写入文件中
        for i in tags_a:
            href = i.get('href')
            #print("href:",href) #get it href good
            i_class = i.get('class')
            if i_class !='disabled':
                nurl = 'https://m.luoqiuzw.com'+href
                print("nurl======================",nurl)
                time.sleep(30)
                self.get_content(nurl)  # 循环执行读取小说
                break
            else:
                url = ''
                print('小数读取完毕！')
            #print(i.get_text()) #print(i.get_text()) == print(i.string) output the middle text
            #print("len(tags_a):",len(tags_a))

    def use_a_getnext(self,a_tb):
        for a_next in a_tb:
            if a_next.text=='下一页' and a_next.get('class')!='disabled':
                href = a_next.get('href')
                nurl = 'https://m.luoqiuzw.com' + href
                return nurl
                break
            elif a_next.text=='下一页':
                nurl='no next'
                return nurl
                break





    def write_to_file(self,n_title,n_content):
        fo = open('aa.txt', "ab") #打开小说文件
        # 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码
        fo.write(('\r\n\n\r' + n_title + '\r\n').encode('UTF-8'))
        # 以二进制写入章节内容
        fo.write((n_content).encode('UTF-8'))
        fo.close()

    def get_codingmode(self,request):
        '''防止出现乱码'''
        pass

url = 'https://m.luoqiuzw.com/book/53082/38368952.html'
c=CatchNovel()
c.get_content(url)

