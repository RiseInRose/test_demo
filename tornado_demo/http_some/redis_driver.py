# -*- coding:utf8 -*-
# author caturbhuja
# date   2019-07-07 17:17
# wechat chending2012
import aioredis
"""
aioredis
python 文档
https://aioredis.readthedocs.io/en/v1.2.0/

下面需要写一个orm 为了驱动异步驱动redis。
"""
from tornado.ioloop import IOLoop


class Driver:
    def __init__(self, url, port):
        self.conn = None
        self.ioloop = IOLoop.current()
        self.url = url
        self.port = port
        self.ioloop.start(self.connects())

    async def connects(self):
        """
        :param method: get, set,
        :param key:
        :return:
        """
        self.conn = await aioredis.create_pool((self.url, self.port))
        val = await self.conn.execute(method, key)


if __name__ == '__main__':
    driver = Driver('localhost', 6379)