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

# Get the page
uri = "https://www.taiwanlottery.com/lotto/result/super_lotto638"
chrome.get(uri)
chrome.implicitly_wait(2)
# time.sleep(2)
print(f"\n\t<<[ {chrome.title} ]>>", end=SKIP_ONE_LINE)

# # Query a specifc sec.
# while True:
#     sec = input("查詢期別：")  # 115000037
#     if not sec.isdigit():
#         break

#     # Fill input data.
#     inp = chrome.find_element(By.ID, "el-id-1024-3")
#     inp.clear()
#     inp.send_keys(sec)
#     # Click the query button.
#     chrome.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
#     time.sleep(1)
#     # Crawl numbers
#     numbers = chrome.find_elements(By.CLASS_NAME, "secondary-area")
#     print(f"期別：{sec}\t中獎號：", end="")
#     for i in numbers[:-1]:
#         print(i.text, end=" ")
#     print(f" 特別號：[{numbers[-1].text}]", end=SKIP_ONE_LINE)

# Query by month
chrome.find_element(By.XPATH, '//*[@id="date_picker_98"]').click()
table = chrome.find_element(
    By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div/div[2]/table"
)
disabled = table.find_elements(By.CLASS_NAME, "disabled")
spans = table.find_elements(By.TAG_NAME, "span")
print(f"{len(spans)} month buttons, {len(disabled)} disabled.")

# Traverse enabled months button in decending order.
for m in range(len(spans) - len(disabled) - 1, 0, -1):
    spans[m].click()
    time.sleep(2)
chrome.quit()
