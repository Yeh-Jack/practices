import os, re, ssl
import requests as req

# import requests as req
from bs4 import BeautifulSoup as bs

SKIP_ONE_LINE = "\n\n"


def crawlOk(uri, res):
    print(f"HTTP status code = {res.status_code}", end=SKIP_ONE_LINE)
    if res.status_code != req.codes.ok:
        # raise HTTPException(status_code=404, detail="Video not found")
        print(f"Unable to crawl this page: [{uri}]")
        os._exit(1)


# cwd = os.getcwd()
# # cwd = os.getcwd() + "/.."
# imgPath = cwd + "/data/img/"
# print(f"--->>>   Saving images to the folder: {imgPath}   <<<---", end=SKIP_ONE_LINE)
# if not os.path.exists(imgPath):
#     os.mkdir(imgPath)

# --- Momo
# urlBase = "https://www.momoshop.com.tw/search/"
# url = urlBase + "searchShop.jsp?keyword=Raspberry+Pi"


# --- Yahoo News
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


url = "https://tw.news.yahoo.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
}
res = req.get(url, headers=headers)
crawlOk(url, res)
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


# --- PTT (uses cookies to skip adult confirmation page)
url = "https://www.ptt.cc/bbs/Gossiping/index38877.html"
res = req.get(url, cookies={"over18": "1"})
crawlOk(url, res)
res.encoding = "utf-8"
soup = bs(res.text, "lxml")
# Make a fake <a> tag to replenish if it's absent.
DELETED = bs('<a href="deleted">本文已被刪除</a>', "lxml").a

for div in soup.find_all("div", "r-ent"):
    # --- Replenish a `deleted <a>` tag for process in the same way.
    aTag = div.find("a") or DELETED  # Now, aTag definitely existing.
    print(f"{aTag.text.strip()}")  # Print the text directly without error.

    # --- Test None aTag by if
    # aTag = div.find("a")
    # if aTag == None:
    #     print("--->>  本文已被刪除  <<---")
    # else:
    #     title = aTag.text.strip()
    #     print(f"{title}")
