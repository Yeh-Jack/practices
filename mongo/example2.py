import pymongo

try:
    # 連線到mongodb
    myclient = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
    
    # 創建集合mydb(等同於MySQL的database)
    mydb = myclient["mydb"]
    # 創建檔案emp(等同於MySQL的table)
    empdata = mydb["emp"]
    
    data = {"empno":7369, "ename":"SMITH", "job":"CLERK"}
    # 插入一筆資料
    cursor = empdata.insert_one(data)
    print(cursor)
    
    # 顯示剛插入的資料
    for data in empdata.find():
        print(data)

except Exception as e:
    print("資料庫發生錯誤", e)
    
