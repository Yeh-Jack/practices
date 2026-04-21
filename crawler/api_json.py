import csv
import pandas
import requests as rq

SKIP_ONE_LINE = "\n\n"

# OpenData API address of the YouBike JSON data.
print("===============   YouBike   ===============")
url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json"
rsp = rq.request("GET", url, verify=False)  # Skip SSL certificate verification.
data = rsp.json()  # Extract data from the response object in JSON format.

# json = [{
#     "scity": "新北市",
#     "scityen": "New Taipei City",
#     "sna": "YouBike2.0_下庄市場",
#     "sarea": "八里區",
#     "ar": "舊城路21號(前)",
#     "snaen": "YouBike2.0_Shia Juang Market",
#     "sareaen": "Bali Dist",
#     "aren": "No.21, Jiucheng Rd., Bali Dist",
#     "sno": "500201001",
#     "tot_quantity": "20",
#     "sbi_quantity": "5",
#     "mday": "20260416T103503",
#     "lat": "25.14678",
#     "lng": "121.3999",
#     "bemp": "15",
#     "act": "1",
#     "yb2_quantity": "3",
#     "eyb_quantity": "2",
# }]

for bike in data:
    shrinkSna = bike["sna"].replace("YouBike2.0_", "")  # Remove the SNA prefix.
    print(
        f"站點：{shrinkSna}, 地址：{bike['ar']}, 總停車格：{bike['tot_quantity']}, 車輛數：{bike['sbi_quantity']}, 空位數：{bike['bemp']}, 資料時間：{bike['mday']}."
    )
print()

print("===============   電影院   ===============")
url = "https://data.ntpc.gov.tw/api/datasets/61c99f42-8a90-4adc-9c40-ba9e0ea097aa/csv"
rsp = rq.request("GET", url, verify=False)
data = list(csv.reader(rsp.text.split()))

# The CSV format is: ['name', 'address', 'tel', 'number']
df = pandas.DataFrame(data[1:], columns=["電影院名稱", "地址", "電話", "廳數"])
df.index += 1
print(df, end=SKIP_ONE_LINE)
