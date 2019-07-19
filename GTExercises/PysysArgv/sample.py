#coding: utf-8  
import sys      
def readfile(filename):  #定义readfile函数，从文件中读出文件内容      
    '''''''''Print a file to the standard output.'''      
    f = file(filename)   #Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),writing or appending.   
    while True:      
        line = f.readline()    #next line from the file, as a string.（从文件中读取下一行）  
        if len(line) == 0:     #下一行的长度为0，即为空 
            break
        print(line, end=' ')  # notice comma  分别输出每行内容
    f.close()      
# Script starts from here    
print(sys.argv)  # 打印sys.argv数组内容
if len(sys.argv) < 2:                   #数组长度<2，表示数组只有一个成员，打印不允许的操作。
    print('No action specified.')
    sys.exit()                          #退出当前程序
if sys.argv[1].startswith('--'):        #坑人的垃圾操作判断参数是不是已--开头啊，后面跟的是不是version啊，help啊     
    option = sys.argv[1][2:]      
    # fetch sys.argv[1] but without the first two characters/提取   sys.argv[1]（）不包括前两个字符
    if option == 'version':  #当命令行参数为-- version，显示版本号      
        print('Version 1.2')
    elif option == 'help':   #当命令行参数为--help时，显示相关帮助内容      
        print
        ('  \n'
         '            This program prints files to the standard output.    \n'
         '            Any number of files can be specified.    \n'
         '            Options include:    \n'
         '            --version : Prints the version number    \n'
         '            --help    : Display this help')
    else:
        print('Unknown option.')
    sys.exit()      
else:      
    for filename in sys.argv[1:]: #当参数为文件名时，传入readfile，读出其内容
        readfile(filename)   