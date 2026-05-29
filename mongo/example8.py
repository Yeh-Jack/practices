import pymongo

try:
    # 連線到mongodb
    myclient = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
    
    testdb = myclient["testdb"]
    towndata = testdb["towndata"]
    
    # 用正則方式查詢臺中市開頭的資料
    print("=======查詢台中市的資料(正則寫法)=======")
    for row in towndata.find({"區域別":{"$regex": "^臺中市"}}):
        print(row)
        
    # 用$where方式查詢臺中市開頭的資料
    # print("======= 查詢臺中市的資料($where寫法)=======")
    # for row in towndata.find({"$where": "this.區域別.startsWith('臺中市')"}):
    #     print(row)

except Exception as e:
    print("資料庫發生錯誤", e)
    
    