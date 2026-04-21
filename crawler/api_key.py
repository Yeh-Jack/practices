import requests
import math
from collections import Counter
import os

# Read OMDB API key from environment variable
OMDB_URL = f'http://www.omdbapi.com/?apikey={os.environ.get("OMDB_KEY")}'


def get_data(url):
    # data = json.loads(requests.get(url).text)
    data = requests.get(url).json()
    if data["Response"] == "True":
        return data
    else:
        return None


def search_ids_by_keyword(keywords):
    movie_ids = list()
    query = "+".join(keyword.split())  # e.g., "Iron Man" -> Iron+Man
    page = 0  # Page index for crawl.
    totalPages = 1
    while page < totalPages:
        url = OMDB_URL + "&s=" + query + "&page=" + str(page + 1)
        data = get_data(url)
        if data:
            for item in data["Search"]:
                movie_ids.append(item["imdbID"])

            # 取得搜尋結果總數
            if page == 0:
                total = int(data["totalResults"])
                totalPages = math.ceil(total / 10)
        page += 1
    return movie_ids


def search_by_id(movie_id):
    url = OMDB_URL + "&i=" + movie_id
    return get_data(url)


keyword = input("Input movie name for searching ... ")
m_ids = search_ids_by_keyword(keyword)
print("關鍵字 %s 共有 %d 部影片" % (keyword, len(m_ids)))
print("取得影片資料中...")
movies = list()
for m_id in m_ids:
    movies.append(search_by_id(m_id))
print("影片資料範例 first20:")
for m in movies[:20]:
    print("Title:", m["Title"], "Year:", m["Year"], "imdbID:", m["imdbID"])

years = [m["Year"] for m in movies]
# collections.Counter() 會統計一個 list 中各項目出現的次數, 並回傳一個 dict
year_dist = Counter(years)
print("發行年份分布:", year_dist)
print("發行年份分布:", sorted(year_dist.items()))
# 如果該電影的 'imdbRating' 欄位不是 'N/A' 則轉換其值為 float 並放入 ratings 內
ratings = [float(m["imdbRating"]) for m in movies if m["imdbRating"] != "N/A"]
print("平均評分:", sum(ratings) / len(ratings))
