import os
import getpass
import MySQLdb
from dotenv import load_dotenv

# 讀取環境變數(Environment)檔案
# 通常用來存放金鑰、帳密、token…等資料
load_dotenv()

# 讀取帳密(優先從環境變數存取，不存在才互動式要求）
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 3307))
DB_USER = os.environ.get("DB_USER") or input("DB user: ")
DB_PASSWORD = os.environ.get("DB_PASSWORD") or getpass.getpass("DB password: ")
DB_NAME = os.environ.get("DB_NAME", "cmdev")

# 建立連線
try:
    conn = MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        port=DB_PORT,
        db=DB_NAME,
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    # 參數化查詢(查詢部門編號30的員工，薪資大於1300）
    dept = 30
    min_salary = 1300

    sql = """
    SELECT empno, ename, job, salary
    FROM emp
    WHERE deptno = %s AND salary > %s
    """
    cursor.execute(sql, (dept, min_salary))

    rows = cursor.fetchall()
    for r in rows:
        print(r)

except MySQLdb.Error as e:
    print("錯誤訊息:", e)
    
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
