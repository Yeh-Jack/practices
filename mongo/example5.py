import pymongo
import pandas as pd

try:
    # 連線到mongodb
    myclient = pymongo.MongoClient("mongodb://root:12345678@localhost:27017/")
    
    # 創建集合mydb(等同於MySQL的database)
    mydb = myclient["mydb"]
    # 創建檔案emp(等同於MySQL的table)
    empdata = mydb["emp"]
    
    # 將emp表中的資料轉換成dataframe
    data = pd.DataFrame(empdata.find())

    # 找出salary的nan值的索引
    na_index = data[data["salary"].isna()].index
    # [1,2,3]
    # 修正salary欄中的缺值
    new_salaries = [800, 1600, 1350]    

    for i, val in zip(na_index, new_salaries):
        data.at[i, "salary"] = val
    
    # 將新資料寫回資料庫
    for doc in data.to_dict(orient="records"):
        empno = doc["empno"]
        doc.pop("_id", None)  # 移除_id欄位避免更新錯誤
        empdata.update_one({"empno": empno}, {"$set": doc})    

    print("=======查詢全部資料=======")
    for data in empdata.find():
        print(data)
    
except Exception as e:
    print("資料庫發生錯誤", e)
    
