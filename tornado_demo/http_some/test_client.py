# -*- coding:utf8 -*-
# author caturbhuja
# date   2019-07-07 13:52
# wechat chending2012
"""
这个样例用来测试服务器的异步特性

"""
import requests
import threading
from time import time

url = 'http://127.0.0.1:8888/{}'


def my_request(key):
    print(requests.get(url.format(key)).content)


class MyThread(threading.Thread):
    def __init__(self, key):
        super().__init__()
        self.key = key

    def run(self):
        """"""
        '''
        开启线程锁，会让线程单独一个一个运行。浪费了时间。
        '''
        # 获取锁，用于线程同步
        # threadLock.acquire()
        my_request(self.key)
        # 释放锁，开启下一个线程
        # threadLock.release()


# threadLock = threading.Lock()

thread_dict = dict()
num = 10
t = time()
key = 'async'
# key = 'sync'

# 创建新线程
print("开启线程")
for each in range(num):
    thread_dict["t{}".format(each)] = MyThread(key)

for each in range(num):
    thread_dict["t{}".format(each)].start()

# 等待所有线程完成
for each in range(num):
    thread_dict["t{}".format(each)].join()

print("退出主线程")
print("it cost {}".format(time() - t))
