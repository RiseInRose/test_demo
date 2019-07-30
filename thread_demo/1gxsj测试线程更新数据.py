# coding:utf-8
# author caturbhuja
# date   2019/7/18 5:34 PM 
# wechat chending2012 
"""
这个案例，主要测试:
1. 线程去更新的数据，能够共享给主线程？
2. 线程能否共享到主线程的初始化数据库连接？
答：都可以

3 join的作用？
答：如果需要子线程等待主线程执行完才停止，需要添加join，否则，可以不添加join。

注意，线程的参数，需要以元组的方式添加
"""
from threading import Thread
import time
import redis
import signal
import sys


def signal_handler():
    sys.exit(0)


class Base:
    def __init__(self):
        self.data = ''
        self.conn = redis.Redis(host="127.0.0.1", port=6379)

    def update_data(self):
        while 1:
            with open('./data.txt') as f:
                b = f.read()
            self.data = b
            print('子线程值：{}'.format(b))
            time.sleep(3)

    @staticmethod
    def set_data_by_files():
        while 1:
            with open('./data.txt', 'w') as f:
                i = input('请输入：')
                f.write(i)

    def update_data_from_redis(self):
        while 1:
            self.data = self.conn.get("x1")
            print('子线程值：{}'.format(self.data))
            time.sleep(3)

    def set_data_from_redis(self):
        while 1:
            i = input('请输入：')
            self.conn.set("x1", i+'\n', ex=5)  # ex代表seconds，px代表ms

    def show_data(self):
        while 1:
            print('主线程值：{}'.format(self.data))
            time.sleep(3)

    def start_thread(self):
        """
        下面这个是错误写法，函数后面添加括号，会导致这个函数直接被执行，因为内部有while 1，会导致子线程根本无法创建成功
        p = Thread(target=self.update_data())
        """
        p = Thread(target=self.update_data)
        p.start()
        p.join()


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
        p1 = Thread(target=self.update_data)
        p2 = Thread(target=self.show_data)
        print('--start--')
        p1.start()
        p2.start()


class D(Base):
    def __init__(self):
        super().__init__()
        self.start_thread()

    def start_thread(self):
        p1 = Thread(target=self.update_data_from_redis)
        p2 = Thread(target=self.show_data)
        p3 = Thread(target=self.set_data_from_redis)
        print('--start--')
        p1.start()
        p2.start()
        p3.start()


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
    因为线程在输入函数，后面添加了括号，导致，创建线程时函数被执行。而函数本身是个循环，导致。。。。。
    '''
    # try:
    #     c = C()
    # except KeyboardInterrupt:
    #     pass
    # signal.signal(signal.SIGINT, signal_handler)
    '''
    '''
    try:
        d = D()
    except KeyboardInterrupt:
        pass
