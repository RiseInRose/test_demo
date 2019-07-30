# coding:utf-8
# author caturbhuja
# date   2019/7/29 9:59 AM 
# wechat chending2012
import motor
import asyncio
"""
这个案例实现 python 异步驱动mongodb
motor 文档
https://motor.readthedocs.io/en/stable/
"""

'''连接'''
# 普通连接
client = motor.MotorClient('mongodb://localhost:27017')
'''
# 副本集连接
client = motor.MotorClient('mongodb://host1,host2/?replicaSet=my-replicaset-name')
# 密码连接
client = motor.MotorClient('mongodb://username:password@localhost:27017/dbname')
'''
# 获取数据库
db = client.zfdb
# db = client['zfdb']
# 获取 collection
collection = db.test
# collection = db['test']
loop = asyncio.get_event_loop()


# 增加1条记录
async def do_insert_one():
    document = {'name': 'zone', 'sex': 'boy'}
    result = await db.test_collection.insert_one(document)
    print(f'result {repr(result.inserted_id)}')
loop.run_until_complete(do_insert_one())


# 批量增加记录
async def do_insert_many():
    result = await db.test_collection.insert_many([{'name': i, 'sex': str(i + 2)} for i in range(20)])
    print(f'inserted {len(result.inserted_ids)} docs')
loop.run_until_complete(do_insert_many())


# 查找一条记录
async def do_find_one():
    document = await db.test_collection.find_one({'name': 'zone'})
    print(document)
loop.run_until_complete(do_find_one())


# 查找多条记录 排序
async def do_find_many():
    cursor = db.test_collection.find({'name': {'$lt': 5}}).sort('i')
    for document in await cursor.to_list(length=100):
        print(document)
loop.run_until_complete(do_find_many())


# 添加筛选条件，排序，跳过，限制返回结果数
async def do_find():
    cursor = db.test_collection.find({'name': {'$lt': 4}})
    # Modify the query before iterating
    cursor.sort('name', -1).skip(1).limit(2)
    async for document in cursor:
        print(document)
loop.run_until_complete(do_find())


# 统计
async def do_count():
    n = await db.test_collection.count_documents({})
    print('%s documents in collection' % n)
    n = await db.test_collection.count_documents({'name': {'$gt': 1000}})
    print('%s documents where i > 1000' % n)
loop.run_until_complete(do_count())


# 替换，将除id以外的其他内容全部替换
async def do_replace():
    coll = db.test_collection
    old_document = await coll.find_one({'name': 'zone'})
    print(f'found document: {old_document}')
    _id = old_document['_id']
    result = await coll.replace_one({'_id': _id}, {'sex': 'hanson boy'})
    print(f'replaced {result.modified_count} document')
    new_document = await coll.find_one({'_id': _id})
    print(f'document is now {new_document}')
loop.run_until_complete(do_replace())


# 更新 更新指定字段，不会影响到其他内容
async def do_update():
    coll = db.test_collection
    result = await coll.update_one({'name': 0}, {'$set': {'sex': 'girl'}})
    print(f'更新条数：{result.modified_count}')
    new_document = await coll.find_one({'name': 0})
    print(f'更新结果为：{new_document}')
loop.run_until_complete(do_update())


# 删除 删除指定记录
async def do_delete_many():
    coll = db.test_collection
    n = await coll.count_documents({})
    print(f'删除前有 {n} 条数据')
    await db.test_collection.delete_many({'name': {'$gte': 10}})
    m = await coll.count_documents({})
    print(f'删除后有 {m} 条数据')
loop.run_until_complete(do_delete_many())
