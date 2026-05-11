from time import sleep
import requests as req
from bs4 import BeautifulSoup as bs

SKIP_ONE_LINE = "\n\n"
SITE = "https://www.ptt.cc"


def crawlPage(url: str):
    # --- PTT (uses cookies to skip adult confirmation page)
    res = req.get(url, cookies={"over18": "1"})
    # print(f"HTTP status code = {res.status_code}", end=SKIP_ONE_LINE)
    if res.status_code != req.codes.ok:
        raise Exception(status_code=res.status_code)

    res.encoding = "utf-8"
    soup = bs(res.text, "lxml")
    return soup


def extractPageNo(url: str):
    fileName = url.split("/")[-1]
    page = fileName[5:-5]
    return int(page)


def extractThreads(soup, crawled: int, limit: int, hotOnly: bool):
    for div in soup.find_all("div", "r-ent"):
        aTag = div.find("a")
        span = div.find("span")
        if span is None:
            span = "  "
            isHot = False
        else:
            span = span.text.strip()
            isHot = span == "爆"

        if (aTag != None) and ((not hotOnly) or isHot):
            link = SITE + aTag.get("href")
            title = aTag.text.strip()
            author = div.find("div", "author").text.strip()
            crawled = crawled + 1
            print(f"{crawled:03}: [{span}] {title} ({author})\n\t{link}")

        if crawled >= limit:
            break
    print("\t\t--->>  Paused for 2 seconds ...  <<---", end=SKIP_ONE_LINE)
    sleep(2)
    return crawled


def getLastPage(soup):
    previous = soup.select("a.wide:nth-child(2)")
    url = previous[0].get("href")
    return "https://www.ptt.cc" + url


def getUrlByPageNo(pageNo: int):
    page = ""
    if pageNo > 0:
        page = str(pageNo)
    url = f"https://www.ptt.cc/bbs/Gossiping/index{page}.html"
    return url


# --- Get newest 100 threads
print("--->>  Get the newest 100 threads from PTT Gossiping  <<---", end=SKIP_ONE_LINE)
pageNo = 0
threads = 0
limit = 100
lastPage = ""
while threads < limit:
    url = getUrlByPageNo(pageNo)
    # --- PTT (uses cookies to skip adult confirmation page)
    soup = crawlPage(url)
    # Get the last page number from the "previous page" link of the first page.
    if lastPage == "":
        lastPage = getLastPage(soup)
    threads = extractThreads(soup, threads, limit, False)
    pageNo = pageNo + 1
print()

# --- Get oldest threads.
print("--->>  Get the oldest 50 HOT threads from PTT Gossiping  <<---")
print(f"\t->  The last page is [{lastPage}]", end=SKIP_ONE_LINE)
pageNo = extractPageNo(lastPage)
threads = 0
limit = 50
while threads < limit:
    url = getUrlByPageNo(pageNo)
    # --- PTT (uses cookies to skip adult confirmation page)
    soup = crawlPage(url)
    threads = extractThreads(soup, threads, limit, True)
    pageNo = pageNo - 1
print()
