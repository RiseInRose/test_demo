# -*- coding: cp936 -*-

import gevent

import time
from gevent import event  # 调用gevent的event子模块


# 三个进程需要定义三个事件event1,event2,event3，来进行12,23,31循环机制，即进程一，进程二，进程三顺序执行

def fun1(num, event1, event2):  # 固定格式

    i = 0

    while i < 10:  # 设置循环10次

        i += 1

        time.sleep(1)  # 睡眠1秒

        print('进程一：111111111')

        event2.set()  # 将event2值设为True

        event1.clear()  # 将event1值设为False

        event1.wait()  # event1等待，其值为True时才执行


def fun2(num, event2, event3):
    i = 0

    while i < 10:
        i += 1

        time.sleep(1)

        print('进程二：222222222')

        event3.set()  # 将event3值设为True

        event2.clear()  # 将event2值设为False

        event2.wait()  # event2等待，其值为True时才执行


def fun3(num, event3, event1):
    i = 0

    while i < 10:
        i += 1

        time.sleep(1)

        print('进程三：333333333')

        event1.set()

        event3.clear()

        event3.wait()


if __name__ == "__main__":  # 执行调用格式

    act1 = gevent.event.Event()  # 调用event中的Event类,用act1表示

    act2 = gevent.event.Event()

    act3 = gevent.event.Event()

    # 三个进程，act1,act2,act3

    Gevents = []  # 建立一个数列，用来存和管理进程

    g = gevent.Greenlet(fun1, 1, act1, act2)  # 调用gevent中的Greenlet子模块，用Greenlet创建进程一

    g.start()

    print('进程一启动：')

    Gevents.append(g)  # 将进程一加入到Gevents数列
    g = gevent.Greenlet(fun2, 2, act2, act3)

    g.start()

    print('进程二启动：')

    Gevents.append(g)
    g = gevent.Greenlet(fun3, 3, act3, act1)

    g.start()

    print('进程三启动：')

    print('所有进程都已启动！')

    Gevents.append(g)
    gevent.joinall(Gevents)  # 调用Greenlet中的joinall函数，将Gevents的进程收集排列