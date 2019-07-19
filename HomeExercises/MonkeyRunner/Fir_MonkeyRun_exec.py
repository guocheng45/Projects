#coding=utf-8
#-*- coding: utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage#这个错误正常，Eclip不认识它，在monkeyRunner来执行就行
#�����豸
device = MonkeyRunner.waitForConnection(3,"device_name")

#����APP
device.startActivity("com.example.zhangjian.minibrowser2/com.example.zhangjian.minibrowser2.myapplication.MainActivity")
MonkeyRunner.sleep(2)
#���������
device.touch(100,100,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
#�����ѯ��
device.type('test')
MonkeyRunner.sleep(1)
#����س���
device.press('KEYCODE_ENTER','DOWN_AND_UP')
MonkeyRunner.sleep(1)
#���������ť
device.touch(400,100,'DOWN_AND_UP')
MonkeyRunner.sleep(6)
#��ͼ
image = device.takeSnapshot()
image.writeTofile('./test.png','png')
#������ť
device.touch(300,100,'DOWN_AND_UP')
MonkeyRunner.sleep(3)