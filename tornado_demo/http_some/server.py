# -*- coding:utf8 -*-
# author caturbhuja
# date   2019-07-07 10:57
# wechat chending2012
"""
1 tornado 使用异步功能 11  成功，直接使用async和await关键字即可
2 tornado 使用异步redis 11
3 tornado 使用异步mysql 11
4 tornado 使用异步mongo 1
5 tornado 使用多核 1
tornado 文档 https://tornado-zh.readthedocs.io/zh/latest/

异步http_server 文档
https://tornado-zh.readthedocs.io/zh/latest/httpserver.html
"""

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.httpserver import HTTPServer
import asyncio
import time
'''
阅读tornado IOLoop本身的文档，发现了python3 asyncIO，python2 采用epoll。于是提出问题？
asyncIO与epoll哪个效率高？

查阅资料：结论如下
Tornado的作者也指出过，他的测试过程中，使用asyncio和tornado自带的epoll事件循环性能差不多。并且tornado5.0会考虑完全吸纳asyncio。
在此之前，使用tornado无论是使用自带的事件循环还是asyncio或者uvloop，在性能方面上都差不大。需要兼容数据库或http库的时候，
使用uvloop的驱动方式，兼容性最好~

参考文档：https://www.jianshu.com/p/6d6fa94a01ef

关于连接数据库，由于是异步，所以数据库连接数会随着请求量的增加而增加。所以可能会出现too many connections。所以，采用连接词的方式，
能更大的发挥数据库的性能。

需要确定redis，mysql，mongodb等数据库支持的最大连接数。
redis： 2.6版本后默认10000，可以设置成 100k 。 
mysql： 5.6版本默认151 上限为100k （实际可能处理的是151左右）
mongodb：默认1000,000 实际可能处理远远小于这个数目。 

修改最大连接数时，都需要顺带修改linux打开最大文件数目（默认为1024）。

关于网络模型：
redis默认采用异步网络库处理。
mysql

mongodb 的服务模型是每个网络连接由一个单独的线程来处理，每个线程配置了1MB的栈空间。当网络连接数太多时，过多的线程会导致上下文切换
开销变大，同时内存开销也会上涨。
mongodb 在处理短链接情况时，并不优雅，3000链接即可跑满24core的cpu。所以推荐使用长连接。但是需要正确的配置客户端？

参考：
redis：
https://www.cnblogs.com/zt007/p/9510795.html
redis 使用shell查看最大连接数 https://blog.csdn.net/secretx/article/details/73498148

mysql
https://www.cnblogs.com/zhang-ding-1314/p/9564311.html 
https://www.cnblogs.com/liaojie970/p/6888311.html

mongodb：
http://www.mongoing.com/archives/3145
https://yq.aliyun.com/articles/54021?spm=5176.group11.0.0.o3PfTi

'''


class async_test_handler(RequestHandler):
    """"""
    '''
    测试结果，只需要在继承的get内部添加async，即可实现tornado的协程
    '''
    async def gg(self):
        print('1')
        await asyncio.sleep(1)
        print('2')
        '''
        这个为了测试协程是否会跳过，执行后面的程序。
        结论：程序会在2 位置等待结果，然后再次执行。
        '''
        await asyncio.sleep(3)
        print('3')
        return 'nices'

    async def get(self):
        data = await self.gg()
        self.write(data)


class sync_test_handler(RequestHandler):
    def get(self):
        time.sleep(1)
        self.write("nice")


class async_test_redis(RequestHandler):
    async def get_data_from_redis(self):
        pass

    async def get(self):
        data = await self.get_data_from_redis()
        self.write(data)


if __name__ == '__main__':
    application = Application(
        [
            (r"/async", async_test_handler),
            (r"/sync", sync_test_handler),
            (r"/async_redis", async_test_redis),
        ]
    )
    server = HTTPServer(application)
    server.listen(8888)
    ioLoop = IOLoop.current()
    ioLoop.start()
