# -*- coding: cp936 -*-

import gevent

import time
from gevent import event  # ����gevent��event��ģ��


# ����������Ҫ���������¼�event1,event2,event3��������12,23,31ѭ�����ƣ�������һ�����̶���������˳��ִ��

def fun1(num, event1, event2):  # �̶���ʽ

    i = 0

    while i < 10:  # ����ѭ��10��

        i += 1

        time.sleep(1)  # ˯��1��

        print('����һ��111111111')

        event2.set()  # ��event2ֵ��ΪTrue

        event1.clear()  # ��event1ֵ��ΪFalse

        event1.wait()  # event1�ȴ�����ֵΪTrueʱ��ִ��


def fun2(num, event2, event3):
    i = 0

    while i < 10:
        i += 1

        time.sleep(1)

        print('���̶���222222222')

        event3.set()  # ��event3ֵ��ΪTrue

        event2.clear()  # ��event2ֵ��ΪFalse

        event2.wait()  # event2�ȴ�����ֵΪTrueʱ��ִ��


def fun3(num, event3, event1):
    i = 0

    while i < 10:
        i += 1

        time.sleep(1)

        print('��������333333333')

        event1.set()

        event3.clear()

        event3.wait()


if __name__ == "__main__":  # ִ�е��ø�ʽ

    act1 = gevent.event.Event()  # ����event�е�Event��,��act1��ʾ

    act2 = gevent.event.Event()

    act3 = gevent.event.Event()

    # �������̣�act1,act2,act3

    Gevents = []  # ����һ�����У�������͹������

    g = gevent.Greenlet(fun1, 1, act1, act2)  # ����gevent�е�Greenlet��ģ�飬��Greenlet��������һ

    g.start()

    print('����һ������')

    Gevents.append(g)  # ������һ���뵽Gevents����
    g = gevent.Greenlet(fun2, 2, act2, act3)

    g.start()

    print('���̶�������')

    Gevents.append(g)
    g = gevent.Greenlet(fun3, 3, act3, act1)

    g.start()

    print('������������')

    print('���н��̶���������')

    Gevents.append(g)
    gevent.joinall(Gevents)  # ����Greenlet�е�joinall��������Gevents�Ľ����ռ�����