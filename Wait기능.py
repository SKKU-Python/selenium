# Wait 기능
# Explicit Wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('chromedriver')

url = "http://www.lottecinema.co.kr/LCHS/Contents/Cinema/Cinema-Detail.aspx?divisionCode=1&detailDivisionCode=1&cinemaID=1013"

# 롯데시네마 접속
driver.get(url)

# div.time_inner를 찾을때까지 3초 대기
items = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.time_inner')))
print(items.text)

# ==================================================================================================
# time.sleep 이용
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')

url = "http://www.lottecinema.co.kr/LCHS/Contents/Cinema/Cinema-Detail.aspx?divisionCode=1&detailDivisionCode=1&cinemaID=1013"

driver.get(url)
time.sleep(3) # 코드를 3초간 정지

itmes = driver.find_element_by_class_name('time_inner')
print(items.text)