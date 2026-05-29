import pymongo

try:
    # 連線到mongodb
    myclient = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
    
    # 創建集合mydb(等同於MySQL的database)
    mydb = myclient["mydb"]
    # 創建檔案emp(等同於MySQL的table)
    empdata = mydb["emp"]
    
    print("=======查詢全部資料=======")
    for data in empdata.find():
        print(data)

    print("=======查詢job是SALESMAN的資料=======")
    for data in empdata.find({"job":"SALESMAN"}):
        print(data)
        
    print("=======查詢salary>1300的資料=======")
    for data in empdata.find({"salary":{"$gt":1300}}):
        print(data)
    
except Exception as e:
    print("資料庫發生錯誤", e)
    
