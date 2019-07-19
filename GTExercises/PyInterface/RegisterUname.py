# -*- coding: utf-8 -*- 


from Tkinter import *
import ttk
import Regisintfa

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
regis = Regisintfa.RegisIntfa()
class Application():

    def __init__(self,Mframe):
        self.Mframe = Mframe
        self.main_widget()
        self.other_widget()
        
    def main_widget(self):
        self.top_lb = Label(self.Mframe,fg = "blue",bg = "green",text = "注册用户名",font = ('Tempus Sans ITC', 15))
        self.top_lb.grid(row = 0,column = 0,padx = 15,pady = 2)  #布局：行、列、控件周围x方向空白大小、控件周围y方向空白大小
        

    def other_widget(self):
        self.lb_frame = LabelFrame(self.Mframe,height=200,width=300)    #创建一个容器放置于Mframe中
        self.lb_frame.grid(row=1,column=0,padx=15,pady=2)
        
        self.lb0 = Label(self.lb_frame,text="环    境：")
        self.lb0.grid(row=0,column=0,padx=15,pady=2)
        self.box_value = StringVar()
        self.comb0 = ttk.Combobox(self.lb_frame, textvariable=self.box_value, state='readonly')
        self.comb0['values'] = ('CN','EN')
        #艹不能用啊，怎么回事。。。
        #self.comb0.current(1) #显示默认选择项
        #self.comb0.set("演员表")#设置默认选项
        #print self.comb0.get()
        self.comb0.grid(row=0,column=1,padx=5,pady=2)
    
        self.lb1 = Label(self.lb_frame,text="用户名关键字：")                    #label控件
        self.lb1.grid(row=1,column=0,padx=15,pady=2)
        #输入框
        self.str_ent1 = StringVar()
        self.enty1 = Entry(self.lb_frame,textvariable = self.str_ent1)
        self.enty1.grid(row=1,column=1,padx=15,pady=2)
        
        self.lb2 = Label(self.lb_frame,text="game_id：")
        self.lb2.grid(row=2,column=0,padx=15,pady=2)
        #输入框
        self.str_ent2 = StringVar()
        self.enty2 = Entry(self.lb_frame,textvariable = self.str_ent2)
        self.enty2.insert(0, 4398)
        self.enty2.grid(row=2,column=1,padx=15,pady=2)

        self.lb3 = Label(self.lb_frame,text="创建个数：")
        self.lb3.grid(row=3,column=0,padx=15,pady=2)
        #输入框
        self.str_ent3 = StringVar()
        self.enty3 = Entry(self.lb_frame,textvariable = self.str_ent3)
        self.enty3.grid(row=3,column=1,padx=15,pady=2)

        #button按钮
        self.bt1 = Button(text = "提交",width=10,command = self.Regis_list)   #, command=self.runtime()#height是text行数；width是
        self.bt1.grid(row=3,column = 0,padx=15,pady=2)        #sticky="e"/w左对齐，e右对齐（west西左西，east东右东）
        self.tex0 = Text(self.Mframe,width =25 ,height = 5)
        self.tex0.grid(row=4,column = 0,padx=15,pady=2)
    def Regis_list(self):
        Uname = self.str_ent1.get()
        num= self.str_ent3.get()
        times=1
        #print "Uname:",Uname,"ent3:",num
        #print type(num)
        if Uname !='' and num!='':
            while (times<=int(num)):
                Unamed = Uname + str(times)
                self.produced(Unamed)
                times=times+1
                #print type(times)
                #print 'Times:',times,'NUM:',num
        else:
            self.tex0.configure(state = 'normal')
            self.tex0.insert(END, '没有用户名或创建个数！'+'\n')
            self.tex0.configure(state = 'disabled')
        
        
        
    def produced(self,Uname):
        comb0_value = self.comb0.get()  #打印选中项的值
        print comb0_value
        if comb0_value =="CN":
            #Uname = self.str_ent1
            gid = self.enty2.get()
            self.rets = regis.CN_regist_username(Uname, gid)
            if self.rets >= 0:
                self.tex0.configure(state = 'normal')
                self.tex0.insert(END, Uname+'登录成功'+'\n')
                self.tex0.configure(state = 'disabled')
            else:
                self.tex0.configure(state = 'normal')
                self.tex0.insert(END, '登录失败！'+'\n')
                self.tex0.configure(state = 'disabled')
            
        elif comb0_value =="EN":
            Uname = self.str_ent1
            gid = self.enty2.get()
            self.rets = regis.EN_regist_username(Uname, gid)
            if self.rets >= 0:
                self.tex0.configure(state = 'normal')
                self.tex0.insert(END, Uname+'登录成功'+'\n')
                self.tex0.configure(state = 'disabled')
            else:
                self.tex0.configure(state = 'normal')
                self.tex0.insert(END, '登录失败！'+'\n')
                self.tex0.configure(state = 'disabled')
            
        else:
            self.tex0.configure(state = 'normal')
            self.tex0.insert(END, '没有环境啊！'+'\n')
            self.tex0.configure(state = 'disabled')
#     
#     def runtime(self):
#         print (self.str_ent1.get())
#         print (self.str_ent2.get())

MainFrame = Tk()
MainFrame.title("Register")
Application(MainFrame)
MainFrame.mainloop()
