from bs4 import BeautifulSoup
import requests as rq
import os

# Read OMDB API key from environment variable
apiKey = os.environ.get("OMDB_KEY")

# Crawl the movie page from atmovies (開眼電影網)
url = "https://www.atmovies.com.tw/movie/fpen12042730/"
html_content = rq.request("GET", url)
soup = BeautifulSoup(html_content.text, "html.parser")

# Extract the movieID in the IMDB for the same movie.
selector = "#filmCastDataBlock > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)"
element = soup.select_one(selector)
imdbId = ""
if element:
    href = element.get("href")
    print(f"Found link: {href}")
    imdbId = href.split("/")[4]
else:
    print("Element not found.")

# Get JSON data of the movie by issuing an OMDB API request.
urlOmdb = f"http://www.omdbapi.com/?i={imdbId}"
print(f"Crawl OMDB > {urlOmdb}")
urlOmdb += f"&apikey={apiKey}"
movie = rq.request("GET", urlOmdb)
json = movie.json()
if json["Response"] == "True":
    print(f"Retrieved :\n{json}")
else:
    print(f"Failed to get the [{imdbId}] movie information.")
