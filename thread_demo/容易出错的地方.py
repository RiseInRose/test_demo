# coding:utf-8
# author caturbhuja
# date   2019/7/18 6:52 PM 
# wechat chending2012

"""
创建线程时，需要输入函数名称，如果输入函数后面添加括号，函数会被直接执行。
"""


#正确写法
def start_thread(self):
    p = Thread(target=self.update_data)
    p.start()
    # p.join()


#错误写法
def start_thread(self):
    p = Thread(target=self.update_data())
    p.start()
    # p.join()
