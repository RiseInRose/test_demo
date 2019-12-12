# coding=utf-8
# author caturbhuja
# date   2019/9/23 4:10 PM 
# wechat chending2012
# 日期 推荐类型 场景 算法 推荐次数 推荐人数 推荐点击数 推荐点击率


j = """
2019-09-18 1 selection 热门榜单 66475771 709135 115321 0.001735
2019-09-18 1 selection 其他推荐算法 21780 1153 42 0.001928
2019-09-18 1 selection 基于用户的协同过滤 2427417 77732 17073 0.007033
2019-09-18 1 fashionMakeup 热门榜单 87871 2430 733 0.008342
2019-09-18 1 fashionMakeup 基于用户的协同过滤 8385 598 229 0.027311
2019-09-18 1 makeup 热门榜单 326087 8435 5061 0.01552
2019-09-18 1 makeup 其他推荐算法 679 32 17 0.025037
2019-09-18 1 makeup 基于用户的协同过滤 32274 2119 1040 0.032224
2019-09-18 1 homeGoods 热门榜单 295330 8242 1427 0.004832
2019-09-18 1 homeGoods 其他推荐算法 37 2 0 0.0
2019-09-18 1 homeGoods 基于用户的协同过滤 8249 1144 197 0.023882
2019-09-18 1 qualityHome 热门榜单 97834 2760 1021 0.010436
2019-09-18 1 qualityHome 基于用户的协同过滤 8630 734 145 0.016802
2019-09-18 1 phoneDigital 热门榜单 150812 4497 2035 0.013494
2019-09-18 1 phoneDigital 基于用户的协同过滤 23684 1440 706 0.029809
2019-09-18 1 phone 热门榜单 2502873 63969 52776 0.021086
2019-09-18 1 phone 其他推荐算法 62255 2054 462 0.007421
2019-09-18 1 phone 基于用户的协同过滤 265528 17108 8391 0.031601
2019-09-18 1 computer 热门榜单 538676 14628 5810 0.010786
2019-09-18 1 computer 其他推荐算法 537 30 15 0.027933
2019-09-18 1 computer 基于用户的协同过滤 50451 3264 1505 0.029831
2019-09-18 1 selectionNew 热门榜单 4608 1 0 0.0
"""
''' 经过测试，制表符在处理格式问题上其实没什么大的乱用 '''
# for each in j.split('\n'):
#     k = each.split(' ')
#     l = ('\t').join(k)
#     print(l)

# ---------------- prettytable ---------------
# from prettytable import PrettyTable
# table = PrettyTable(['日期', '推荐类型', '场景', '算法', '推荐次数', '推荐人数', '推荐点击数', '推荐点击率'])
# count = 0
#
# for each in j.split('\n'):
#     count += 1
#     k = each.split(' ')
#     if k[0]:
#         table.add_row(k)
# print(table)

# ---------------- prettytable2 ---------------
# from prettytable import PrettyTable
# header = ['日期', '推荐类型', '场景', '算法', '推荐次数', '推荐人数', '推荐点击数', '推荐点击率']
# table = PrettyTable()
# table_tmp = dict()
# for each in j.split('\n'):
#     k = each.split(' ')
#     if k[0]:
#         for index, ggs in enumerate(header):
#             if table_tmp.get(ggs):
#                 table_tmp[ggs].append(k[index])
#             else:
#                 table_tmp[ggs] = [k[index]]
#
# for key, value in table_tmp.items():
#     table.add_column(key, value)
# print(table)


# ---------------- tabulate ----------------
from tabulate import tabulate
table = list()
for each in j.split('\n'):
    k = each.split(' ')
    if k[0]:
        table.append(k)

header = ['日期', '推荐类型', '场景', '算法', '推荐次数', '推荐人数', '推荐点击数', '推荐点击率']

print(tabulate(table, header, tablefmt="grid"))
# print(tabulate(table, ['date', 'type', 's1', 's2', 's3', 's4', 's5', 's6'], tablefmt="grid"))


# ------- 方法一 ------------ 自己填充空位
len_fix = [10, 10, 14, 17, 10, 10, 10, 10]
table = list()
for each in j.split('\n'):
    k = each.split(' ')
    k_tmp = list()
    if k[0]:
        for name, each_len in zip(k, len_fix):
            # print('{name:<{len}}\t'.format(name=name, len=14 - len(name.encode('GBK')) + len(name)))  # 手动调整宽度，14这个参数刚刚好
            k_tmp.append('{name:<{len}}\t'.format(name=name, len=each_len - len(name.encode('GBK')) + len(name)))
        # k_tmp.append('\n')
        # table.append(k_tmp)
        table.append(' '.join(k_tmp))

header = ['{name:<{len}}\t'.format(name=name, len=each_len - len(name.encode('GBK')) + len(name)) for name, each_len in zip(['日期', '推荐类型', '场景', '算法', '推荐次数', '推荐人数', '推荐点击数', '推荐点击率'], len_fix)]


# print(tabulate(table, header, tablefmt="grid"))
# print(tabulate(table, ['date', 'type', 's1', 's2', 's3', 's4', 's5', 's6'], tablefmt="grid"))

header_print = (' ').join(header)
# table_print = (' ').join(table)

print(header_print)
for each in table:
    print(each)

# -------方法二------------ 采用 chr(12288)  中文空格 补充
print('{0:{1}^9}\t'.format(ii, chr(12288)), end='')  # 居中对齐
print('{0:{1}<9}\t'.format(ii, chr(12288)), end='')  # 左对齐    用chr(12288)去填充，即这里的{1}


# ---------------格式对齐函数---------------
# def myAlign(string, length=0):
#     if length == 0:
#         return string
#     slen = len(string)
#     re = string
#
#     # 检验是否含有中文字符
#     def is_contains_chinese(strs):
#         for _char in strs:
#             if '\u4e00' <= _char <= '\u9fa5':
#                 return True
#         return False
#
#     if is_contains_chinese(string):
#         placeholder = ' '
#     else:
#         placeholder = '　'
#     while slen < length:
#         re += placeholder
#         slen += 1
#     return re
#
#
# s1 = '我是一个长句子，是的很长的句子。'
# s2 = '我是短句子'
#
# print(myAlign(s1, 20) + myAlign(s2, 10))
# print(myAlign(s2, 20) + myAlign(s1, 10))



# 下面这个暂时不处理，遇到了ascii 编码错误。
# with open('data1.txt', 'w') as f:
#     f.write(j)
#
# with open('data1.txt', 'r') as f:
#     i = f.readlines()
