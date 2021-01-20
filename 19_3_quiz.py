from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-agent=userMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

url = "https://land.naver.com/complexes/104917"
browser = webdriver.Chrome(options = options)
browser.get(url)

# title = browser.find_elements_by_class_name("title")
# print(title)

