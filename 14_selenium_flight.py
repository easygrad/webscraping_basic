from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] 이번달 선택 / element로 하고 [] 넣으면 에러('WebElement' object is not subscriptable), elements로 해야 함
browser.find_elements_by_link_text("28")[1].click() # [1] 다음달 선택

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click() # xpath 복사
# 클릭을 못하는 경우 발생하면 xpath 위치를 바꿔가면서 해보면 됨

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
# 너무 빨라서 로딩 시간 필요함

# import time
# time.sleep(3) 마냥 시간을 기다릴 수도 있지만
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    #성공했을 때 동작 수행
    # 괄호 빼먹으면 TypeError: __init__() takes 2 positional arguments but 3 were given 에러 뜸
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()
# browser를 최대 10초까지 대기하는데, 어떤 조건을 기준으로, XPATH 기준으로, 이것에 해당하는 위치가 나올 때까지. 10초를 기다려보고 그 전에 나오면 다음 동작, 그 이후에도 안나오면 에러
# try 로 묶어줌: 에러 뜨거나 동작 끝나면 창 닫기
