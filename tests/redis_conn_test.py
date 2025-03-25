import redis

# 连接本地 Redis 服务
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# 测试写入和读取
r.set('name', 'TangRenchuan')
print("Got from Redis:", r.get('name'))
