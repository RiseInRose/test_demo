# -*- coding=utf8 -*-
# @author caturbhuja@foxmail.com
# date   2019/11/22 17:30
# @wechat chending2012
"""
单例模式
  单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，
某个类只能出现一个实例时，单例对象就能派上用场。

  比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，
有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，
而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。

参考网站 https://www.cnblogs.com/huchong/p/8244279.html
"""


# ----------------------------1 模块导入 -------------------------------
# 模块导入，mysingleton.py
class Singleton(object):
    def foo(self):
        pass


singleton = Singleton()

# 在其他文件中导入这个例子，这个即为单例模式
# from a import singleton


# ----------------------------2 使用装饰器-------------------------------
# 使用装饰器，这个装饰器能保证，被装饰的类，只有一个实例。可以在工程中大规模使用。
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)


# ----------------------------3 类装饰器-------------------------------
# 使用类 这个需要加锁，否则在多线程时，容易出问题。目前这个作为了解。
import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


def task(arg):
    obj = Singleton.instance()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
time.sleep(20)
obj = Singleton.instance()
print(obj)

# ----------------------------4 重写 __new__ -------------------------------
# 基于__new__方法实现（推荐使用，方便）佳能项目代码，使用的就是这个。
'''
我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），
实例化对象；然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式
'''
# 实例化


# ----------------------------5  使用元类  -------------------------------
# 基于metaclass方式实现，这个后面复习元类的时候再说吧
'''
1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
'''



