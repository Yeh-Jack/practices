from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from io import StringIO
import os, time
import pandas as pd

# Create folder if it doesn't exist
DATA_PATH = "data/csv/nba"
os.makedirs(DATA_PATH, exist_ok=True)

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.nba.com/stats/players/traditional")
    # driver.maximize_window()    # 將視窗最大化

    time.sleep(2)
    # 把cookie畫面取消掉
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    time.sleep(1)
    # 滑鼠滾輪往下滾300像素 (to avoid data table is covered by advertisement window).
    driver.execute_script("window.scrollTo(0,300)")

    page = 1
    # Crawl all pages.
    while True:
        time.sleep(1)
        # Remove advertisement
        try:
            # Try to get the non-blocking advertisement window if exists.
            driver.find_element(By.CSS_SELECTOR, "#bx-close-inside-3074827")

            # Try to remove the non-blocking advertisement window.
            i = 0
            while i < 5:
                try:
                    # Remove the non-blocking advertisement window.
                    driver.find_element(
                        By.CSS_SELECTOR, "#bx-close-inside-3074827"
                    ).click()
                    print("--> Non-blocking advertisement removed !!!")
                    break
                except Exception as e:
                    time.sleep(1)  # If failed to remove, wait for 1 second and retry.
                finally:
                    i += 1
        except Exception as err:
            page = page
        finally:
            print(f"Parsing page {page} ...")
        soup = BeautifulSoup(driver.page_source, "lxml")

        # 先找到存放NBA球員資料的table
        table = soup.find("table", class_="Crom_table__PJugT")

        # 將球員資料放到dataframe中再寫成csv檔
        df = pd.read_html(StringIO(str(table)))
        df[0].to_csv(f"{DATA_PATH}/NBA球員資料第{page}頁.csv")
        print(f"--> 已儲存第 {page} 頁.")

        try:
            # Get page operation buttons group.
            pageOps = driver.find_elements(By.CLASS_NAME, "Pagination_button__7JMDL")
            nextPage = pageOps[1]  # [0] is backward, [1] is forward.
            # 判定是否按到最後一頁
            if nextPage.is_enabled():
                nextPage.click()
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
