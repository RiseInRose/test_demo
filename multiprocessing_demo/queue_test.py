# coding:utf-8
# author caturbhuja
# date   2019/7/11 11:18 AM 
# wechat chending2012
"""
这个是python2.7环境下，多进程队列模式的demo
"""
import time
from multiprocessing import Process, Queue

'''
# import Queue
Queue 在多线程中有效，但是在多进程，无效。因为多进程中的内存不共享。
在多进程中会出现，一个queue满了，另外一个进程的queue是空的。

问题2：join 会造成阻塞吗？导致后面的程序不被执行？
答：join 会造成阻塞，所以join需要放到最后。
'''


def put():
    print 'start put'
    cnt = 0
    while True:
        if q.full():
            print 'queue is full'
            time.sleep(0.5)
            continue
        else:
            q.put(cnt)
            cnt += 1
            time.sleep(0.1)


def get():
    print 'start get'
    while True:
        if q.empty():
            print 'queue is empty'
            time.sleep(0.1)
        else:
            print q.get()
            time.sleep(1)


q = Queue(10)
pro_num = 10
pro_dict = dict()

p1 = Process(target=put)
for p in range(pro_num):
    pro_dict["p"+str(p)] = Process(target=get)


p1.start()
for p in range(pro_num):
    pro_dict["p" + str(p)].start()

'''

'''