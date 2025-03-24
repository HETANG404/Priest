import mysql.connector.pooling
from config.mysql import MYSQL_CONFIG

class MySQLManager:
    def __init__(self):
        self.pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="priest_pool",
            pool_size=MYSQL_CONFIG['pool_size'],
            **{k:v for k,v in MYSQL_CONFIG.items() if k not in ['pool_size','pool_recycle']}
        )

    def get_connection(self):
        return self.pool.get_connection()

    def get_item(self, itemid):
        with self.get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM items WHERE itemid = %s", (itemid,))
            return cursor.fetchone()