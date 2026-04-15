from xml.dom import minidom
import os

# import pandas as pd
# import MySQLdb

# 用os.listdir()查詢data資料夾裡有幾個檔案
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

dirpath = "./data/xml/earthquake"
allfile = os.listdir(dirpath)

newdata = []

# 用迴圈讀取XML內的資料
for i in range(len(allfile)):
    fp = dirpath + "/" + allfile[i]
    # 解析XML文件
    tree = minidom.parse(fp)
    # 找到所有<EarthquakeInfo>節點
    earthquake_info = tree.getElementsByTagName("EarthquakeInfo")
    # 進入每一個<EarthquakeInfo>節點後
    # 找出每個地震的發生時間、緯(lat)經(lon)度
    for child in earthquake_info:
        # getElementsByTagName("OriginTime")：找尋<EarthquakeInfo>標籤中是否有名為<OriginTime>的子標籤
        # getElementsByTagName()回傳結果為list，所以要用索引方式取得結果
        # .firstChild.nodeValue則會取得本文，例如<OriginTime>1991-01-01T11:00:51+08:00</OriginTime>
        # 則會取得字串"1991-01-01T11:00:51+08:00"
        nodeData = []
        for nodeTag in [
            "OriginTime",
            "EpicenterLatitude",
            "EpicenterLongitude",
            "LocalMagnitude",
        ]:
            nodeData.append(child.getElementsByTagName(nodeTag)[0].firstChild.nodeValue)

        # 將資料放入list中
        newdata.append(nodeData)
        print(f"{nodeData}")

# alldata = pd.DataFrame(newdata)
# del newdata
