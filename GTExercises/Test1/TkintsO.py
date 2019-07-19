# -*- coding: utf-8 -*- 


from Tkinter import *

class Application():

    def __init__(self,Mframe):
        self.Mframe = Mframe
        self.main_widget()
        self.other_widget()
        
    def main_widget(self):
        self.top_lb = Label(self.Mframe,fg = "blue",bg = "green",text = "这里是你想要输入的标题",font = ('Tempus Sans ITC', 15))
        self.top_lb.grid(row = 0,column = 0,padx = 15,pady = 2)  #布局：行、列、控件周围x方向空白大小、控件周围y方向空白大小
        

    def other_widget(self):
        self.lb_frame = LabelFrame(self.Mframe,height=200,width=300)
        self.lb_frame.grid(row=1,column=0,padx=15,pady=2)
    
        self.lb1 = Label(self.lb_frame,text="用户名：")
        self.lb1.grid(row=0,column=0,padx=15,pady=2)

        #输入框
        self.str_ent1 = StringVar()
        self.enty1 = Entry(self.lb_frame,textvariable = self.str_ent1)
        self.enty1.grid(row=0,column=1,padx=15,pady=2)

        self.lb2 = Label(self.lb_frame,text="密   码：")
        self.lb2.grid(row=1,column=0,padx=15,pady=2)
        #输入框
        self.str_ent2 = StringVar()
        self.enty2 = Entry(self.lb_frame,textvariable = self.str_ent2,show="*")
        self.enty2.grid(row=1,column=1,padx=15,pady=2)

        #button按钮
        self.bt1 = Button(text = "提交",width=10)   #, command=self.runtime()#height是text行数；width是
        self.bt1.grid(row=3,column = 0,padx=15,pady=2)        #sticky="e"/w左对齐，e右对齐（west西左西，east东右东）
    
#     def show_info(self):
#         self.lsbox = labe
#     
#     def runtime(self):
#         print (self.str_ent1.get())
#         print (self.str_ent2.get())

MainFrame = Tk()
MainFrame.title("what do you want to say?")

Application(MainFrame)
MainFrame.mainloop()
