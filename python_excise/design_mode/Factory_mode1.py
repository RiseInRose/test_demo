# -*- coding=utf8 -*-
# author caturbhuja
# date   2019/11/21 15:39
# wechat chending2012
"""工厂模式
工厂模式，顾名思义就是我们可以通过一个指定的“工厂”获得需要的“产品”，在设计模式中主要用于抽象对象的创建过程，
让用户可以指定自己想要的对象而不必关心对象的实例化过程。这样做的好处是用户只需通过固定的接口而不是直接去调用类的实例化方法来获得一个对
象的实例，隐藏了实例创建过程的复杂度，解耦了生产实例和使用实例的代码，降低了维护的复杂性。
参考文档：https://segmentfault.com/a/1190000013053013
"""

"""
简单工厂模式
"""


class Mercedes(object):
    """梅赛德斯
    """
    def __repr__(self):
        return "Mercedes-Benz"


class BMW(object):
    """宝马
    """
    '''
    1. 区别
    __repr__ __str__ 功能都是实现str 字符的转化，__str__ 返回结果可读性强，__repr__返回结果更准确
    str(today)  2019-11-21
    repr(today) datetime.date(2019, 11, 21)
    
    2 每个类最好都有一个 __repr__ 方法
    
    def __repr__(self):
        return f'class name is {self.__class__.__name__}'
    
    3 在print 时，优先调用 __str__ 这个方法。
    '''
    def __repr__(self):
        return "BMW"

    def __str__(self):
        return "create a BMW Factory !"


class SimpleCarFactory(object):
    """简单工厂
    """
    @staticmethod
    def product_car(name):
        if name == 'mb':
            return Mercedes()
        elif name == 'bmw':
            return BMW()


c1 = SimpleCarFactory.product_car('mb')
c2 = SimpleCarFactory.product_car('bmw')
print(c1)
print(c2)

"""工厂方法
虽然有了一个简单的工厂，但在实际使用工厂的过程中，我们会发现新问题：如果我们要新增一个“产品”，例如Audi的汽车，
我们除了新增一个Audi类外还要修改SimpleCarFactory内的product_car方法。这样就违背了软件设计中的开闭原则[1]，
即在扩展新的类时，尽量不要修改原有代码。所以我们在简单工厂的基础上把SimpleCarFactory抽象成不同的工厂，
每个工厂对应生成自己的产品，这就是工厂方法。
"""

import abc


class AbstractFactory(object):
    """抽象工厂
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass


class MercedesFactory(AbstractFactory):
    """梅赛德斯工厂
    """
    def product_car(self):
        return Mercedes()


class BMWFactory(AbstractFactory):
    """宝马工厂
    """
    def product_car(self):
        return BMW()
