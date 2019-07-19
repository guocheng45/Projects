# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

def show_entry():
    text1.configure(state="normal")     #先把text的属性设置为可编辑的
    text1.insert(1.0,e.get())
    s = e.get()
    print "获取到text中的输入信息：",s 
    text1.configure(state="disabled")   #disabled，输入内容后设置控件属性不可编辑
e = StringVar()
entry1 = Entry(root,textvariable=e)

bt1 = Button(root,text="查  看",command = show_entry)

text1 = Text(root,width=25,height=5)

entry1.grid(row=0,column=0,padx=15,pady=2)
bt1.grid(row=1,column=0,padx=15,pady=2)
text1.grid(row=2,column=0,padx=15,pady=2)
root.mainloop()

#from Tkinter import * 
#root = Tk() 
#t = Text(root) 
#t.pack() 
#t.insert(1.0,'0123456789')
#t.delete(1.0,END)           #如无此句则展示0123456789jcodeer，有则展示jcodeer
#t.insert(END,'jcodeer')
#t.focus_force()
#root.mainloop()

