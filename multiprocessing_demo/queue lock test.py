# coding:utf-8
# author caturbhuja
# date   2019/8/7 11:33 AM 
# wechat chending2012 
from multiprocessing import Process, Queue
import time


def put():
    print('start put')
    cnt = 0
    while True:
        try:
            q.put_nowait(cnt)
            cnt += 1
            print('put:{}'.format(cnt))
            # time.sleep(0.01)
        except Exception as e:
            # print(e)
            # print('queue is full')
            # time.sleep(0.01)
            pass


def get(name='get1'):
    print('start get')
    while True:
        try:
            print("{}:{}".format(name, q.get_nowait()))
            time.sleep(0.1)
        except Exception as e:
            print(e)
            print('queue is empty')
            time.sleep(1)


def get2(name='get2'):
    print('start get2')
    while True:
        try:
            print("{}:{}".format(name, q.get_nowait()))
            with open('qw') as e:
                e.read()
            time.sleep(0.1)
        except Exception as e:
            print(e)
            print('queue is empty or some error')
            time.sleep(0.1)


q = Queue(1000)
pro_num = 4
pro_dict = dict()

p1 = Process(target=put)
for p in range(pro_num):
    pro_dict["p"+str(p)] = Process(target=get, args=(p, ))


p1.start()
for p in range(pro_num):
    pro_dict["p" + str(p)].start()

Process(target=get2).start()
