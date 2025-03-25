# import mysql.connector.pooling
# from config.mysql import MYSQL_CONFIG

# class MySQLManager:
#     def __init__(self):
#         self.pool = mysql.connector.pooling.MySQLConnectionPool(
#             pool_name="priest_pool",
#             pool_size=MYSQL_CONFIG['pool_size'],
#             **{k:v for k,v in MYSQL_CONFIG.items() if k not in ['pool_size','pool_recycle']}
#         )

#     def get_connection(self):
#         return self.pool.get_connection()

#     def get_item(self, itemid):
#         with self.get_connection() as conn:
#             cursor = conn.cursor(dictionary=True)
#             cursor.execute("SELECT * FROM items WHERE itemid = %s", (itemid,))
#             return cursor.fetchone()

# db/mysqlmanager.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from config.mysql import (
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DATABASE,
    MYSQL_POOLSIZE,
    MYSQL_POOLRECYCLE,
)

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/"
    f"{MYSQL_DATABASE}?charset=utf8mb4"
)

# 创建引擎
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_size=MYSQL_POOLSIZE,
    pool_recycle=MYSQL_POOLRECYCLE,
)

# 创建 Session 工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


