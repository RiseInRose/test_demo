import tkinter as tk

class APP:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side = tk.LEFT,padx = 10,pady = 10)
        # 设置，左边靠齐，x,y，分别是10距离。

        self.hi_there = tk.Button(frame,text = 'Hello,world', bg = 'yellow', fg='red',command = self.say_hi)
        # 这里设置的背景色无效？后来测试了，应该是python版本问题，或者mac系统问题。
        self.hi_there.pack()

    def say_hi(self):
        print('hi,nice to meet you!')

root = tk.Tk()
app = APP(root)

root.mainloop()