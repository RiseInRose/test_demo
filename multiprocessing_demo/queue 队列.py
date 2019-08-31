# coding:utf-8
# author caturbhuja
# date   2019/7/21 11:34 AM 
# wechat chending2012 
"""
这里是队列的用法.更详细的介绍，请看蚂蚁笔记介绍。
"""
from multiprocessing import Queue as Qa
from multiprocessing import queues

q1 = Qa(maxsize=10)
'''
q2 = queues.Queue(maxsize=10) 这个貌似需要更多函数，Qa其实就是queues.Queue的一个包装，直接看函数就知道了。
'''
# 清空队列, 这个怎么木有清空队列？python3 环境下没有清空队列，python2环境有。
# q1.queue.clear()

'''
no_wait 队列
'''
n = 0
while n < 20:
    try:
        n += 1
        q1.put_nowait(n)
    except Exception as e:
        print(e)

while 1:
    print(q1.get_nowait())
