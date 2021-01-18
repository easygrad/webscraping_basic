import time # 동작 시간
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") # 같은 경로에 있으면 경로 필요 없음

# 1. 네이버 이동
browser.get("http://naver.com")
# [5740:2416:0115/054821.784:ERROR:device_event_log_impl.cc(211)] [05:48:21.787] USB: usb_device_handle_win.cc:1020 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
# 장치관리자(Ctrl + X) -> 범용직렬버스컨트롤러 -> USB 중간꺼(Composite어쩌구) 사용안함으로 변경

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id를 새로 입력
browser.find_element_by_id("id").send_keys("my_id")
# 이전 id 뒤에 덧붙여짐
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료