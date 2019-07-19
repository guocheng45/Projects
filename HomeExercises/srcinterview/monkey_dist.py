#-*- coding:utf-8 -*-
import os
import os.path
import time
import glob
from mhlib import PATH
#此脚本用于测试多个设备同时进行monkey测试
#删除已有的测试CMD脚本
path = 'E:\\monkey_test\\'
for file in glob.glob(os.path.join(path,'*.cmd')):
    os.remove(file)

os.system('cls')  #这个语句具有清屏功能
rt = os.popen('adb devices').readlines() #os.open()执行系统命令并返回执行结果,是一个list
n = len(rt)-2
print '当前连接设备数为：',n
aw = raw_input('是否要开始你的monkey测试，请输入Y/N:')  #命令框中的选择判断GG

if aw =='Y':
    print "monkey测试将要开始..."
    count = raw_input('请输入你要进行的monkey测试次数：')
    testmodel = raw_input('请输入你是要进行单次测试还是多次连续测试，1代表单次，2 代表多次：')
    ds = range(n) #[1,2,3...n]把设备数作为一个数组来用
    for i in range(n):
        nPos = rt[i+1].index('\t')
        ds[i] = rt[i+1] [:nPos]
        print '这是ds[i]:',ds[i]
        dev = ds[i]
        #获取手机型号
        promodel = os.popen('adb -s '+dev+' shell cat /system/build.prop | find "ro.product.model="').readlines()
        #modelname = ('').join(promodel) #将list转为字符串
        print 'adb -s '+dev+' shell cat /system/build.prop | find "ro.product.model="'
        print 'promodel',promodel
        modelname = promodel[0] #从list中取出第一个值
        model = modelname[17:].strip('\r\n')
        #获取手机名称
        proname = os.popen('adb -s '+dev+' shell cat /system/build.prop | find "ro.product.brand="').readlines()
        print 'adb -s '+dev+' shell cat /system/bulid.prop | find "ro.product.brand="'
        print 'proname:',proname
        roname = proname[0]
        name = roname[17:].strip('\r\n') #从第17个字符开始，到\r\n结束
        packagename = os.popen('adb -s '+dev+' shell pm list packages | find "android.gallery"').readlines()
        print 'adb -s '+dev+' shell pm list packages | find "android.gallery"'
        package = packagename[0]
        pk = package[8:].strip('\r\n')
        print 'pk:',pk
        if pk == 'com.android.gallery':
            filedir = os.path.exists('E:\\monkey_test\\')
            if filedir:
                print "File Exist!"
            else:
                os.mkdir("E:\\monkey_test\\")
            devicedir = os.path.exists("E:\\monkey_test\\"+name+'-'+model+'-'+dev)
            if devicedir:
                print "file exist!"
            else:
                os.mkdir("E:\\monkey_test\\"+name+'-'+model+'-'+dev) #按设备ID声场日志目录文件夹
            wl = open("E:\\monkey_test\\"+name+'-'+model+'-'+ds[i]+'-logcat'+'.cmd','w')
            #wl.write('adb -s ' + dev + ' logcat -v time ACRA:E ANRManager:E System.err:W *:S')
            wl.write('adb -s '+dev+' logcat -v time *:W')
            #wl.write('>E\\monkey_test\\'+'"'+name+'-'+model+'-'+dev+'"'+'\\logcat_%random%.txt\n')
            wl.write('>E:\\monkey_test\\'+name+'-'+model+'-'+dev+'\\logcat_%random%.txt\n')
            wl.close()
            if testmodel == '1':
                wd = open("E:\\monkey_test\\"+name+'-'+model+'-'+ds[i]+'-device'+'.cmd','w')
                wd.write(
                         'adb -s '+dev+' shell monkey -p com.android.gallery --monitor-native-crashes --ignore-crashes --pct-syskeys 5 --pct-touch 55 --pct-appswitch 20 --pct-anyevent 20 --throttle 200 -s %random% -v '
                         +count) #选择设备执行monkey
                #wd.write('>E:\\monkey_test\\'+'"'+name+'-'+dev+'"'+'\\monkey_%random%.txt/n')
                wd.write('>E:\\monkey_test\\'+name+'-'+model+'-'+dev+'\\monkey_%random%.txt\n')
                wd.write('@echo 测试成功完成，请查看日志文件~')
                wd.close()
            elif testmodel == '2':
                wd = open('E:\\monkey_test\\'+name+'-'+model+'-'+ds[i]+'-device'+'.cmd','w')
                wd.write(':loop')
                wd.write('\nset /a num+=1')
                wd.write('\nif "%num%"=="4" goto end')
                #选择设备执行monkey
                wd.write('\nadb -s ' + dev + ' shell monkey -p com.android.gallery --monitor-native-crashes --ignore-crashes --pct-syskeys 5 --pct-touch 55 --pct-appswitch 20 --pct-anyevent 20 --throttle 200 -s %random% -v ' + count)
                #wd.write('>E:\\monkey_test\\' + '"'+ name  + '-'+ model + '-' + dev + '"' + '\\monkey_%random%.txt\n')
                wd.write('>E:\\monkey_test\\' + name  + '-'+ model + '-' + dev + '\\monkey_%random%.txt\n')
                wd.write('@echo 测试成功完成，请查看日志文件~')
                wd.write('\nadb -s '+ dev +' shell am force-stop '+ pk)
                wd.write('\n@ping -n 15 127.1 >nul')
                wd.write('\ngoto loop')
                wd.write('\n:end')
                wd.close()
            else:
                print '请确认待测手机'+name+'-'+model +'未安装com.XXX~'
        #执行上述生成的cmd脚本path='E:\\monkey_test\\'
        print path
        
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path,file)) == True:
                if file.find('.cmd')>0:
                    os.system('start '+os.path.join(path,'"'+file+'"')) #dos 命令中文件名如果有空格，许加上双引号
                    time.sleep(1)
elif aw == 'no':
    print('请重新确认所有的待测手机是否已通过adb命令连接到PC！')
else:
    print '测试结束，输入非法，请重新输入yes or no!'