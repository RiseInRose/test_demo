# -*- coding=utf8 -*-
# author caturbhuja
# date   2019-11-07 15:47
# wechat chending2012
import mmap
# f = open('test.txt', 'r')
# '''
# f.fileno() 文件描述符
# '''
# m = mmap.mmap(f.fileno(), )


# 方法二 使用os打开文件
import os
import time
import json
fd = os.open('test.txt', os.O_RDONLY)
# print(fd)
fi = mmap.mmap(fd, 0, access=mmap.ACCESS_COPY)
jj = json.loads(fi[0:])

while 1:
    print(jj['data'])
    time.sleep(1)
# for each in fi:
#     print(each.decode())

