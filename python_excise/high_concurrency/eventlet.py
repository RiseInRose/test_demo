'''
这里出现一个bug，代码没有问题，但是放到ide中执行就会报错，说没有这个参数。
代码直接放到python解释器是可以执行的。
只要加入multiprocessing模块，程序基本就不会报错。
'''

import eventlet
import requests
import pymongo
import time,multiprocessing
headers2 = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection':'keep-alive'
}
i = time.strftime("%d/%m/%Y").split('/')
times = str(i[2])+str(i[1])+str(i[0])
search_key = "python"
client = pymongo.MongoClient('localhost', 27017,connect=False)
NiceJob = client.NiceJob
client_name = search_key + 'Job_' + times
url = []

urls = NiceJob[client_name].find()
for each in urls:
    url.append(each['job_url'])

def open_url(url):
    r = requests.get(url, headers=headers2,timeout=30)
    print(r.status_code)

import datetime

def opurls(url):
    pool = eventlet.GreenPool(200)
    pool.imap(open_url,url)

    print('opurls')


if __name__ == '__main__':
    start = datetime.datetime.now()
    pool2 = multiprocessing.Pool(processes=16)
    for each in url:
        print(each)
        pool2.apply_async(opurls,(each,))
    pool2.close()
    pool2.join()
    print("All process done.")

    end = datetime.datetime.now()
    print(end - start)

