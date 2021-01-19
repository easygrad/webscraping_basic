import re
import requests
from bs4 import BeautifulSoup

url = "https://land.naver.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

today_news = soup.find_all("div", attrs = {"class":"news NE=a:tdn"})
today_news_titles = today_news[0].get_text()
print(today_news_titles)

# def landSearch(name):
    
#     return