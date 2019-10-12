'''
import urllib
import urllib3
import re

class Spider:
    def __init__(self):
        self.underURL1 = 'http://mm.taobao.com/json/request_top_list.htm'
        
    def getpageAll(self,pageIndex):
        url1 = self.underURL1+'?page='+str(pageIndex)
        #print url1
        request = urllib3.Request(url1)
        response = urllib3.urlopen(request)
        return response.read().decode('gbk')
    
    def getContents(self,pageIndex):
        pageAll = self.getpageAll(pageIndex)
        #print "pageAll:",pageAll
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,pageAll)
        for item in items:
            print (item[0],item[1],item[2],item[3],item[4])
der = Spider()
der.getContents(1)
'''