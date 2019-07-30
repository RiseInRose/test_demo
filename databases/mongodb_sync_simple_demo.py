# coding:utf-8
# author caturbhuja
# date   2019/7/29 9:59 AM 
# wechat chending2012 
from pymongo import MongoClient

"""
介绍：这个demo简单介绍 python连接mongodb。
"""
# 普通连接
client = MongoClient('localhost', 27017)
'''
client = MongoClient('mongodb://localhost:27017/')
# 密码连接
client = MongoClient('mongodb://username:password@localhost:27017/dbname')
'''

db = client.zfdb
# db = client['zfdb']

test = db.test

# 增加一条记录
person = {'name': 'zone', 'sex': 'boy'}
person_id = test.insert_one(person).inserted_id
print(person_id)

# 批量插入
persons = [{'name': 'zone', 'sex': 'boy'}, {'name': 'zone1', 'sex': 'boy1'}]
result = test.insert_many(persons)
print(result.inserted_ids)

# 删除单条记录
result1 = test.delete_one({'name': 'zone'})
print(result1)

# 批量删除
result1 = test.delete_many({'name': 'zone'})
print(result1)

# 更新单条记录
res = test.update_one({'name': 'zone'}, {'$set': {'sex': 'girl girl'}})
print(res.matched_count)

# 更新多条记录
test.update_many({'name': 'zone'}, {'$set': {'sex': 'girl girl'}})

# 查找多条记录
print(test.find())

# 添加查找条件
print(test.find({"sex": "boy"}).sort("name"))

# 聚合查找
aggs = [
    {"$match": {"$or": [{"field1": {"$regex": "regex_str"}}, {"field2": {"$regex": "regex_str"}}]}},     # 正则匹配字段
    {"$project": {"field3": 1, "field4": 1}},       # 筛选字段
    {"$group": {"_id": {"field3": "$field3", "field4": "$field4"}, "count": {"$sum": 1}}},   # 聚合操作
]
result = test.aggregate(pipeline=aggs)
print(result)
