import re

SKIP_ONE_LINE = "\n\n"

# html = """
# <html><head><title>國立臺灣大學系統</title></head>
# <body>
# <p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
# <p class="ntu_system">
# <a href="http://www.ntu.edu.tw/test" class="union" id="link1">臺灣大學</a>
# <a href="https://www.ntnu.edu.tw/req" class="union" id="link2">臺灣師範大學</a>
# <a href="http://www.ntust.edu.tw/exp" class="union" id="link3">臺灣科技大學</a>
# </p></body></html>
# """

# # Find web sites without path.
# pattern = re.compile(r"https?://[\w.]+/") # Finds both of http:// and https:// sites.
# result = pattern.findall(html)
# print(f"Matched: {result}", end=SKIP_ONE_LINE)

# # Reluctant qualified by '?' (find the shortest matching string).
# pattern = re.compile(r"<a.*?>")
# result = pattern.findall(html)
# print(f"Matched: {result}", end=SKIP_ONE_LINE)

import os
import requests as rq
from bs4 import BeautifulSoup

url = "http://blog.castman.net/py-scraping-analysis-book/ch2/blog/blog.html"
res = rq.get(url)
if res.status_code != rq.codes.ok:
    print(f"Unable to crawl this page: {url}")
    os._exit(1)

soup = BeautifulSoup(res.text, "lxml")
for img in soup.find_all("img", {"src": re.compile(r"beginner.*\.png$")}):
    print(img["src"])
print()
