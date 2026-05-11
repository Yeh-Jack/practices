import os, re, ssl
import urllib.request as req

# import requests as req
from bs4 import BeautifulSoup as bs

SKIP_ONE_LINE = "\n\n"

cwd = os.getcwd()
# cwd = os.getcwd() + "/.."
imgPath = cwd + "/data/img/"
print(f"--->>>   Saving images to the folder: {imgPath}   <<<---", end=SKIP_ONE_LINE)
if not os.path.exists(imgPath):
    os.mkdir(imgPath)

ssl._create_default_https_context = ssl._create_unverified_context  # For urllib
url = "https://www.edu.tw"
# --- Use urllib to crawl the page and feed it to BeautifulSoup.
html = req.urlopen(url)
html_text = html.read().decode("utf-8")  # decode bytes to string
soup = bs(html_text, "lxml")
# --- Use requests to crawl the page and feed it to BeautifulSoup.
# html = req.get(url, verify=False)
# html.encoding = "utf-8"
# soup = bs(html.text, "lxml")
for img in soup.find_all("img"):
    src = img.get("src")
    if src != None and (re.search(r"\.(jpg|png)$", src)):
        fileName = src.split("/")[-1]  # Get file name from the 'src' URL
        if not src.startswith("http"):
            if src.startswith("/"):
                src = url + src
            else:
                src = url + "/" + src
            print(f"Convert relative to obsolute URL: {src}")
        try:
            resImg = req.urlopen(src)
            imgFilePath = os.path.join(imgPath, fileName)
            print(f"Saving {src} ...")
            with open(imgFilePath, "wb") as f:
                f.write(resImg.read())
            print(f"\t--> {fileName} is saved.")
        except Exception as e:
            print(f"\t--> Unable to persist [{src}].")
