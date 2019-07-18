# coding:utf-8
# author caturbhuja
# date   2019/7/18 5:43 PM 
# wechat chending2012 
"""
目前创建线程有如下2中方法
参考网址：
https://www.cnblogs.com/wongbingming/p/9028851.html
https://www.cnblogs.com/cnkai/p/7504980.html
https://www.cnblogs.com/wang-can/p/3580457.html

"""
'''
# 方法1
from threading import Thread  # 创建线程的模块
def task(name):
    print(name)

if __name__ == '__main__':
    # 开启线程  参数1：方法名(不要带括号)   参数2：参数（元祖）      返回对象
    p = Thread(target=task, args=('线程1',))
    p.start()  # 只是给操作系统发送了一个就绪信号，并不是执行。操作系统接收信号后安排cpu运行
    print('主')
'''
'''
# 方法2 按照类的方法
from threading import Thread  # 创建线程的模块

class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):  # 固定名字run ！！！必须用固定名
        print(self.name)

if __name__ == '__main__':  # 必须要这样启动 
    p = MyThread('子线程1')
    p.start()
    print('主)

'''

'''
常用方法：
currentThread() 取线程对象
getName() 取线程名
setName(‘设置线程名’) 取线程对象
isAlive() # 线程是否存活
'''

from threading import Thread
from threading import currentThread  # 获取当前线程对象的 对象
import time


def task():
    print('%s is runing' %currentThread().getName())  # 获取线程名
    time.sleep(2)
    print('%s is down' % currentThread().getName())


if __name__ == '__main__':
    t = Thread(target=task, name='这里设置子线程初始化名')
    t.start()
    t.setName('设置线程名')  # ！！！！
    t.join()  # 等待子线程运行结束
    # currentThread() 等同于 线程对象t  所以获取线程名也可以t.getName()
    print('主线程', currentThread().getName())
    # 但在主线程内（并没有线程对象）要获取线程名必须用 currentThread().getName()
    t.isAlive()  # 线程是否存活！ 查看线程对象是否存活
