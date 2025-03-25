import os
import sys
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text  # ✅ 新增这行

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.db.mysql_manager import engine


def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ 数据库连接成功，测试结果:", result.scalar())
    except SQLAlchemyError as e:
        print("❌ 数据库连接失败:", e)

if __name__ == "__main__":
    test_connection()
