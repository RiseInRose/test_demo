# coding=utf-8
# author caturbhuja
# date   2019/9/24 10:09 AM 
# wechat chending2012 

with open('removed.csv', 'r') as files:
    f = files.readlines()

for each in f:
    try:
        user_id = int(each.strip())
        print(user_id)
    except ValueError:
        pass
