import MySQLdb
import pandas as pd
import matplotlib.pyplot as plt
import sys

# ======================
# 設定中文
# ======================
plt.rcParams["font.family"] = ["Microsoft JhengHei", "sans-serif"]
plt.rcParams["font.size"] = 10
plt.rcParams["axes.unicode_minus"] = False

# ======================
# 資料庫連接取得data
# ======================
key = input("請輸入要查詢的縣市名稱：")

try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(
        host="127.0.0.1",  # 主機ip
        user="jack",  # 帳號
        password="jack",  # 密碼
        port=3306,  # 通訊埠
        database="testdb",
    )  # 資料庫

    # 使用cursor()方法操作資料庫
    cursor = conn.cursor()

    try:
        # 先確認使用者輸入的縣市是否正確
        sql = "SELECT count(if('%s' = left(site,3), 'True', NULL)) \
               FROM towndata " % (key)

        cursor.execute(sql)
        data = cursor.fetchone()

        # 若使用者輸入縣市正確則將資料丟入DataFrame
        if data[0] != 0:
            sql = "SELECT * \
                    FROM towndata \
                    WHERE site LIKE '%s' \
                    ORDER BY people_total DESC \
                    limit 5" % (key + "%")
            # " %(key+'%')
            cursor.execute(sql)
            data = cursor.fetchall()
            citydata = pd.DataFrame(
                data, columns=["統計年", "區域別", "年底人口數", "土地面積", "人口密度"]
            )

        # 若縣市錯誤則強制終止程式
        else:
            print("輸入縣市名有誤(例如請打臺北市)")
            sys.exit(0)

        cursor.close()
        conn.close()

    except Exception as e:
        print("錯誤訊息：", e)

except Exception as e:
    print("資料庫連接失敗：", e)


# ======================
# 設定畫布
# ======================
plt.figure(figsize=(10, 4))

# ======================
# 繪製圖表
# ======================
# x與y軸
x = [i for i in range(len(citydata))]
y = [citydata.iloc[i, 2] for i in range(len(citydata))]

# 使用colormap(顏色圖函數)
cm = plt.get_cmap("RdPu")
# 參數範圍為0.0~1.0
color_maps = [cm(0.9), cm(0.7), cm(0.5), cm(0.4), cm(0.2)]

# 長條圖
plt.bar(x, y, width=0.6, color=color_maps, zorder=10)

# 將x軸更改為區域名
name = [citydata.iloc[i, 1][3:] for i in range(len(citydata))]
plt.xticks(x, name, rotation=0)

# 設定資料標籤
for i, value in enumerate(citydata["年底人口數"]):
    plt.text(i, value, value, ha="center", va="bottom", fontsize=10)

# 調整y軸刻度
plt.ylim(0, citydata.iloc[0, 2] + 20000)

# 設定標題
plt.title(key + "113年底人口數", size=20)

# 設定網格
plt.grid(axis="y", zorder=0)

plt.show()
