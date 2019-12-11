from tkinter import *

def callback():
     var.set('Nice job,You do it!')


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("nice to see you again!")
textLabel = Label(frame1,
                  textvariable = var,
                  justify = LEFT
                  )
# text 与textvariable 区别？我在将文字改成var后，使用text不能显示。
# 加了textvariable 后，能正常显示，textvariable能自动刷新更改文字。详见http://bbs.fishc.com/thread-59087-1-1.html

# 支持换行 ,左对齐
textLabel.pack(side = LEFT)

photo = PhotoImage(file = '/Users/caturbhuja/Downloads/icon/1.gif')
# bug这里使用gif图片时，图片不会动。
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side = RIGHT)

theButton = Button(frame2, text = 'hit me',command = callback)
theButton.pack()

frame1.pack(padx = 10,pady = 10)
frame2.pack(padx = 10,pady = 10)
# 第一次时，没有加这两句，没办法显示？为什么？

mainloop()