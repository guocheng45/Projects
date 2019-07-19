# -*- coding: UTF-8 -*-

import swampy.Gui as spy


gui = spy.Gui()
gui.title("Frame Work place")
top_lb = gui.la(text="这里是标题名称哦！",fg="blue",bg="yellow",font=('tempus sans itc',15))
top_lb.grid(row=0,column=0,padx=15,pady=2)

lb1 = gui.la(text="用户名:",font=('tempus sans itc',15))

gui.mainloop()

'''
def hello():
    ca.text([0,0],'hello','red')

gui = spy.Gui()
gui.title("练习本1！")
#不能用。。win = gui.frame(None,title="simple Editor")
gui.row()            #新建行
ca = gui.ca(bg='blue')
gui.col()            #新建列
gui.bu(text='Hello',command=hello) #于是两个按钮在同一列，按钮和画布（Canvas）在同一行。
gui.bu(text='Quit',command=gui.quit)
gui.endcol()         #新建和结束行和列通常都是成对出现的（对应14和15）
gui.endrow()
gui.mainloop()


g=spy.Gui()
g.gr(3)   #gr(cols, cweights, rweights) 分列

for i in range(1,10):
    g.bu(text=str(i))   #bu(text, command) button
    
g.mainloop()
'''