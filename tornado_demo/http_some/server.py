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


class async_test_handler(RequestHandler):
    """"""
    '''
    测试结果，只需要在继承的get内部添加async，即可实现tornado的协程
    '''
    async def gg(self):
        await asyncio.sleep(1)
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
