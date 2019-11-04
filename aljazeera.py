import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.aljazeera.com'

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

find = soup.findAll("div", {"class": "row latest-news-topic-trending"})
array1 = [find[i].findAll('p')[1].text for i in range(10)]
for i in array1:
    print(i)
    print()
