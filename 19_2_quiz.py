from selenium import webdriver


url = "https://land.naver.com"
browser = webdriver.Chrome()
browser.get(url)

# browser.find_element_by_xpath("//*[@id='queryInputHeader']").click()
browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys("마포래미안푸르지오") # 검색어에 입력


browser.find_element_by_xpath("//*[@id='queryInputHeader']").send_keys("\n")
