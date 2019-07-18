# coding:utf-8
# author caturbhuja
# date   2019/7/18 5:34 PM 
# wechat chending2012 
"""
为什么案例1，2中子线程不能独立出来？不应该啊，这个到底是什么原因？

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
        super().__init__()
        self.start_thread()


class B(Base):
    pass


class C(Base):
    def start_thread(self):
        p1 = Thread(target=self.update_data())
        p2 = Thread(target=self.show_data())
        p1.start()
        p2.start()
        # 需要设置让子线程随着主线程退出而退出，否者容易造成僵尸进程。
        p1.setDaemon(True)
        p2.setDaemon(True)
        p1.join()
        p2.join()


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
    c.start_thread()
    '''
    还发现一个问题，子线程无法使用ctrl + c 退出？这个需要处理一下。
    '''