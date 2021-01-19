import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element 의 속성 정보를 출력
# print(soup.a["href"]) # a element 의 herf 속성 '값' 정보를 출력
# 이렇게 하는건 페이지에 대한 이해도가 높을 때만!

print(soup.find("a", attrs = {"class": "Nbtn_upload"})) # class = ""인 a element를 찾아줘
print(soup.find(attrs = {"class": "Nbtn_upload"})) # class = ""인 어떤 element를 찾아줘 페이지에 웹툰 올리기가 하나이기 때문에 가능

print(soup.find("li", attrs = {"class": "rank01"}))
rank1 = soup.find("li", attrs = {"class": "rank01"})
print(rank1.a.get_text())
print(rank1.next_sibling)
print(rank1.next_sibling.next_sibling) # next_sibling 두 번 해주는 이유? 먼가 사이에 끼어있어서 두 번 해주는 경우 있음
rank2 = rank1.next_sibling.next_sibling
print(rank2.a.get_text())
rank1 = rank2.previous_sibling.previous_sibling # next가 있으니깐 previous도 있음. next와 previous는 형제들끼리 왔다갔다 하는 것

print(rank1.parent) # 부모로 가볼 수도 있음

rank2 = rank1.find_next_sibling("li") # 개행?이 있는지 없는지 모르니깐 li에 해당하는 것만 찾으면 위에서 한 불편함 해소 가능
print(rank2.a.get_text())

print(rank1.find_next_siblings("li")) # 한 번에 가져올 수 있는 방법

webtoon = soup.find("a", text = "싸움독학-61화 : 야 하면되잖아") # 텍스트로 가져올 수도 있음
print(webtoon)
