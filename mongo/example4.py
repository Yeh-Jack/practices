import pymongo

try:
    # 連線到mongodb
    myclient = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
    
    # 創建集合mydb(等同於MySQL的database)
    mydb = myclient["mydb"]
    # 創建檔案emp(等同於MySQL的table)
    empdata = mydb["emp"]
    
    # 將員編7369的資料裡增加薪水1250元
    newdata = empdata.update_one({"empno":7369}, {"$set":{"salary":1250}})
    # print(newdata)
    
    print("=======查詢全部資料=======")
    for data in empdata.find():
        print(data)
    
except Exception as e:
    print("資料庫發生錯誤", e)
    
