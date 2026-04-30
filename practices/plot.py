# 圖例的錨點說明
# https://matplotlib.org/stable/users/explain/axes/legend_guide.html
# https://blog.csdn.net/sinat_41299610/article/details/106494549

# 雙y軸 / 雙x軸
# https://www.cnblogs.com/geoli91/p/16166200.html
# https://blog.csdn.net/qq_41677123/article/details/126601090

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd

matplotlib.use("TkAgg")
fontPath = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
fontProp = fm.FontProperties(fname=fontPath)
# plt.rcParams["font.family"] = ["Noto Sans"]

# Generate data.
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)
data = pd.DataFrame(
    {"Bike": [34, 76, 65, 87], "Car": [45, 56, 67, 78], "Fruit": [98, 87, 76, 56]}
)

# # --- Single chart.
# # Set chart attributes.
# plt.title("線形圖", loc="right", fontproperties=fontProp, fontsize=15)
# plt.xlabel("年度", loc="right", fontproperties=fontProp)
# plt.ylabel("Qty", loc="top", rotation=0)
# plt.xticks(range(len(data.Bike)), [x + 2020 for x in range(len(data.Bike))])

# # Draw the chart.
# # plt.plot(x, y, marker="o", markerfacecolor="#0066CC", ls="-.")
# for key in iter(data):
#     sales = data[key].values
#     plt.plot(sales, label=key, marker="o")
#     for idx, value in enumerate(sales):
#         plt.text(idx + 0.025, value + 1, value, color="r")

# plt.legend(loc=4)
# # 設定圖例(圖例位子放置於圖表外)
# # plt.legend(bbox_to_anchor=(0, 1.02 ,1, 0),  # 拿圖例的左下角去對準(0, 1.02)這個點
# #                                             # (1, 0)圖例寬度為1、高度為0
# #            loc=3,                           # 圖例位置(lower left)
# #            ncol=len(data),                  # 圖例資料欄數
# #            mode="expand",                   # 圖例橫向平均分配
# #            borderaxespad=0)                 # 去除圖例與邊界之間的間隙，讓對齊更精準

# -- Declare 2 * 1 plot canvas.
fig, ax = plt.subplots(2, 1)

# -- Draw the first plot located in (0, 0)
# ax[0] = plt.subplot(2, 1, 1)

for key in iter(data):
    sales = data[key].values
    ax[0].plot(sales, label=key, marker="o")
    for idx, value in enumerate(sales):
        ax[0].text(idx + 0.025, value + 1, value, color="r")

# Draw the second bar.
# ax[1] = plt.subplot(2, 1, 2)
width = len(data["Bike"])
ax[1].bar(data.index - width * 2, data["Bike"], color="#345678", label="Bike")
ax[1].text(idx + 0.025, data["Bike"] - 2, data["Bike"], color="r")

plt.show()
