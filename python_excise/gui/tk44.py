from tkinter import *
root = Tk()
'''
TKinter3种布局方式，这里选用grid，使用表格布局。
加入自动将密码转换成*
加入验证输入合法性。
'''

Label(root,text = "账号：").grid(row = 0,column = 0)#第0行，第0列
Label(root,text = '密码：').grid(row = 1,column = 0)

v1 = StringVar()
v2 = StringVar()#一个存放账号，一个存放密码

def check_account():
    if e1.get() == 'chending':
        print('yes')
        return True
    else:
        print('wrong')
        e1.delete(0,END)
        return False

def test2():
    print('我被调用了。。。。')
    return True

e1 = Entry(root,textvariable = v1,validate = 'focusout',
           validatecommand = check_account,invalidcommand = test2)
# 设置失去焦点（focuseout）时验证，调用check_account函数。

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