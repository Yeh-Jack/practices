import pymongo
import os
from dotenv import load_dotenv
import getpass
import mysql.connector   # 安裝指令pip install mysql-connector-python
from datetime import datetime

load_dotenv("./.env", override=True)

# 讀取帳密(優先從環境變數存取，不存在才互動式要求）
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 3307))
DB_USER = os.environ.get("DB_USER") or input("DB user: ")
DB_PASSWORD = os.environ.get("DB_PASSWORD") or getpass.getpass("DB password: ")
DB_NAME = os.environ.get("DB_NAME", "cmdev")

# ======== 連線到 MariaDB ========
mariadb_config = {
    "host": DB_HOST,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "database": DB_NAME,
    "port": DB_PORT
}

try:
    mariadb_conn = mysql.connector.connect(**mariadb_config)
    # 從mysql撈出來的資料會是tuple(如(7369, "SMITH", "CLERK", ...))
    # 設定dictionary=True，會讓撈出來的資料變成dict(如{"empno": 7369, "ename": "SMITH", ...})
    cursor = mariadb_conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM emp")
    emp_rows = cursor.fetchall()

finally:
    if "mariadb_conn" in locals() and mariadb_conn.is_connected():
        cursor.close()
        mariadb_conn.close()

# ======== 連線到 MongoDB ========
mongo_client = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
mongo_db = mongo_client["testdb"]
mongo_col = mongo_db["emp"]

mongo_docs = []

for row in emp_rows:
    clean_row = {}
    for key, value in row.items():
        if value is not None:
            # 檢查是否為日期或時間物件(查詢value物件裡是否有strftime方法)
            if hasattr(value, "strftime"):
                # 如果是單純的date物件(沒有時分秒)，需轉換為datetime物件
                if not isinstance(value, datetime):
                    clean_row[key] = datetime(value.year, value.month, value.day)
                else:
                    clean_row[key] = value  # 如果原本就是datetime，直接寫入
            else:
                clean_row[key] = value

    mongo_docs.append(clean_row)

if mongo_docs:
    result = mongo_col.insert_many(mongo_docs)
    print("成功匯入%s筆資料至mongoDB" %(len(result.inserted_ids)))
else:
    print("沒有資料需要匯入")