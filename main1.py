import requests
from bs4 import BeautifulSoup
import html5lib

url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"

# Send an HTTP request t the webpage you want to scrape and retrieve its HTML contents:
content = requests.get(url)

# Fetching the content of HTML page
htmlcontent = content.content

# Parsing or structuring raw html page
soup = BeautifulSoup(htmlcontent, 'html.parser')

# fetching the title
title = soup.title 
print(title.string)

# Fetching the content of the page
pageContent = soup.get_text()
print(pageContent)
