from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

url = "https://land.naver.com"
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

# browser.find_element_by_xpath("//*[@id='queryInputHeader']").click()
browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys("리센츠") # 검색어에 입력
browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys("\n") # 엔터
# browser.find_element_by_xpath("//*[@id='header']/div[1]/div/div[1]/div/fieldset/a[1]").click() # 검색 클릭



interval = 2
time.sleep(interval)

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    else:
        curr_height = prev_height
print("스크롤 완료")

# def landSearch(name):

#     url = "https://land.naver.com"
#     browser = webdriver.Chrome()
#     browser.get(url)
#     browser.maximize_window()

#     # browser.find_element_by_xpath("//*[@id='queryInputHeader']").click()
#     browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys(name) # 검색어에 입력
#     browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys("\n") # 엔터
#     # browser.find_element_by_xpath("//*[@id='header']/div[1]/div/div[1]/div/fieldset/a[1]").click() # 검색 클릭
    
#     # interval = 2
#     # time.sleep(interval)

#     # prev_height = browser.execute_script("return document.body.scrollHeight")

#     # while True:
#     #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     #     time.sleep(interval)
#     #     curr_height = browser.execute_script("return document.body.scrollHeight")
#     #     if curr_height == prev_height:
#     #         break
#     #     else:
#     #         curr_height = prev_height
#     # print("스크롤 완료")

#     soup = BeautifulSoup(browser.page_source, "lxml")

#     items = soup.find_all("div", attrs = {"class":"item_inner"})
#     print("매물 개수: ", len(items))
#     print("-"*100)

#     for item in items:
#         title = item.find("div", attrs = {"class":"item_title"}).get_text()
#         price_type = item.find("span", attrs = {"class":"type"}).get_text()
#         price = item.find("span", attrs = {"class":"price"}).get_text()
#         spec = item.find("span", attrs = {"class":"spec"}).get_text()
#         print(title)
#         print(price_type, " : ", price)
#         print(spec)
#         print("-"*100)
#         # price = item.find("")

#     browser.quit()

# name1 = "리센츠"
# landSearch(name1)
