from selenium import webdriver
import requests
from bs4 import BeautifulSoup


url = "https://land.naver.com"
browser = webdriver.Chrome()
browser.get(url)

# browser.find_element_by_xpath("//*[@id='queryInputHeader']").click()
browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys("마포래미안푸르지오") # 검색어에 입력
browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys("\n") # 엔터
# browser.find_element_by_xpath("//*[@id='header']/div[1]/div/div[1]/div/fieldset/a[1]").click() # 검색 클릭

soup = BeautifulSoup(browser.page_source, "lxml")

items = soup.find_all("div", attrs = {"class":"item_inner"})
print("매물 개수: ", len(items))

for item in items:
    title = item.find("div", attrs = {"class":"item_title"}).get_text()
    price_type = item.find("span", attrs = {"class":"type"}).get_text()
    print(title)
    print(price_type)
    print("-"*100)
    # price = item.find("")

browser.quit()

# title = soup.find("div", attrs = {"class":"item_title"})
# print(title[0].get_text())



# urlSe