import pymongo

try:
    # 連線到mongodb
    myclient = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
    
    testdb = myclient["testdb"]
    towndata = testdb["towndata"]
        
    # 查詢臺中市開頭且人數大於10萬以上的資料，由大到小排序    
    query = {"區域別": {"$regex": "^臺中市"},
             "年底人口數": {"$gt": 100000}}
    for row in towndata.find(query).sort("年底人口數", -1): # -1為降序，1為升序
        print(row)

except Exception as e:
    print("資料庫發生錯誤", e)
    
    