# -*- coding:utf8 -*-
# author caturbhuja
# date   2019-07-18 21:18
# wechat chending2012
"""
当捕获到键盘打断时，程序会被中止。这个用在哪里？
在运行多线程程序时，有时出现，无法使用键盘打断整个程序，即使添加子线程守护进程也没有用。
这时候，这个打断程序就派上用场了。
todo
"""
# 方法1


def main():
    # whatever your app does.
    pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # do nothing here
        pass
'''
方法2：
# 使用信号来判断被打断
import signal
import sys
import time

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print 'Press Ctrl+C'
while True:
    time.sleep(1)

'''