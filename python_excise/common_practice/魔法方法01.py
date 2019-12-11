class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    # __init__ 返回值一定要是None,否则出错。
    # __init__ 表示初始化对象，self.x 表示实例化后的东西，x表示参数。
    def getPeri(self):
        return (self.x +self.y)*2
    def getArea(self):
        return self.x*self.y

class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return  str.__new__(cls,string)
'''
__new__(cls[,...])是类里面最先执行的，而不是init。这个必须要返回值
使用在，继承不可改变的类时，修改最先的参数。
__new__(cls[,...])是python的构造器。
不同于__del__(self)是python的析构器。

当对象被销毁时，这个__del__(self)方法会自动被调用。python垃圾回收机制

在类，实例化参数时，所有的参数会自动进__init__
__init__(self,param1,param2....)

'''

class C:
    def __index__(self):
        print('i am __init__,i am working!')
    def __del__(self):
        print('i am __del__,i am working!')

'''
公有和私有，

在类定义参数的前面加上 __,如 __name 这样就变成了私有。
要访问，就只能从内部访问。可以在内部写入函数，访问。

'''

class Persion:
    __myname = 'caturbhuja'
    name = 'mains'
    def getmyName(self):
        return self.__myname


if __name__ == '__main__':
    p = Persion()
    print(p.name)
    print(p.getmyName())


    # i = Rectangle(3,4)
    # print(i)
    # print(i.getArea())
    # print(i.getPeri())

    # k = 'nice job!'
    # print(CapStr(k))

    # c1 = C()
    # print(c1)


