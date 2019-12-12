from tkinter import *

root = Tk()

textLabel = Label(root,text = "nice to see，\n you again!",
                  justify = LEFT)

# 支持换行 ,左对齐
textLabel.pack()

photo = PhotoImage(file = '/Users/caturbhuja/Downloads/icon/1.gif')
# bug这里使用gif图片时，图片不会动。
imgLabel = Label(root,image=photo)
imgLabel.pack()

mainloop()