from tkinter import *
root = Tk()

v = IntVar()
# 需要预先定义变量类型

c = Checkbutton(root, text = 'just check',variable = v)
c.pack()

l = Label(root, textvariable = v)
l.pack()

mainloop()