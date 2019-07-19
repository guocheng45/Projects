import pytest
# import random
# @pytest.mark.parametrize("x",[(1),(2),(6)])
#
# def test_add(x):
#     print(x)
#     assert x ==random.randrange(1,7)

#def test_assume_assert():
'''2、使用logger设置日志，将日志保存到文件。
    3、查找 / tomcat / log / 目录下的log文件，如果文件最后修改时间是在1小时之前，把次文件打包压缩，备份到
    / home / back / log
    目录下
    4、在Linux下每隔1分钟检查一下tomcat进程是不是在运行，如果tomcat进程退出了，立即启动tomcat进程
    
'''
import os
import subprocess
print(os.stat('demo.txt')[9])
subprocess.check_output(['tar -xvf tomcat.tar log'], shell=True)  #打包的命令

'''
5、搜索目录 / home / tools / 下所有已test开头，py结尾的文件(包括子目录的), 把文件全路径输出到一个列表里面打印出来
'''
import glob
import os
os.path.dirname()
os.path.isdir()
print(glob.glob('path',recursive=True))     #循环查找文件，百度一下吧

"".endswith(".py")