#coding=utf-8


from xml.dom.minidom import parse
import xml.dom.minidom

#使用minidom 解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse('movies.xml')  # 打开movies.xml文件
collection = DOMTree.documentElement    # 获取xml文件中的数据
if collection.hasAttribute("shelf"):    # 判断里面是否有项叫'shelf'
    print("Root element : %s" % collection.getAttribute("shelf"))   # 存在则打印 'shelf' 的值

# 在集合中获取所有的电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:    # 循环每一个movie
    print("**********movie**********")
    if movie.hasAttribute("title"): # 判断movie的节点下是否存在 ‘title’
        print("Title: %s" % movie.getAttribute("title"))    # 打印存在的 title 的值

    type = movie.getElementsByTagName('type')[0]    # 定义一个type 等于movie 下的第一个type 节点
    print("type: %s" % type.childNodes[0].data)     # 打印type 节点中间的文案信息
    format = movie.getElementsByTagName('format')[0]
    print("format: %s" % format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print("rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print("description: %s" % description.childNodes[0].data)