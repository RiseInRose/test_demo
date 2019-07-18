# coding:utf-8
# author caturbhuja
# date   2019/7/18 5:34 PM 
# wechat chending2012 
"""
这个案例，主要测试:
1. 线程去更新的数据，能够共享给主线程？
2. 线程能否共享到主线程的初始化数据库连接？

注意，线程的参数，需要以元组的方式添加
"""
from threading import Thread
import time


class Base:
    def __init__(self):
        self.data = ''

    def update_data(self):
        while 1:
            with open('./data.txt') as f:
                b = f.read()
            self.data = b
            print('子线程值：{}'.format(b))
            time.sleep(3)

    def update_data_from_redis(self):
        pass

    def show_data(self):
        while 1:
            print('主线程值：{}'.format(self.data))
            time.sleep(3)

    def start_thread(self):
        p = Thread(target=self.update_data())
        p.start()
        # p.join()


class A(Base):
    def __init__(self):
        self.start_thread()
        super().__init__()


class B(Base):
    pass


class C(Base):
    def __init__(self):
        self.start_thread()
        super().__init__()

    def start_thread(self):
        print('---------')
        p1 = Thread(target=self.update_data())
        print('22222222')
        p2 = Thread(target=self.show_data())
        print('--start--')
        p1.start()
        print('p1 start')
        p2.start()
        print('p2 start')


if __name__ == '__main__':
    '''
    在类内部开启子线程结果：主线程会在初始化的时候被卡住。
    '''
    # a = A()
    # a.show_data()
    '''
    在类外部开启子线程结果：主线程同样会被卡住。
    '''
    # b = B()
    # Thread(target=b.update_data()).start()
    # b.show_data()
    '''
    两个都使用子线程，这样使用线程是对的吗？为什么前面的线程会把后面的卡住？
    '''
    c = C()
