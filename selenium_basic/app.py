from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
# 웹 브라우저 주소창을 컨트롤하기 위한 드라이버
driver.get("https://www.naver.com")
time.sleep(3)

#  요소를 찾아서 Copy.
css_selector = "#newsstand > div.ContentHeaderView-module__content_header___nSgPg"

# 찾아온 요소를 find_element로 가져오기 -> 변수 담기
group_nav = driver.find_element(By.CSS_SELECTOR, css_selector)

#  데이터 가져오기
print(group_nav.text)

# 요소 클릭하기[액션]
group_nav.click()
input()

