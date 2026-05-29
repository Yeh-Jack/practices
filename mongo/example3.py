import pymongo

try:
    # 連線到mongodb
    myclient = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
    
    # 創建集合mydb(等同於MySQL的database)
    mydb = myclient["mydb"]
    # 創建檔案emp(等同於MySQL的table)
    empdata = mydb["emp"]
    
    data = [{"empno":7499, "ename":"ALLEN", "job":"SALESMAN"},
            {"empno":7521, "ename":"WARD", "job":"SALESMAN"},
            {"empno":7566, "ename":"JONES", "job":"MANAGER"}]
    
    
    # 插入多筆資料
    cursor = empdata.insert_many(data)
    print(cursor)
    
    # 顯示目前的資料
    for data in empdata.find():
        print(data)

except Exception as e:
    print("資料庫發生錯誤", e)
    
