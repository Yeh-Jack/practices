import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import MySQLdb

# ==============================
#      爬台銀匯率
# ==============================
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

table = soup.find(
    "table", "table table-striped table-bordered table-condensed table-hover"
)
# 抓取幣別名稱
currency = table.find_all("div", {"class": "hidden-phone print_show xrt-cur-indent"})
# 抓取現金買入及賣出價
bankbuy = table.find_all("td", {"class": "rate-content-cash text-right print_hide"})


# ==============================
#      將爬下資料寫成dataframe
# ==============================
# 將幣別名稱、買入及賣出分別做成dataframe
data1 = pd.DataFrame(
    ((currency[i].text).strip() for i in range(len(currency))), columns=["幣別"]
)
data2 = pd.DataFrame(
    (bankbuy[i].text for i in range(len(bankbuy)) if i % 2 == 0), columns=["本行買入"]
)
data3 = pd.DataFrame(
    (bankbuy[i].text for i in range(len(bankbuy)) if i % 2 != 0), columns=["本行賣出"]
)

# 將三份資料合併(以欄合併)
alldata = pd.concat([data1, data2, data3], axis=1)
# 將匯率中非數值的值全更換為0
alldata["本行買入"] = alldata["本行買入"].replace("-", 0).astype(float)
alldata["本行賣出"] = alldata["本行賣出"].replace("-", 0).astype(float)

# 取得今日日期
today = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

# ==============================
#      將資料寫入資料庫
# ==============================

try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(
        host="127.0.0.1",  # 主機ip
        user="jack",  # 帳號
        password="jack",  # 密碼
        port=3306,  # 通訊埠
        database="testdb",  # 資料庫
        charset="utf8",  # 資料庫編碼
    )

    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()

    # 將資料data寫到資料庫中
    try:
        pdToTuple = [
            (today, str(row[0]), float(row[1]), float(row[2]))
            for row in alldata.itertuples(index=False, name=None)
        ]

        sql = "INSERT INTO twbank_currency VALUES(%s, %s, %s, %s)"
        cursor.executemany(sql, pdToTuple)

        conn.commit()
        conn.close()
        print("資料寫入完成")

    except Exception as e:
        print("錯誤訊息：", e)

except Exception as e:
    print("資料庫連接失敗：", e)

finally:
    print("資料庫連線結束")
