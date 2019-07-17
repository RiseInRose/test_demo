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
问题1：在class中，Queue是否被共享。
答：会被共享，

问题2：self字典中的所有内容都可以被共享？
答：会被共享，

问题3：python多进程，到底多进程了什么东西？
答：pass

问题4：multiprocessing 的Queue 一出来，是否需要初始化？
答：这个是初始化好的，如果有2个以上的引用，会导致程序卡住（短时间内不报错）。
'''


class Am:
    def __init__(self, queue_lens):
        self.queue = Queue(queue_lens)
        self.cnt = 0

    def put(self):
        print 'start put'
        while True:
            if self.queue.full():
                print 'queue is full'
                time.sleep(0.5)
                continue
            else:
                self.queue.put(self.cnt)
                self.cnt += 1
                time.sleep(0.1)

    def get(self):
        print 'start get'
        while True:
            if self.queue.empty():
                print 'queue is empty'
                time.sleep(0.1)
            else:
                print self.queue.get()
                # print self.cnt
                time.sleep(1)


if __name__ == '__main__':

    # ----------测试问题1，2，3-----------
    # a = Am(10)
    # pro_num = 8
    # pro_dict = dict()

    # p1 = Process(target=a.put)
    # for p in range(pro_num):
    #     pro_dict["p"+str(p)] = Process(target=a.get)
    #
    # p1.start()
    # for p in range(pro_num):
    #     pro_dict["p" + str(p)].start()

    # ---------测试问题4-------------
    a = Queue(3)
    b = Queue(2)
    a.put(1)
    b.put(2)
    a.get()
    a.get()
