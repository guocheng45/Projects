# -*- coding: UTF-8 -*-

from Tkinter import *
import MongoDBConn
root = Tk()

dbconn = MongoDBConn.DBConn()
def show_entry():
    text1.configure(state="normal")     #先把text的属性设置为可编辑的
    text1.delete(1.0,END)
    phone_num = e.get()
    if int(phone_num)<10000000000:
        phone_string = '+81-'+phone_num
    else:
        phone_string = '+86-'+phone_num
    
#    print phone_string
    returns = dbconn.select_code(phone_string)
    text1.insert(1.0,returns)
    text1.configure(state="disabled")   #disabled，输入内容后设置控件属性不可编辑
e = StringVar()
entry1 = Entry(root,textvariable=e)

bt1 = Button(root,text="查看验证码",command = show_entry)

text1 = Text(root,width=25,height=5)

entry1.grid(row=0,column=0,padx=15,pady=2)
bt1.grid(row=1,column=0,padx=15,pady=2)
text1.grid(row=2,column=0,padx=15,pady=2)
root.mainloop()

