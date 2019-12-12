from tkinter import *
root = Tk()
'''
TKinter3种布局方式，这里选用grid，使用表格布局。
加入自动将密码转换成*
'''

Label(root,text = "账号：").grid(row = 0,column = 0)#第0行，第0列
Label(root,text = '密码：').grid(row = 1,column = 0)

v1 = StringVar()
v2 = StringVar()#一个存放账号，一个存放密码

e1 = Entry(root,textvariable = v1)
e2 = Entry(root,textvariable = v2,show = '$')
#获取输入的内容并存入，show后面定义显示样子。

e1.grid(row = 0,column = 1,padx = 20,pady = 10)
e2.grid(row = 1,column = 1,padx = 20,pady = 10)

def show():
    print('账号：%s'% e1.get())
    print('密码：%s'% e2.get())


Button(root,text = '打印信息',width=10,command = show).\
    grid(row = 3,column = 0,sticky = W,padx = 20,pady = 10)
Button(root,text = '退出',width=10,command = root.quit).\
    grid(row = 3,column = 1,sticky = E,padx = 20,pady = 10)



mainloop()