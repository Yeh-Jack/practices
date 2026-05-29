import pymongo
from mongo_conn import connectMongo

try:
    # 連線到 MongoDB
    monclient = connectMongo()


except Exception as e:
    print("資料庫發生錯誤", e)
