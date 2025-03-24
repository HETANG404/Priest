# config/redis.py
REDIS_CONFIG = {
    "host": "localhost",
    "port": 6379,
    "db": 0,
    "max_connections": 20,
    "socket_timeout": 3,
    "ttl": 3600  # 默认1小时过期
}