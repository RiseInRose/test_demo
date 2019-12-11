from tkinter import *
root = Tk()
'''
TKinter3种布局方式，这里选用grid，使用表格布局。
'''

Label(root,text = "作品：").grid(row = 0,column = 0)#第0行，第0列
Label(root,text = '作者：').grid(row = 1,column = 0)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row = 0,column = 1,padx = 20,pady = 10)
e2.grid(row = 1,column = 1,padx = 20,pady = 10)

def show():
    print('作品：《%s》'% e1.get())
    print('作者：《%s》'% e2.get())


Button(root,text = '获取信息',width=10,command = show).\
    grid(row = 3,column = 0,sticky = W,padx = 20,pady = 10)
Button(root,text = '退出',width=10,command = root.quit).\
    grid(row = 3,column = 1,sticky = E,padx = 20,pady = 10)



mainloop()