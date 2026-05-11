import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

SKIP_ONE_LINE = "\n\n"

# firefox = webdriver.Firefox()
# firefox.implicitly_wait(5)
# firefox.quit()

# cwd = os.getcwd()
filePath = os.path.abspath("data/SeleniumTest.html")
uri = "file://" + filePath

chrome = webdriver.Chrome()
chrome.implicitly_wait(5)

# uri = "https://example.com/"
chrome.get(uri)
print(f"\nPage title = [{chrome.title}]", end=SKIP_ONE_LINE)

content = chrome.find_element(By.CLASS_NAME, "content")
print(f"Find by class : [{content.text}]", end=SKIP_ONE_LINE)

content = chrome.find_element(By.PARTIAL_LINK_TEXT, "消")
print(
    f"href of the [{content.text}] link is : [{content.get_attribute("href")}]",
    end=SKIP_ONE_LINE,
)

chrome.quit()
