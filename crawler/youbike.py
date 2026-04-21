import xml.etree.ElementTree as ET
import os
import urllib
import ssl

# urlopen https需要SSL驗證
# 使用ssl._create_unverified_context將驗證關閉，以避免錯誤訊息跳出
ssl._create_default_https_context = ssl._create_unverified_context

# 資料來源
tree = ET.parse("新竹youbike.xml")

# 找尋根節點
root = tree.getroot()

ubikedata = []      # 存放新竹ubike資料
fail_download = []  # 存放下載失敗的圖檔名

for child in root:
    tmp = []
    for grandchild in child:
        tmp.append(grandchild.text)

    ubikedata.append(tmp)

# 若桌面上沒有新竹ubike資料夾，則自動產生一個
img_file = "./新竹ubike"
if not os.path.exists(img_file):
    os.mkdir(img_file)
    
for row in ubikedata:
    img_path = row[3]  # 找出圖檔的路徑
    
    try:
        # 向圖檔路徑請求連線
        # 若請求server回傳狀態碼為200時則將該圖存入桌面的新竹ubike資料夾中
        # 圖片檔名為<站點名稱>標籤內的值
        image = urllib.request.urlopen(img_path)  
        img_download = open(os.path.join(img_file, row[0]+".jpg"), "wb")
        img_download.write(image.read())
        print("%s下載中" %row[0])
    
    except Exception as e:
        fail_download.append(row[0])
        print("下載失敗：%s, %s" %(row[0],e))
        
        