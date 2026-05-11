from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, os
import requests
import pandas as pd
import MySQLdb
from dotenv import load_dotenv
import getpass
            
load_dotenv("./.env", override=True)

# 讀取帳密(優先從環境變數存取，不存在才互動式要求）
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 3307))
DB_USER = os.environ.get("DB_USER") or input("DB user: ")
DB_PASSWORD = os.environ.get("DB_PASSWORD") or getpass.getpass("DB password: ")
DB_NAME = os.environ.get("DB_NAME", "testdb2")

# 建立存放圖片的資料夾
folder_name = "./hero"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

try:
    #使用selenium自動開啟瀏覽器，並打開英雄聯盟官網
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    url = "https://www.leagueoflegends.com/zh-tw/champions/"
    driver.get(url)
    
    time.sleep(5)
    # 用bs4解析網頁
    soup = BeautifulSoup(driver.page_source, "lxml")
    # 英雄圖片路徑
    all_imgs = soup.find_all("img", {"data-testid": "mediaImage"})
    # 英雄名稱
    all_names = soup.find_all("div", {"class":"sc-ce9b75fd-0 lmZfRs"})
    # 英雄資料網址
    all_hero_url = soup.find_all("a", {"class":"sc-b988531e-0 bvEIZU sc-d043b2-0 bZMlAb"})
    
    # 放英雄資料
    heroData = []
    for img, name, url in zip(all_imgs, all_names, all_hero_url):

        img_url = img.get("src").split("?")[0]
        hero_url = url.get("href")
        
        try:
            response = requests.get(img_url)
            response.raise_for_status()
            # 下載英雄圖片
            file_path = os.path.join(folder_name, "%s.jpg" %name.text)
            with open(file_path, "wb") as f:
                f.write(response.content)
                
        except Exception as e:
            print("下載失敗：%s, 原因：%s" %(name.text, e))
        
        time.sleep(1)
        # 開新分頁至各別英雄頁面
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.leagueoflegends.com"+hero_url)
        hero_info = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div/section[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/p[2]').text
        
        # 關閉英雄頁面切回總表
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
                
        heroData.append([img_url, name.text, hero_info])    
        
        time.sleep(1)
        
    data = pd.DataFrame(heroData, columns=["圖片連結","英雄", "英雄類別"])
    # data.to_csv("英雄資料.csv")
    
except Exception as e:
    print(e)
    
finally:
    driver.quit()

# 整理資料
heroCategory = pd.Series(list(data.groupby("英雄類別").groups)).reset_index().rename(columns={"index":"類別編號", 0:"英雄類別"})
category_map = dict(zip(heroCategory["英雄類別"], heroCategory["類別編號"]))
data["類別代碼"] = data["英雄類別"].map(category_map)

image_binaries = []
for index, row in data.iterrows():
    hero_name = row["英雄"]
    file_path = os.path.join(folder_name, "%s.jpg" %(hero_name)) 
    
    try:
        with open(file_path, "rb") as f:
            image_binary = f.read()
            image_binaries.append(image_binary)
            
    except FileNotFoundError:
        print("找不到圖片檔案：%s，使用None代替。" %(file_path))
        image_binaries.append(None)
data["圖片二進制"] = image_binaries

# 將資料寫入資料庫
try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(host=DB_HOST,          # 主機名稱
                            user=DB_USER,         # 帳號
                            password=DB_PASSWORD, # 密碼
                            database =DB_NAME,    # 資料庫
                            port=DB_PORT,         # port
                            charset="utf8")       # 資料庫編碼
    
    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()
    
    # 將資料data寫到資料庫中
    try:
        
        for i in range(len(data)):
            sql = "INSERT INTO herodata (name, category_id, url, img) VALUES (%s, %s, %s, %s)"
            var = ( 
                data.iloc[i,1], # 英雄名
                data.iloc[i,3], # 類別代碼
                data.iloc[i,0], # url
                MySQLdb.Binary(data.iloc[i,4]) if data.iloc[i,4] is not None else None) # 圖片二進制     
            cursor.execute(sql, var)
            
        conn.commit()

        print("英雄資料寫入完成")
        
    except Exception as e:
        print("錯誤訊息：", e)
        conn.rollback()
    
    try:
        
        for i in range(len(heroCategory)):
            sql = "INSERT INTO herocategory VALUES (%s, %s)"
            var = ( heroCategory.iloc[i,0], heroCategory.iloc[i,1])     
            cursor.execute(sql, var)
            
        conn.commit()
        print("類別資料寫入完成")
        
    except Exception as e:
        print("錯誤訊息：", e)
    
    conn.close()
 
except Exception as e:
    print("資料庫連接失敗：", e)
    
finally:
    print("資料庫連線結束")
