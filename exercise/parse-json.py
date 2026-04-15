import json
import os

cwd = os.getcwd()
print(f"Current work directory = [{cwd}]", end="\n\n")

with open("data/json/drugstore.json", encoding="utf-8-sig") as file:
    data = json.load(file)

attrs = [
    "機構狀態",
    "機構名稱",
    "地址縣市別",
    "地址鄉鎮市區",
    "地址街道巷弄號",
]
found = []
idx = 0

while len(found) < 20:
    row = data[idx]
    store = {}
    for item in row:
        for key, value in item.items():
            if key in attrs:
                store[key] = value
    if store["機構狀態"] == "開業" and store["地址縣市別"] == "新北市":
        found.append(store)

    idx += 1

for i in range(10, 20):
    row = found[i]
    print(f"{row[attrs[1]]}   {row[attrs[2]]}{row[attrs[3]]}{row[attrs[4]]}")
