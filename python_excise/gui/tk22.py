from tkinter import *

root = Tk()

photo = PhotoImage(file = "/Users/caturbhuja/Downloads/icon/1.gif")
theLabel = Label(root,text = 'nice to meet you too',
                 justify = LEFT,
                 image = photo,
                 compound = CENTER,
                 font=('',20),
                 fg = 'blue'
                 )
# 这里的背景色生效了。

theLabel.pack()

mainloop()

# button 组件和label大部分用法相同，唯一区别是，button能接受用户的命令
