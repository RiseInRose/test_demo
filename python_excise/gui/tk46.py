from tkinter import *
'''
TKinter3种布局方式，这里选用grid，使用表格布局。
加入自动将密码转换成*
加入验证输入合法性。
加入隐藏方法，可以输入参数。
用上面所学，实现一个加法计算器。
'''
'''
frame 是框架的嵌套关系，需要指定某个组件在某个框架内部，复合某种定位关系。
如果不用frame，可以直接使用root。（Tk（）实例化后的对象。）

'''
root = Tk()
frame = Frame(root)
frame.pack(padx = 10,pady = 10)

v1 = StringVar()
v2 = StringVar()#一个存放账号，一个存放密码
v3 = StringVar()


def check_account(content):
    return content.isdigit()
# 判断是否是数字，是的话返回True

def test2():
    print('我被调用了。。。。')
    return True


check_account_CMD = root.register(check_account)
#这里需要将check_account封装，才能让其识别后面的参数。

e1 = Entry(frame,textvariable = v1,validate = 'key',
           validatecommand = (check_account_CMD,'%P'),invalidcommand = test2,width = 10)
# 设置失去焦点（focuseout）时验证，调用check_account函数。
# %P输入框发生任何改变，得到输入框内部的值,%W相当与程序设计的句柄，%v检查时调用的方法。
Label(frame,text = '+').grid(row = 0,column = 1)#第0行，第1列

e2 = Entry(frame,textvariable = v2,validate = 'key',
           validatecommand = (check_account_CMD,'%P'),invalidcommand = test2,width = 10)

Label(frame,text = '=').grid(row = 0,column = 3)


e3 = Entry(frame,state = 'readonly',textvariable = v3,width = 10)
#获取输入的内容并存入，show后面定义显示样子。

e1.grid(row = 0,column = 0,padx = 2,pady = 5)
e2.grid(row = 0,column = 2,padx = 2,pady = 5)
e3.grid(row = 0,column = 4,padx = 2,pady = 5)

def show():
    pass

def count():
    v = int(e1.get())+ int(e2.get())
    v3.set(v)

def delete():
    v1.set('')
    v2.set('')

Button(frame,text = '确定',width=10,command = count).\
    grid(row = 1,column = 0,sticky = W,padx = 2,pady = 5)
Button(frame,text = '清零',width=10,command = delete).\
    grid(row = 1,column = 1,sticky = W,padx = 2,pady = 5)
Button(frame,text = '退出',width=10,command = root.quit).\
    grid(row = 1,column = 2,sticky = E,padx = 2,pady = 5)



mainloop()