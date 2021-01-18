import requests
# res = requests.get("http://naver.com")
res1 = requests.get("http://nadocoding.tistory.com")
print ("응답코드:", res1.status_code) # 200이면 정상

if res1.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드:", res1.status_code,"]")

# if를 쓰지 않고도 확인할 수 있다.
res = requests.get("http://google.com")
res.raise_for_status()
# 이렇게 두 줄로 처리 가능!

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding = "utf-8") as f:
    f.write(res.text)