# 抓取台銀匯率資訊

import threading
import time

import requests
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime, strptime, mktime
from datetime import datetime
from os.path import exists

# 子執行緒的工作函數
# def job():
while True:
    html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
    bsObj = BeautifulSoup(html.content, "lxml")
    for single_tr in (
        bsObj.find("table", {"title": "牌告匯率"}).find("tbody").findAll("tr")
    ):
        cell = single_tr.findAll("td")
        currency_name = cell[0].find("div", {"class": "visible-phone"}).contents[0]
        currency_name = currency_name.replace("\r", "")
        currency_name = currency_name.replace("\n", "")
        currency_name = currency_name.replace(" ", "")
        currency_rate = cell[2].contents[0]
        print(currency_name, currency_rate)

        file_name = "E2-1-1-1" + currency_name + ".csv"
        now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        if not exists(file_name):
            data = [["時間", "匯率"], [now_time, currency_rate]]
        else:
            data = [[now_time, currency_rate]]
        f = open(file_name, "a")
        w = csv.writer(f)
        w.writerows(data)
        f.close()

        # print("Child thread:")
    time.sleep(60)

# # 建立一個子執行緒
# child_thread = threading.Thread(target = job)

# # 執行該子執行緒
# child_thread.start()

# # 主執行緒繼續執行自己的工作
# print("Main thread:")
# time.sleep(60)

# # 等待 t 這個子執行緒結束
# child_thread.join()

# print("Done.")
