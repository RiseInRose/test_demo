# coding:utf-8
# author caturbhuja
# date   2019/7/11 2:50 PM 
# wechat chending2012 
"""
在网域网络公司开发高并发服务器时，发现，有时候，写入到队列的信息，只能写入，但消费的很少。当时感觉单核上，线程应该上均分的，
但是现在想来，可能出现，queue一直被写线程抢占，导致读线程没有机会执行。
现在来设计案例测试下。
"""
from threading import Thread
from queue import Queue
import time
q = Queue(10)


def put():
    cnt = 0
    while 1:
        # cnt += 1
        # q.put(cnt)
        # print("put cnt:{}".format(cnt))

        q.put(1)
        print("put cnt")


def get():
    while 1:
        print("get cnt:{}".format(q.get()))
        # time.sleep(0.001)


if __name__ == '__main__':
    Thread(target=put).start()
    Thread(target=get).start()

'''
观察结果，在mac的cpu会有时间片的概念。每个子线程会分配到相同的时间片。
'''
