import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys
import os

SKIP_ONE_LINE = "\n\n"
# cwd = os.getcwd()
cwd = os.getcwd() + "/.."
csvPath = cwd + "/data/csv/"
jsonPath = cwd + "/data/json/"
xmlPath = cwd + "/data/xml/"


# 設定中文
# plt.rcParams["font.family"] = ["DejaVu Sans"]
plt.rcParams["font.family"] = "SimHei"  # or any font you've installed
plt.rcParams["font.size"] = 10

try:
    # 讀取資料
    data = pd.read_csv(csvPath + "113年度各鄉鎮市區人口密度.csv", header=1, nrows=370)
    # 調整區域別欄位，將縣市與鄉鎮分成兩欄
    data["縣市"] = data["區域別"].str[:3]
    data["鄉鎮"] = data["區域別"].str[3:]
    # 重新排列欄位順序
    new_data = data[["統計年", "縣市", "鄉鎮", "年底人口數", "土地面積", "人口密度"]]
    # 清理資料
    # new_data.loc[:, "年底人口數"] = new_data["年底人口數"].replace("… ", 0).astype(int)
    # new_data.loc[:, "人口密度"] = new_data["人口密度"].replace("… ", 0).astype(int)
    new_data["年底人口數"] = new_data["年底人口數"].replace("… ", 0).astype(int)
    new_data["人口密度"] = new_data["人口密度"].replace("… ", 0).astype(int)

except IOError as e:
    print("檔案路徑不正確", e)
    sys.exit(0)

# 使用遮罩查詢新竹縣的資料
county = ""
while county == "":
    county = input("請輸入要查詢的縣市名稱：")
    if county in new_data["縣市"].values:
        countyData = new_data["縣市"] == county
    else:
        print("輸入的縣市名稱不正確")
        county = ""

fig, ax = plt.subplots(1, 1)
plt.figure(figsize=(16, 4))
# 繪制折線圖
plt.plot(
    range(len(new_data[countyData]["年底人口數"])),
    new_data[countyData]["年底人口數"],
    marker="h",
    c="#2D70F0",
)

# 修改x軸標籤
plt.xticks(
    range(len(new_data[countyData]["年底人口數"])),
    new_data[countyData]["鄉鎮"],
    rotation=45,
)

# 增加文字標籤
for i, value in enumerate(new_data[countyData]["年底人口數"]):
    plt.text(i, value + 500, "{:,}".format(value), ha="center", va="bottom")

# 幫y軸加千分位
ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ","))
)

# 圖表標題
plt.title("113年度%s年底人口數" % (county))

max = new_data[countyData]["年底人口數"].max()
buffer = max * 1.05
plt.ylim(
    new_data[countyData]["年底人口數"].min() - buffer,
    new_data[countyData]["年底人口數"].max() + buffer,
)

# 顯示圖表
plt.show()
