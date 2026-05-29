import pandas as pd
import pymongo

# 從第1行開始讀，往下讀370行
data = pd.read_csv("113年度各鄉鎮市區人口密度.csv", header=1, nrows=370, encoding="utf-8")
# 把「...」更改為0，再將整欄型態調整為int
data["年底人口數"] = data["年底人口數"].replace("… ", 0).astype("int")
data["人口密度"] = data["人口密度"].replace("… ", 0).astype("int")

try:
    # 連線到mongodb
    myclient = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
    
    # testdb(等同於MySQL的database)
    testdb = myclient["testdb"]
    # 創建檔案towndata(等同於MySQL的table)
    towndata = testdb["towndata"]
    
    # 插入資料
    towndata.insert_many(data.to_dict(orient="records"))

except Exception as e:
    print("資料庫發生錯誤", e)
    
    