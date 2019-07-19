# -*- coding: UTF-8 -*-

from Tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
root.title("nishisadiaoo")
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)
lb1=Label(root,text="213213",width=15,heigh=2)
tx1=Text(root,width=15,heigh=1)


lb1.pack()                      #默认显示位置
tx1.pack(side = BOTTOM)           #向左显示~~~side: 决定哪方父widget包对TOP（默认），BOTTOM下，LEFT左，或RIGHT右.
#tx1.place(x= 20, y = 13)
listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环