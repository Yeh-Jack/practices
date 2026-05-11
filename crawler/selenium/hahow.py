import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

SKIP_ONE_LINE = "\n\n"

# cwd = os.getcwd()
# filePath = os.path.abspath("data/SeleniumTest.html")
# uri = "file://" + filePath

chrome = webdriver.Chrome()
chrome.implicitly_wait(3)

# Get the page after loaded 10 seconds.
uri = "https://hahow.in/courses"
chrome.get(uri)
time.sleep(10)
print(f"\nPage title = [{chrome.title}]", end=SKIP_ONE_LINE)

# Get page source.
pageSrc = chrome.page_source
chrome.quit()

# Persist this page.
with open("data/hahow.html", "w") as file:
    file.write(pageSrc)
    print(f"Page source is written.", end=SKIP_ONE_LINE)

# Crawl this page.
soup = bs(pageSrc, "lxml")
for h2 in soup.find_all("h2"):
    text = h2.text
    print(text)
print()
