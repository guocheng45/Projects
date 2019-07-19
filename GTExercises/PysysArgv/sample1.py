# -*- coding: utf-8 -*- 
'''
Created on 2017年2月10日

@author: KTplay
'''
# sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径，所以参数从1开始，以下两个例子说明:
# 1、使用sys.argv[]的一简单实例:
# 以下是sample1.py文件：
import sys,os   
print (sys.argv )
os.system(sys.argv[1])  #os.system接收命令行参数，运行参数指令，cmd命令行带参数运行python sample1.py notepad，将打开一个无标题记事本程序。
#sys.argv[]当前理解为命令行中python之后的各个参数，0-sample1.py，1-后跟参数，2-空格后的又一个参数，参数应该都是字符串