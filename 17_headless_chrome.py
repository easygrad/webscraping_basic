from selenium import webdriver

# 브라우저 안 띄우고 작업
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options = options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한 번씩(아래 while문에서 사용) 

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    
    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png") # 동작이 제대로 됐는지 확인하기 위해 캡쳐

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs = {"class":"Vpfmgd"}) # 이거 하나로만 하면 중복 없이 가져옴
print(len(movies)) 

for movie in movies:
    title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text() # 텍스트를 가져옴
    original_price = movie.find("span", attrs = {"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue
    
    price = movie.find("span", attrs = {"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    link = movie.find("a", attrs = {"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ","https://play.google.com"+link)
    print("-"*100)

browser.quit()