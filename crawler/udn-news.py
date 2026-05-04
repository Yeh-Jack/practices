import os
import requests as rq
from bs4 import BeautifulSoup as bs

SKIP_ONE_LINE = "\n\n"
url = "https://udn.com/news/index"
res = rq.get(url)
if res.status_code != rq.codes.ok:
    print(f"Unable to crawl this page: {url}")
    os._exit(1)

soup = bs(res.text, "lxml")

# --- Crawl Real-time news:
print("--->>>   Real-Time News   <<<---")
print("================================", end=SKIP_ONE_LINE)
# Use CSS selector
for aTag in soup.select("div.context-box:nth-child(2) > div:nth-child(1) > a"):  # 即時
    print(f"{aTag["title"]} > {aTag["href"]}")
print()

# --- Crawl Special recommendations:
print("--->>>   Special Recommendations   <<<---")
print("=========================================", end=SKIP_ONE_LINE)
# Use find & find_all
aTags = soup.find(
    "div", {"class": "story-list__holder story-list__holder--big"}
).find_all("a")
for aTag in aTags:
    print(f"{aTag.text.strip()} > {aTag["href"]}")
print()
