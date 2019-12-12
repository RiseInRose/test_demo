from elasticsearch import Elasticsearch
import json
import datetime

# mapping 定义你的es字段
doc_mapping = {
    'properties': {
        "other_id": {"type": "long"},
        "city": {"type": "keyword"},
        "id": {"type": "keyword"},
    }
 }

# es = Elasticsearch(hosts='http://server.muguayun.top', port=10025)
es = Elasticsearch(['http://server.muguayun.top:10025'])

# es的基础配置,  index_name, alias(别名可以创建多个), doc_type(表名)
index_name = f'complex_test'
online_alias = f'online_complex_test'
type_name = f'complex_city'

# es 创建库
# 创建索引，索引的名字是my-index,如果已经存在了，就返回个400，
# 这个索引可以现在创建，也可以在后面插入数据的时候再临时创建

es.indices.create(index='my-index')


# 插入数据,(这里省略插入其他两条数据，后面用)
# 每次插入数据，如果数据相同，则会使用新数据覆盖原来数据，并且更新版本。
es.index(index="my-index", doc_type="test-type", id='01', body={"any": "data01", "timestamp": datetime.datetime.now()})

# 查询数据，两种get and search，如果获取不成功，则报错。
# get获取
res1 = es.get(index="my-index", doc_type="test-type", id='01')

# es.get(index='indexName', doc_type='typeName', id='idValue')

# print(res1)

# delete：删除指定index、type、id的文档。如果找不到这个数据，则删除报错。
es.delete(index='my-index', doc_type='test-type', id='01')

# 条件删除
# delete_by_query：删除满足条件的所有数据，查询条件必须符合DLS格式

query = {'query': {'match': {'sex': 'famale'}}}# 删除性别为女性的所有文档

# query = {'query': {'range': {'age': {'lt': 11}}}}# 删除年龄小于11的所有文档

es.delete_by_query(index='indexName', body=query, doc_type='typeName')

# 条件更新
# update_by_query：更新满足条件的所有数据，写法同上删除和查询

# 批量写入、删除、更新
doc = [
    {"index": {}},
    {'name': 'jackaaa', 'age': 2000, 'sex': 'female', 'address': u'北京'},
    {"index": {}},
    {'name': 'jackbbb', 'age': 3000, 'sex': 'male', 'address': u'上海'},
    {"index": {}},
    {'name': 'jackccc', 'age': 4000, 'sex': 'female', 'address': u'广州'},
    {"index": {}},
    {'name': 'jackddd', 'age': 1000, 'sex': 'male', 'address': u'深圳'},
]
# doc = [
#     {'index': {'_index': 'indexName', '_type': 'typeName', '_id': 'idValue'}}
#     {'name': 'jack', 'sex': 'male', 'age': 10}
#     {'delete': {'_index': 'indexName', '_type': 'typeName', '_id': 'idValue'}}
#     {"create": {'_index': 'indexName', "_type": 'typeName', '_id': 'idValue'}}
#     {'name': 'lucy', 'sex': 'female', 'age': 20}
#     {'update': {'_index': 'indexName', '_type': 'typeName', '_id': 'idValue'}}
#     {'doc': {'age': '100'}}
# ]
es.bulk(index='indexName', doc_type='typeName', body=doc)

index_type = ''
i = ''
# 批量更新也可以采用如下的方式进行json拼装，最后写入
# for line in list():
#     action = {
#         "_index": index_name,
#         "_type": index_type,
#         "_id": i,  # _id 也可以默认生成，不赋值
#         "_source": {
#             "date": line['date'],
#             "source": line['source'].decode('utf8'),
#             "link": line['link'],
#             "keyword": line['keyword'].decode('utf8'),
#             "title": line['title'].decode('utf8')}
#     }
#     i += 1
#     ACTIONS.append(action)
# success, _ = bulk(self.es, ACTIONS, index=self.index_name, raise_on_error=True)

# 查询所有数据

# 搜索所有数据
es.search(index="my_index", doc_type="test_type")

# 或者
body = {
    "query": {
        "match_all": {}
    }
}
es.search(index="my_index", doc_type="test_type", body=body)

# term与terms

# term
body = {
    "query": {
        "term": {
            "name": "python"
        }
    }
}
# 查询name="python"的所有数据
es.search(index="my_index", doc_type="test_type", body=body)

# terms
body = {
    "query": {
        "terms": {
            "name": [
                "python", "android"
            ]
        }
    }
}
# 搜索出name="python"或name="android"的所有数据
es.search(index="my_index", doc_type="test_type", body=body)

# match与multi_match

# match:匹配name包含python关键字的数据
body = {
    "query": {
        "match": {
            "name": "python"
        }
    }
}
# 查询name包含python关键字的数据
es.search(index="my_index", doc_type="test_type", body=body)

# multi_match:在name和addr里匹配包含深圳关键字的数据
body = {
    "query": {
        "multi_match": {
            "query": "深圳",
            "fields": ["name", "addr"]
        }
    }
}
# 查询name和addr包含"深圳"关键字的数据
es.search(index="my_index", doc_type="test_type", body=body)
# ids

body = {
    "query": {
        "ids": {
            "type": "test_type",
            "values": [
                "1", "2"
            ]
        }
    }
}
# 搜索出id为1或2d的所有数据
es.search(index="my_index", doc_type="test_type", body=body)

# 复合查询bool
# bool有3类查询关系，must(都满足), should(其中一个满足), must_not(都不满足)

body = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "name": "python"
                    }
                },
                {
                    "term": {
                        "age": 18
                    }
                }
            ]
        }
    }
}
# 获取name="python"并且age=18的所有数据
es.search(index="my_index", doc_type="test_type", body=body)

# 切片式查询

body = {
    "query": {
        "match_all": {}
    },
    "from": 2, # 从第二条数据开始
    "size": 4  # 获取4条数据
}
# 从第2条数据开始，获取4条数据
es.search(index="my_index", doc_type="test_type", body=body)

# 范围查询

body = {
    "query": {
        "range": {
            "age": {
                "gte": 18,  # >=18
                "lte": 30  # <=30
            }
        }
    }
}
# 查询18<=age<=30的所有数据
es.search(index="my_index", doc_type="test_type", body=body)

# 前缀查询

body = {
    "query": {
        "prefix": {
            "name": "p"
        }
    }
}
# 查询前缀为"赵"的所有数据
es.search(index="my_index", doc_type="test_type", body=body)

# 通配符查询

body = {
    "query": {
        "wildcard": {
            "name": "*id"
        }
    }
}
# 查询name以id为后缀的所有数据
es.search(index="my_index", doc_type="test_type", body=body)

# 排序

body = {
    "query": {
        "match_all": {}
    },
    "sort": {
        "age": {  # 根据age字段升序排序
            "order": "asc"  # asc升序，desc降序
        }
    }
}

# filter_path
# 响应过滤

# 只需要获取_id数据,多个条件用逗号隔开
es.search(index="my_index", doc_type="test_type", filter_path=["hits.hits._id"])

# 获取所有数据
es.search(index="my_index", doc_type="test_type", filter_path=["hits.hits._*"])

# count
# 执行查询并获取该查询的匹配数

# 获取数据量
es.count(index="my_index", doc_type="test_type")

# 度量类聚合
# 获取最小值

body = {
    "query": {
        "match_all": {}
    },
    "aggs": {  # 聚合查询
        "min_age": {  # 最小值的key
            "min": {  # 最小
                "field": "age"  # 查询"age"的最小值
            }
        }
    }
}
# 搜索所有数据，并获取age最小的值
es.search(index="my_index", doc_type="test_type", body=body)

# 获取最大值

body = {
    "query": {
        "match_all": {}
    },
    "aggs": {  # 聚合查询
        "max_age": {  # 最大值的key
            "max": {  # 最大
                "field": "age"  # 查询"age"的最大值
            }
        }
    }
}
# 搜索所有数据，并获取age最大的值
es.search(index="my_index", doc_type="test_type", body=body)

# 获取和

body = {
    "query": {
        "match_all": {}
    },
    "aggs": {  # 聚合查询
        "sum_age": {  # 和的key
            "sum": {  # 和
                "field": "age"  # 获取所有age的和
            }
        }
    }
}
# 搜索所有数据，并获取所有age的和
es.search(index="my_index", doc_type="test_type", body=body)

# 获取平均值

body = {
    "query": {
        "match_all": {}
    },
    "aggs": {  # 聚合查询
        "avg_age": {  # 平均值的key
            "sum": {  # 平均值
                "field": "age"  # 获取所有age的平均值
            }
        }
    }
}
# 搜索所有数据，获取所有age的平均值
es.search(index="my_index", doc_type="test_type", body=body)

#
# # 删除索引
# res = es.indices.delete(index=index_name)
# print(res)

'''更多用法 https://elasticsearch-py.readthedocs.io/en/master/api.html'''
