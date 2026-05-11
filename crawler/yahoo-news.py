import requests as req
from bs4 import BeautifulSoup as bs

SKIP_ONE_LINE = "\n\n"

url = "https://tw.news.yahoo.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
}
res = req.get(url, headers=headers)
print(f"HTTP status code = {res.status_code}", end=SKIP_ONE_LINE)
if res.status_code != req.codes.ok:
    raise Exception(status_code=res.status_code)

def crawlSection(blockName: str, findClaz: str):
    print(f"   ----->>>   {blockName}   <<<-----")
    print("=======================================")
    # Use CSS selector
    aTags = (
        soup.find(id="Col1-3-CategoryWrapper-Proxy")
        .find("div", {"class": findClaz})
        .find_all("a")
    )
    i = 0
    lines = 0
    while lines < 3:
        aTag = aTags[i]
        text = aTag.text.strip()
        if len(text) > 0:
            print(f"{aTag.text}")
            lines = lines + 1
        i = i + 1
    print()


res.encoding = "utf-8"
soup = bs(res.text, "lxml")
# --- Crawl Real-time news:
crawlSection(
    "Left Block",
    "Fl(start)",
)

# --- Crawl Special recommendations:
crawlSection(
    "Right Block",
    "Fl(end)",
)
