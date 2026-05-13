from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from io import StringIO
import MySQLdb
from dotenv import load_dotenv
import os
import getpass

load_dotenv(".env", override=True)

# 讀取帳密(優先從環境變數存取，不存在才互動式要求）
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 3307))
DB_USER = os.environ.get("DB_USER") or input("DB user: ")
DB_PASSWORD = os.environ.get("DB_PASSWORD") or getpass.getpass("DB password: ")
DB_NAME = os.environ.get("DB_NAME", "testdb2")

try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(
        host=DB_HOST,  # 主機名稱
        user=DB_USER,  # 帳號
        password=DB_PASSWORD,  # 密碼
        database=DB_NAME,  # 資料庫
        port=DB_PORT,  # port
        charset="utf8",
    )  # 資料庫編碼
except Exception as e:
    print("資料庫連接失敗：", e)
    os._exit(1)

try:

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.nba.com/stats/players/traditional?Season=2024-25")
    # driver.maximize_window()    # 將視窗最大化

    time.sleep(2)
    # 把cookie畫面取消掉
    cookie = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookie.click()
    time.sleep(2)
    # 滑鼠滾輪往下滾300像素
    driver.execute_script("window.scrollTo(0,300)")

    page = 1
    while True:
        # Remove propaganda
        prop = driver.find_element(By.CSS_SELECTOR, "#bx-close-inside-3074827")
        if not prop is None:
            prop.click()
        soup = BeautifulSoup(driver.page_source, "lxml")

        # 確認目前總頁數
        pageloc = soup.find(
            "div", {"class": "Pagination_content__xgsey Crom_cromSetting__Md_cl"}
        )
        page_num = pageloc.find_all("div")
        totalpage = page_num[6].text.split(" ")[1]

        # 先找到存放NBA球員資料的table
        table = soup.select_one(
            "#__next > div.Layout_base__7MdPl > div.Layout_mainContent__Gr_Jz > div.MaxWidthContainer_mwc__ChCs_ > section.Block_block__R72zC.nba-stats-content-block > div > div.Crom_base__heTBP > div.Crom_container__kd1FW.crom-container > table"
        )

        # 將球員資料放到dataframe中再寫成csv檔
        df = pd.read_html(StringIO(str(table)))
        df = df[0]

        try:
            # 使用cursor()方法操作資料庫
            cursor = conn.cursor()
            for i in range(len(df)):
                sql = "INSERT INTO nba (player, team, age) \
                       VALUES(%s, %s, %s)"
                var = (df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3])
                cursor.execute(sql, var)

            # 當資料寫完後要送出事件，以確保剛的資料有成功寫入
            conn.commit()

        except Exception as e:
            print(e)

        try:
            # 資料庫寫入完畢後等待4秒再按下下一頁的按鈕
            time.sleep(4)
            driver.find_element(
                By.XPATH,
                '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]',
            ).click()

            # 判定是否按到最後一頁
            if page < int(totalpage):
                page += 1
                continue
            else:
                print("下載完畢")
                break

        except Exception as e:
            print("下載失敗：", e)

except Exception as e:
    print("爬取失敗：", e)

finally:
    driver.quit()
