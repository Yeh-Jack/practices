from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from io import StringIO
import MySQLdb

try:
  
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.nba.com/stats/players/traditional")
    # driver.maximize_window()    # 將視窗最大化
    
    time.sleep(2)
    # 把cookie畫面取消掉
    cookie = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[1]')
    cookie.click()
    time.sleep(2)
    # 滑鼠滾輪往下滾300像素
    driver.execute_script("window.scrollTo(0,300)")
    
    page = 1
    
    while True:        
        soup = BeautifulSoup(driver.page_source, "lxml")
        
        # 確認目前總頁數
        pageloc = soup.find("div", {"class":"Pagination_content__xgsey Crom_cromSetting__Md_cl"})
        page_num = pageloc.find_all("div")
        totalpage = page_num[6].text.split(" ")[1]
      
        # 先找到存放NBA球員資料的table
        table = soup.select_one("#__next > div.Layout_base__7MdPl > div.Layout_mainContent__Gr_Jz > div.MaxWidthContainer_mwc__ChCs_ > section.Block_block__R72zC.nba-stats-content-block > div > div.Crom_base__heTBP > div.Crom_container__kd1FW.crom-container > table")
        
        # 將球員資料放到dataframe中再寫成csv檔
        df = pd.read_html(StringIO(str(table)))
        df[0].to_csv("NBA球員資料第%d頁.csv" %page)
        print("正在儲存第%d頁..." %page)               
        
        try:
            # csv檔下載完畢後等待2秒再按下下一頁的按鈕
            time.sleep(4)    
            driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]').click()
            
            # 判定是否按到最後一頁
            if page < int(totalpage):
                page += 1                
                continue
            else:
                print("下載完畢")
                break
        
        except Exception as e:
            print("下載失敗：", e)    
                                       
except Exception as e:
    print("爬取失敗：", e)

finally:
    driver.quit() 