# -*- coding=utf8 -*-
# author caturbhuja
# date   2019/11/21 15:39
# wechat chending2012
"""抽象工厂
工厂方法虽然解决了我们“修改代码”的问题，但如果我们要生产很多产品，就会发现我们同样需要写很多对应的工厂类。
比如如果MercedesFactory和BMWFactory不仅生产小汽车，还要生产SUV，那我们用工厂方法就要再多构造两个生产SUV的工厂类。
所以为了解决这个问题，我们就要再更进一步的抽象工厂类，让一个工厂可以生产同一类的多个产品，这就是抽象工厂。具体实现如下：
参考文档：https://segmentfault.com/a/1190000013053013
文档2：https://www.runoob.com/design-pattern/abstract-factory-pattern.html
"""

''' 结论
初学设计模式时会对三种工厂模式的实际应用比较困惑，其实三种模式各有优缺点，应用的场景也不尽相同：

简单工厂
简单工厂模式适用于需创建的对象较少，不会造成工厂方法中的业务逻辑太过复杂的情况下，而且用户只关心那种类型的实例被创建，
并不关心其初始化过程时，比如多种数据库(MySQL/MongoDB)的实例，多种格式文件的解析器(XML/JSON)等。

工厂方法模式
工厂方法模式继承了简单工厂模式的优点又有所改进，其不再通过一个工厂类来负责所有产品的创建，而是将具体创建工作交给相应的子类去做，
这使得工厂方法模式可以允许系统能够更高效的扩展。实际应用中可以用来实现系统的日志系统等，比如具体的程序运行日志，网络日志，
数据库日志等都可以用具体的工厂类来创建。

抽象工厂模式
抽象工厂模式在工厂方法基础上扩展了工厂对多个产品创建的支持，更适合一些大型系统，比如系统中有多于一个的产品族，
且这些产品族类的产品需实现同样的接口，像很多软件系统界面中不同主题下不同的按钮、文本框、字体等等。
'''

"""
抽象工厂模式
"""

import abc


# 两种小汽车
class Mercedes_C63(object):
    """梅赛德斯 C63
    """

    def __repr__(self):
        return "Mercedes-Benz: C63"


class BMW_M3(object):
    """宝马 M3
    """

    def __repr__(self):
        return "BMW: M3"


# 　两种SUV
class Mercedes_G63(object):
    """梅赛德斯 G63
    """

    def __repr__(self):
        return "Mercedes-Benz: G63"


class BMW_X5(object):
    """宝马 X5
    """

    def __repr__(self):
        return "BMW: X5"


class AbstractFactory(object):
    """抽象工厂
    可以生产小汽车外，还可以生产SUV
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass

    @abc.abstractmethod
    def product_suv(self):
        pass


class MercedesFactory(AbstractFactory):
    """梅赛德斯工厂
    """

    def product_car(self):
        return Mercedes_C63()

    def product_suv(self):
        return Mercedes_G63()


class BMWFactory(AbstractFactory):
    """宝马工厂
    """

    def product_car(self):
        return BMW_M3()

    def product_suv(self):
        return BMW_X5()


if __name__ == '__main__':
    c1 = MercedesFactory().product_car()
    s1 = MercedesFactory().product_suv()
    print(c1, s1)
    s2 = BMWFactory().product_suv()
    c2 = BMWFactory().product_car()
    print(c2, s2)
