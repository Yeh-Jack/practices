import requests as rq

url = "http://tqc.codejudger.com:3000/target/5205.json"
response = rq.request("GET", url)
json = response.json()

# dataPath = "./data/json/"
# with open(dataPath + "aqi.json", "w") as file:
#     file.write(response.text)

filter = "新北市"
data = [site for site in json if site.get("County") == filter]
print(f"Size of source list = [{len(json)}], size of filtered = [{len(data)}]")

print(f"{filter} PM2.5 相關資料：", end="\n\n")
for site in data:
    print(f"{site["SiteName"]}：")
    print(f"\tAQI：{site["AQI"]}")
    print(f"\tPM2.5{site["PM2.5"]}")
    print(f"\tPM10：{site["PM10"]}")
    print(f"\t資料更新時間：{site["PublishTime"]}")
print()
