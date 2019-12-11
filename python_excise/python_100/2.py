# import collections
# str1=['a','b','c','d','a','a','b','c']
# m = collections.Counter(str1)
# print(str1)
# print(m)
# print(m['a'])


import eventlet
from eventlet.green import urllib2

urls = [
    "http://www.google.com/intl/en_ALL/images/logo.gif",
    "https://wiki.secondlife.com/w/images/secondlife.jpg",
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
]


def fetch(url):
    return urllib2.urlopen(url).read()


pool = eventlet.GreenPool(200)  # 创建绿色线程池对象，可以指定数量

for body in pool.imap(fetch, urls):  # 协程根据指定要执行的函数依次执行获得url的信息
    print("got body", len(body))