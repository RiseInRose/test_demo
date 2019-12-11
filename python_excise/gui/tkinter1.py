import tkinter as tk

app = tk.Tk()
# 实例化Tk对象
app.title("my demo")
theLabel = tk.Label(app,text = 'my secend pro!')
# label（）内容
theLabel.pack()
# pack（）自动调节尺寸，位置

app.mainloop()
# 窗口的主事件循环