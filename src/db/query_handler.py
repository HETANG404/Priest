from src.db.redis_manager import RedisManager
from src.db.mysql_manager import MySQLManager
from config.redis import REDIS_CONFIG

class QueryHandler:
    def __init__(self):
        self.redis = RedisManager()
        self.mysql = MySQLManager()
        self.ttl = REDIS_CONFIG['ttl']

    def get_item(self, itemid):
        # 优先查询Redis
        if cached := self.redis.get(itemid):
            return cached
        
        # 回源MySQL查询
        if db_data := self.mysql.get_item(itemid):
            self.redis.setex(itemid, self.ttl, db_data)
            return db_data
        
        return None

    def batch_get_items(self, itemids):
        # 批量查询优化逻辑
        pass