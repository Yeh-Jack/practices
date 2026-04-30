import requests
from bs4 import BeautifulSoup
import pandas as pd

# import datetime
import MySQLdb


def fixRate(strRate):
    if strRate == "-":
        return None
    else:
        return float(strRate)


# ==============================
#      爬台銀匯率
# ==============================
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

time = soup.find("span", class_="time").text.replace("/", "-")
table = soup.find(
    "table", "table table-striped table-bordered table-condensed table-hover"
)
# 抓取幣別名稱
currency = table.find_all("div", {"class": "hidden-phone print_show xrt-cur-indent"})
# 抓取現金買入及賣出價
bankbuy = table.find_all("td", {"class": "rate-content-cash text-right print_hide"})

# ==============================
#      整理資料
# ==============================
data = []
for i in range(len(currency)):
    currencyName = currency[i].text.strip()
    parts = currencyName.split("(")
    name = parts[0].strip()
    code = parts[1][:-1]

    currencyBuy = fixRate(bankbuy[i * 2].text)
    currencySold = fixRate(bankbuy[i * 2 + 1].text)
    data.append([time, name, code, currencyBuy, currencySold])

# finData = pd.DataFrame(data, columns=["幣別", "幣別碼", "本行買入", "本行賣出"])
# # 將匯率中非數值的值全更換為0
# finData.loc[:, "本行買入"] = finData["本行買入"].replace("-", 0).astype(float)
# finData.loc[:, "本行賣出"] = finData["本行賣出"].replace("-", 0).astype(float)

# 取得今日日期
# today = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

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
        # pdToTuple = [
        #     (time, str(row[0]), str(row[1]), float(row[2]), float(row[3]))
        #     for row in finData.itertuples(index=False, name=None)
        # ]

        sql = "INSERT INTO twbank_currency (rate_time, currency, code, buy, sell) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(sql, data)
        # cursor.executemany(sql, pdToTuple)

        conn.commit()
        conn.close()
        print("資料寫入完成")

    except Exception as e:
        print("錯誤訊息：", e)

except Exception as e:
    print("資料庫連接失敗：", e)

finally:
    print("資料庫連線結束")
