# coding:utf-8
# author caturbhuja
# date   2019/8/12 3:23 PM 
# wechat chending2012 
"""
redis orm
"""

import time
from abc import ABCMeta, abstractmethod
import zlib
import redis
import random


class RedisBase(object):

    def __init__(self, redis_ip, redis_port, redis_no, redis_passwd, cache_time=0, socket_timeout=-1, **kw):
        self._redis_ip = redis_ip
        self._redis_port = redis_port
        self._redis_no = redis_no
        self._redis_passwd = redis_passwd
        self._socket_timeout = socket_timeout
        self._rdb = None
        # # self._log = handle_ilog(dict_get(kw, 'ilog'))

        self._retry = 10
        self._internal = 60
        self.connect()

        self._cache_time = cache_time
        self._is_cache = False
        if cache_time > 0:
            self._is_cache = True
            self._cache_info = {}

    def connect(self):
        i = 0
        while self._rdb is None and i < self._retry:
            try:
                if self._socket_timeout <= 0:
                    self._rdb = redis.StrictRedis(host=self._redis_ip, port=self._redis_port, db=self._redis_no, password=self._redis_passwd)
                else:
                    self._rdb = redis.StrictRedis(host=self._redis_ip, port=self._redis_port, db=self._redis_no, password=self._redis_passwd, socket_timeout=self._socket_timeout)
            except Exception as e:
                print(e)
                # self._log.error("redis connecting error, host: %s, port: %d, db: %s, err_msg: %s\t%s" %
                #                  (self._redis_ip, self._redis_port, self._redis_no, str(e), traceback.format_exc().replace("\n", "")))
                time.sleep(self._internal)
            i += 1
        # if self._rdb:
            # self._log.info("redis connected, host: %s, port: %d, db: %s" % (self._redis_ip, self._redis_port, self._redis_no))
        # else:
            # self._log.error("last redis connecting error, host: %s, port: %d, db: %s" % (self._redis_ip, self._redis_port, self._redis_no))

    # 统一外部调用方法
    def get(self, key, pos=0, length=-1):
        if not self._is_cache or isinstance(key, list):  # todo 目前只针对RedisKv临时处理, 后续需要处理
            return self.get_local(key, pos, length)
        return self.get_cache_item(key, pos, length)

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_local(self, key, pos, length):
        pass
        # self.log_.error("RedisBase.get_local")

    def get_cache_item(self, key, pos, length):
        cur_time = int(time.time())
        ret_val = None
        get_cache_flag = False
        try:
            cache_key = "_".join([str(key), str(pos), str(length)])
            if self._is_cache:
                if self._cache_info.has_key(cache_key):
                    init_ts, cache_value = self._cache_info[cache_key]
                    if init_ts + self._cache_time >= cur_time:
                        get_cache_flag = True
                        ret_val = cache_value
                if not get_cache_flag:
                    ret_val = self.get_local(key, pos, length)
                    if self._is_cache:
                        self._cache_info[cache_key] = [cur_time, ret_val]
        except Exception as e:
            # self._log.error("get_cache_item error, host: %s, port: %d, db: %s, err_msg: %s\t%s" %
            #                  (self._redis_ip, self._redis_port, self._redis_no, str(e), traceback.format_exc().replace("\n", "")))
            pass
        return ret_val

    def clear_cache(self):
        self._cache_info = {}


class RedisList(RedisBase):

    def __init__(self, redis_ip, redis_port, redis_no, redis_passwd, cache_time=0, socket_timeout=-1, **kw):
        RedisBase.__init__(self, redis_ip, redis_port, redis_no, redis_passwd, cache_time, socket_timeout, **kw)

    def get_local(self, key, pos=0, length=0):
        ret = list()
        st = int(time.time() * 1000)
        try:
            ret = self._rdb.lrange(key, pos, pos + length)
        except Exception as e:
            pass
            # self._log.error("get_local error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
        et = int(time.time() * 1000)
        if et - st > 1500:
            pass
            # self._log.warning("get %s redis too long %s ms,redis_port:%d" % (key, str(et - st), self._redis_port))
        return ret

    def set(self, key, value_list, expire_time=0):
        st = int(time.time() * 1000)
        tmp_key = key + str(random.randint(0, int(time.time())))
        try:
            if value_list:
                self._rdb.delete(tmp_key)
                len_ret = self._rdb.rpush(tmp_key, *value_list)
                if len_ret == len(value_list):
                    self._rdb.rename(tmp_key, key)
                    if expire_time > 0:
                        self._rdb.expire(key, expire_time)
            else:
                pass
                # self._log.warning("redis storing null val, key: %s, value: %s" % (key, str(value_list)))
        except Exception as e:
            pass
            # self._log.error("redis storing error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
        et = int(time.time() * 1000)
        if et - st > 1500:
            pass
            # self._log.warning("get %s redis too long %s ms,redis_port:%d" % (key, str(et - st), self._redis_port))

    def set_simple(self, key, value_list, timeout=0):
        flag = True
        try:
            if value_list:
                self._rdb.rpush(key, *value_list)
            if timeout > 0:
                self._rdb.expire(key, timeout)
        except Exception as e:
            print(e)
            # self._log.error("set error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
            flag = False
        return flag

    def get_len(self, key):
        return self._rdb.llen(key)

    def lpop(self, key):
        return self._rdb.lpop(key)

    def rpop(self, key):
        return self._rdb.rpop(key)

    def lpush(self, key, value_list, timeout=0):
        st = int(time.time() * 1000)
        try:
            self._rdb.lpush(key, *value_list)
            if timeout > 0:
                self._rdb.expire(key, timeout)
        except Exception as e:
            print(e)
            pass
            # self._log.error("lpush error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
        et = int(time.time() * 1000)
        if et - st > 1500:
            pass
            # self._log.warning("lpush %s redis too long %s ms,redis_port:%d" % (key, str(et - st), self._redis_port))

    def lpushx(self, key, value, timeout=0):
        st = int(time.time() * 1000)
        try:
            self._rdb.lpushx(key, value)
            if timeout > 0:
                self._rdb.expire(key, timeout)
        except Exception as e:
            print(e)
            # self._log.error("lpush error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
        et = int(time.time() * 1000)
        if et - st > 1500:
            pass
            # self._log.warning("lpush %s redis too long %s ms,redis_port:%d" % (key, str(et - st), self._redis_port))

    def clear_list(self, key):
        return self._rdb.ltrim(key, 0, 1)


class RedisSortSet(RedisBase):

    def __init__(self, redis_ip, redis_port, redis_no, redis_passwd, cache_time=0, withscore=False, socket_timeout=-1, **kw):
        RedisBase.__init__(self, redis_ip, redis_port, redis_no, redis_passwd, cache_time, socket_timeout, **kw)
        self._with_score = withscore

    def get_local(self, key, pos, length):
        ret = self._rdb.zrevrange(key, pos, pos + length, withscores=self._with_score)
        return ret


class RedisKv(RedisBase):

    def __init__(self, redis_ip, redis_port, redis_no, redis_passwd, cache_time=0, socket_timeout=-1, **kw):
        RedisBase.__init__(self, redis_ip, redis_port, redis_no, redis_passwd, cache_time, socket_timeout, **kw)

    def get(self, key, pos=0, length=-1):
        if self._is_cache and isinstance(key, list): #针对RedisKv临时处理，把已经在缓存中的数据拿出来
            ret_val = ['dft'] * len(key)
            raw_key = list()
            cur_time = int(time.time())
            # list split into two slices(the cached list and the uncached list), use mget command to
            # get the uncached results, and merge the results , return
            for idx, sub_key in enumerate(key):
                cache_key = "_".join([str(sub_key), str(pos), str(length)])
                get_cache_flag = False
                if self._cache_info.has_key(cache_key):
                    init_ts, cache_value = self._cache_info[cache_key]
                    if init_ts + self._cache_time >= cur_time:
                        get_cache_flag = True
                        ret_val[idx] = cache_value

                if not get_cache_flag:
                    raw_key.append(sub_key)

            raw_ret = self._rdb.mget(raw_key)
            blank_idx_lst = [idx for idx, val in enumerate(ret_val) if val == "dft"]
            for idx, sub_key in enumerate(raw_key):
                cache_key = "_".join([str(sub_key), str(pos), str(length)])
                self._cache_info[cache_key] = [cur_time, raw_ret[idx]]
                org_idx = blank_idx_lst[idx]
                ret_val[org_idx] = raw_ret[idx]

            return ret_val
        return self.get_cache_item(key, pos, length)

    def get_local(self, key, pos=0, length=0):
        st = int(time.time() * 1000)
        if type(key) == list:
            ret = self._rdb.mget(key)
        else:
            ret = self._rdb.get(key)
        et = int(time.time() * 1000)
        if et - st > 1500:
            pass
            # self._log.warning("get %s redis too long %s ms,redis_port:%d" % (key, str(et - st), self._redis_port))
        return ret

    def set(self, key, value, timeout=0):
        flag = True
        st = int(time.time() * 1000)
        tmp_key = key + str(random.randint(0, int(time.time())))
        try:
            self._rdb.delete(tmp_key)
            self._rdb.set(tmp_key, value)
            self._rdb.rename(tmp_key, key)
            if timeout > 0:
                self._rdb.expire(key, timeout)
        except Exception as e:
            # self._log.error("set error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
            flag = False
        et = int(time.time() * 1000)
        if et - st > 1500:
            pass
            # self._log.warning("get %s redis too long %s ms,redis_port:%d" % (key, str(et - st), self._redis_port))
        return flag


class RedisKvZip(RedisKv):

    def get(self, key, pos=0, length=-1):
        return RedisBase.get(self, key, pos, length)

    def set(self, key, value, timeout):
        st = int(time.time() * 1000)
        try:
            zlib_str = zlib.compress(value)
            RedisKv.set(self, key, zlib_str, timeout)
        except Exception as e:
            pass
            # self._log.error("redis storing error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
        et = int(time.time() * 1000)
        if et - st > 1500:
            pass
            # self._log.warning("get %s redis too long %s ms,redis_port:%d" % (key, str(et - st), self._redis_port))

    def get_local(self, key, pos=0, length=0):
        st = int(time.time() * 1000)
        try:
            if type(key) == list:
                ret = []
                ret_list = self._rdb.mget(key)
                for ret_item in ret_list:
                    try:
                        if ret_item is not None:
                            ret_item_zlib = zlib.decompress(ret_item)
                            ret_item = ret_item_zlib
                    except Exception as e:
                        pass
                        # self._log.error("get_local error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
                    ret.append(ret_item)
            else:
                ret = self._rdb.get(key)
                try:
                    if ret is not None:
                        ret = zlib.decompress(ret)
                except Exception as e:
                    pass
                    # self._log.error("get_local error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
        except Exception as e:
            pass
            # self._log.error("get_local error, key: %s, err_msg: %s\t%s" % (str(key), str(e), traceback.format_exc().replace("\n", "")))
            ret = None
            if type(key) == list:
                ret = [None for i in range(len(key))]
        et = int(time.time() * 1000)
        if et - st > 1500:
            pass
            # self._log.warning("get %s redis too long %s ms,redis_port:%d" % (key, str(et - st), self._redis_port))
        return ret


def main():
    tt = redis.StrictRedis(host='localhost', port=6379, db=8)
    tt.set('nini', 666)
    tt.lpush('queue', json.dumps({1: 2}))
    i = tt.rpop('queue')
    j = tt.get('nini')
    print(j)
    print(i)


if __name__ == "__main__":
    import json
    main()
