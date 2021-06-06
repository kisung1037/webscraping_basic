import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

excutable_path ="d:/mypy/chromedriver.exe"

# naver_id = "shxof"
# passwd = "namjang230!"

browser = webdriver.Chrome(excutable_path)
time.sleep(random.uniform(1,3)) 
# 네이버 이동
browser.get("http://naver.com") 
# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login") 
elem.click()
# id,pw 입력
input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "shxof", pw = "namjang230!")
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.execute_script(input_js)
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
# 로그인 버튼 클릭
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.find_element_by_id("log.login").click()

# time.sleep(3)
# id를 새로 입력
# browser.find_element_by_id("id").send_keys("namjang")
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("namjang")

# html 정보 출력
# print(browser.page_source)

# 브라우저 종료
# browser.quit()