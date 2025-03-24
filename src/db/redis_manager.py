import redis
from config.redis import REDIS_CONFIG

class RedisManager:
    def __init__(self):
        self.pool = redis.ConnectionPool(
            host=REDIS_CONFIG['host'],
            port=REDIS_CONFIG['port'],
            db=REDIS_CONFIG['db'],
            max_connections=REDIS_CONFIG['max_connections']
        )
    
    @property
    def client(self):
        return redis.Redis(connection_pool=self.pool)

    def get(self, key):
        return self.client.get(key)

    def setex(self, key, ttl, value):
        return self.client.setex(key, ttl, value)