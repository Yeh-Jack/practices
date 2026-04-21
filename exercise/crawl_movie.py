import requests as rq
import os

cwd = os.getcwd()
print(f"Current working directory = {cwd}")

start = "2020/12/1"
end = "2021/01/31"
url = f"https://boxoffice.tfai.org.tw/api/export?start={start}&end={end}"
headers = {
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    # "Accept-Language": "en-US,en;q=0.5",
    # "Connection": "keep-alive",
    # "Cookie": "_ga_YJ385WSQ1N=GS2.1.s1776405509$o1$g1$t1776405632$j60$l0$h0; _ga=GA1.1.268486387.1776405510",
    # "Host": "boxoffice.tfai.org.tw",
    # "Priority": "u=0, i",
    # "Sec-Fetch-Dest": "document",
    # "Sec-Fetch-Mode": "navigate",
    # "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    # "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
}

response = rq.request("GET", url, headers=headers)
dataPath = cwd + "/data/json/"
with open(dataPath + "movies.json", "w") as file:
    file.write(response.text)
json = response.json()["list"]
print(f"Size of source list = [{len(json)}]")

compareKey = "totalTickets"
# tickets = sorted([movie[compareKey] for movie in json])
top10 = json[-10:]
top10.reverse()
# top_10 = sorted(json, key=lambda x: x[compareKey], reverse=True)[:10]
for i, item in enumerate(top10, 1):
    print(
        f"{i}. {item['name']}: Tickets sold: {item[compareKey]}, Amount: {item["totalAmounts"]}"
    )
print()
