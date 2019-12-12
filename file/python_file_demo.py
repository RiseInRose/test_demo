# coding:utf-8
# author caturbhuja
# date   2019/8/16 10:16 AM 
# wechat chending2012 
"""
写模式 w  只能写，不能读，写会清空原来文件，当文件不存在会创建新文件
写读模式 w+   可读可写，其他同上



追加模式 a
追加读模式 a+
"""

import json
i = json.dumps({1: 3})
j = json.dumps({1: 4})

with open('1.txt', 'a') as f:
    f.write(i+'\n')
    f.write(j+'\n')
