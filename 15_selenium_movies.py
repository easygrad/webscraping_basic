import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language":"ko-KR,ko" # 한글페이지 있으면 보내달라는 의미
    }
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs = {"class":"ImZGtf mpg5gc"})
print(len(movies)) # 0이라고 뜸.. 왜?

with open("movie.html", "w", encoding="utf8") as f:
    # f.write(res.text) # 너무 많아서 보기 힘듦
    f.write(soup.prettify()) # html 문서를 예쁘게 실행

# 일단 html 문서 열어보면 영어로 되어 있음
# 구글에서는 접속자에 따라 정보가 다르게 떠서 그런거 같음
# 그럼 일단 한글 페이지에서 정보를 잘 받아올 수 있도록 바꿔야 함
# 이 때 사용할 수 있는게 유저에이전트
# 유저에이전트는 이전 그대로,, 근데 한 가지 더 있는데, 언어설정
# 여기까지 하면 한글페이지 잘 가져와짐

for movie in movies:
    # title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get("title") # title ="" 값을 가져옴
    # title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"})["title"] # title ="" 값을 가져옴
    title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text() # 텍스트를 가져옴
    print(title)

# 그런데 문제가 또 생김. 분명 영화 개수 엄청 많은데 우리가 저장한 html에는 10개 밖에 없음
# 스크롤을 내리면 그때 그때 영화가 추가됨. 이게 동적 페이지


