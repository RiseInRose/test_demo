# coding:utf-8
# author caturbhuja
# date   2019/7/18 5:34 PM 
# wechat chending2012 
"""
上一个案例，使用类测试，子线程不是完全独立出去的，难道是子线程使用方法不对？
这个案例，直接使用函数。来测试下.
结果：
子线程不被主线程独立出去，和使用方法无关，应该和载入的模块有关。
"""
from threading import Thread
import time

data = ''


def update_data():
    while 1:
        with open('./data.txt') as f:
            b = f.read()
        global data
        data = b
        print('子线程值：{}'.format(b))
        time.sleep(3)


def update_data_from_redis():
    pass


def show_data():
    while 1:
        print('主线程值：{}'.format(data))
        time.sleep(3)


if __name__ == '__main__':
    p1 = Thread(target=update_data())
    p2 = Thread(target=show_data())
    p1.start()
    p2.start()
