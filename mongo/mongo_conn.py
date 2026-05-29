import pymongo
import os, getpass


def connectMongo():
    try:
        # 讀取帳密(優先從環境變數存取，不存在才互動式要求）
        MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
        MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
        MONGO_DB = os.environ.get("MONGO_DB", "testdb")
        MONGO_USER = os.environ.get("MONGO_USER") or input("DB user: ")
        MONGO_PASS = os.environ.get("MONGO_PASS") or getpass.getpass("User password: ")

        # 連線到mongodb
        monclient = pymongo.MongoClient(
            f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/?authSource={MONGO_DB}"
        )

        # 查詢目前資料庫版本號
        server_info = monclient.server_info()
        version = server_info.get("version")
        print(f"目前資料庫版本號: {version}")

        # 查詢目前擁有的資料庫
        db_list = monclient.list_database_names()

        for dbname in db_list:
            print(dbname)

        return monclient
    except Exception as e:
        print("資料庫發生錯誤", e)
