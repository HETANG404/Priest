import mysql.connector
from mysql.connector import Error

def check_table_structure(cursor, table_name):
    # 检查表是否存在
    cursor.execute(f"""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_schema = DATABASE()
        AND table_name = '{table_name}'
    """)
    exists = cursor.fetchone()[0]

    if exists:
        print(f"✅ 表 `{table_name}` 存在，结构如下：")
        cursor.execute(f"DESCRIBE {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()  # 换行
    else:
        print(f"❌ 表 `{table_name}` 不存在\n")

try:
    # 连接 MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="punk"
    )

    if conn.is_connected():
        print("✅ conn_successful\n")

    cursor = conn.cursor()

    # 要检查的表列表
    tables_to_check = ["images", "tags"]

    for table in tables_to_check:
        check_table_structure(cursor, table)

except Error as e:
    print("❌ 连接失败：", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("🔌 database disconn")
