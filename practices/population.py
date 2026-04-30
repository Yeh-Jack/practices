import pandas as pd
import MySQLdb
import os

SKIP_ONE_LINE = "\n\n"
cwd = os.getcwd()
# cwd = os.getcwd() + "/.."
csvPath = cwd + "/data/csv/"
jsonPath = cwd + "/data/json/"
xmlPath = cwd + "/data/xml/"

try:
    # 讀取資料
    fp = csvPath + "113年度各鄉鎮市區人口密度.csv"
    data = pd.read_csv(fp, encoding="utf-8", header=1, nrows=370)

except IOError as e:
    print(e)
    
# 清理資料
data["年底人口數"] = data["年底人口數"].replace("… ", 0).astype(int)
data["人口密度"] = data["人口密度"].replace("… ", 0).astype(int)

try:
    # 資料庫連線
    mydb = MySQLdb.connect(
                host="127.0.0.1",   # 主機ip
                user="jack",        # 帳號
                password="jack",    # 密碼
                port=3306,          # 通訊埠
                database = "testdb")  # 資料庫 
    
    
    cursor = mydb.cursor()
    
    # 將DataFrame轉換為python原生的tuple型態
    pdToTuple = [
        (str(row[0]), str(row[1]), int(row[2]), float(row[3]), int(row[4]))
        for row in data.itertuples(index=False, name=None)]
    
    sql = "INSERT INTO towndata VALUES(%s, %s, %s, %s, %s)"
    # executemany() 批量寫入
    cursor.executemany(sql, pdToTuple) 
    
    # 當資料寫完後要送出事件，以確保剛的資料有成功寫入
    mydb.commit()
    # 關閉資料庫連線
    cursor.close()
    mydb.close()
    
except Exception as e:
    print(e)
    
finally:
    print("資料庫連線結束")
