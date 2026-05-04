SKIP_ONE_LINE = "\n\n"

# # --- Grab by URLLib
# import urllib.request as req

# url = "https://python.org/"
# res = req.urlopen(url)
# html = res.read()  # html is in bytes type
# print(html)

# # --- Grab by Requests
# import requests as req

# url = "https://data.gov.tw/"
# res = req.get(url)
# res.encoding = "utf-8"
# # print(res.text)

# --- Parse HTML by BeautifulSoup
from bs4 import BeautifulSoup as bs

# # --- Simple parsing.
# html = """
# <html><head><title>The Dormouse's story</title></head> <body> <p class="title"><b>The Dormouse's story</b></p> <p class="story">Once upon a time there were three little sisters; and their names were <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p> <p class="story">...</p>
# """
# # html = res.text

# # Or use the Python's default parser : 'html.parser', install 'lxml' parser package for this to work.
# soup = bs(html, "lxml")
# print(soup.prettify(), end=SKIP_ONE_LINE)
# idName = "link2"
# print(f"{idName}.text = [{soup.find(id=idName).text}]", end=SKIP_ONE_LINE)
# print(f"--->>>  Title of the page is: [{soup.title.text}]  <<<---", end=SKIP_ONE_LINE)

# sisters = []
# for link in soup.find_all("a"):
#     sisters.append(link.text)
# print(f"The {len(sisters)} sisters are: {", ".join(sisters)}", end=SKIP_ONE_LINE)

# --- Advance parsing.
html = """
<html><head><title>國立臺灣大學系統</title></head>
<body>
<p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
<p class="ntu_system">
<a href="http://www.ntu.edu.tw" class="union" id="link1">臺灣大學</a>
<a href="http://www.ntnu.edu.tw" class="union" id="link2">臺灣師範大學</a>
<a href="http://www.ntust.edu.tw" class="union" id="link3">臺灣科技大學</a>
</p></body></html>
"""

soup = bs(html, "lxml")
print(f"1. {soup.title}")
print(f"2. {soup.find('a')}")
print(f"3. {soup.find('b')}")
print(f"4. {soup.find_all('a',{'class':'union'})}")
print(f"5. {soup.find_all('a',{'id':'link2'})}")
print(f"6. {soup.find_all('a',{'href':'http://www.ntust.edu.tw'})}")

web = soup.find("a", {"id": "link1"})
print(f"7. {web.get('href')}")

# Use CSS selector to find elements.
data = soup.select(".union")
print(f"8. {data[0].text}")
print(f"9. {data[1].text}")
print(f"10. {soup.select('#link3')[0]}", end=SKIP_ONE_LINE)
