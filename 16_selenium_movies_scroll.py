from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)") # 1080: 모니터 해상도 높이 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,2080)") # 2080: 위에 보다 좀 더 내리기

# 화면 가장 아래로 스크롤 내리기(최하단으로 스크롤 이동은 document.body.scrollHeight)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한 번씩(아래 while문에서 사용) 

# 현재 문서 높이 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # 높이가 같으면 탈출
    if curr_height == prev_height:
        break
    
    # 높이가 다르면 다시 높이 설정해주고 또 반복
    prev_height = curr_height

print("스크롤 완료")

# 이제 이전에 했던 것처럼 정보 가져오기
import requests
from bs4 import BeautifulSoup

# 셀레늄에서 가져왔기 떄문에 필요 없음
# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
#     "Accept-Language":"ko-KR,ko" # 한글페이지 있으면 보내달라는 의미
#     }
# res = requests.get(url, headers = headers)
# res.raise_for_status()

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs = {"class":"ImZGtf mpg5gc"}) # 스크롤 해도 이전처럼 똑같이 10개만 가져옴
# movies = soup.find_all("div", attrs = {"class":["ImZGtf mpg5gc","Vpfmgd"]}) # 스크롤 이후는 다른 클래스 이름, 리스트로 묶어줌, 해당하는 모든 클래스 다 가져옴. 근데 이렇게 하면 중복해서 두번 가져옴
movies = soup.find_all("div", attrs = {"class":"Vpfmgd"}) # 이거 하나로만 하면 중복 없이 가져옴
print(len(movies)) 

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify()) 
    
for movie in movies:
    title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text() # 텍스트를 가져옴
    # print(title)

    # 할인 전 가격
    original_price = movie.find("span", attrs = {"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "  <할인되지 않은 영화는 제외>") # 프린트가 있으면 할인되지 않은 영화도 결과에 나와서 빼줌
        continue
    
    # 할인된 가격
    price = movie.find("span", attrs = {"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs = {"class":"JC71ub"})["href"]
    # 올바른 링크 : http://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ","https://play.google.com"+link)
    print("-"*100)

browser.quit()