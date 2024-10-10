import redis
from django.conf import settings


class RedisClient:
    # 类变量存储 Redis 连接
    _conn = None

    @classmethod
    def _get_connection(cls):
        if cls._conn is None:
            cls._conn = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB,
                                    password=settings.REDIS_PASSWORD)
        return cls._conn

    @classmethod
    def set_str(cls, key, value, time=0):
        conn = cls._get_connection()
        if time == 0:
            conn.set(key, value)
        else:
            conn.setex(name=key, time=time, value=value)

    @classmethod
    def get_str(cls, key):
        conn = cls._get_connection()
        value = conn.get(key)
        if value:
            value = str(value, encoding='utf8')
        else:
            return None
        return value

    @classmethod
    def delete_str(cls, key):
        conn = cls._get_connection()
        return conn.delete(key)

    @classmethod
    def insert_set(cls, key, values):
        conn = cls._get_connection()
        for value in values:
            conn.sadd(key, value)

    @classmethod
    def find_set(cls, key):
        conn = cls._get_connection()
        values = conn.smembers(key)
        if values:
            return [str(v, encoding='utf8') for v in values]
        return None

    @classmethod
    def insert_hash(cls, key, param, value):
        conn = cls._get_connection()
        conn.hset(key, param, value)

    @classmethod
    def get_value(cls, key, param):
        conn = cls._get_connection()
        return conn.hget(key, param)

    @classmethod
    def get_all_value(cls, key):
        conn = cls._get_connection()
        return conn.hgetall(key)

    @classmethod
    def del_hash(cls, key, param):
        conn = cls._get_connection()
        conn.hdel(key, param)
