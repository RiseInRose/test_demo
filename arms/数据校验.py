# author caturbhuja
# date   2019/7/8 5:49 PM 
# wechat chending2012 
"""
关于数据校验，python内部比较好在重要的位置添加数据校验，使得在后续的开发过程中，尽可能少出错
"""
'''
字符串校验
'''


# 校验字典内部是否包含这个字符串，拿到的字符串是否为空。
def check_dict(data_dict):
    if not data_dict.get("GUID", '').strip():
        return False


'''
int 校验
'''
