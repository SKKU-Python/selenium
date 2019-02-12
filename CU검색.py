# 키보드 제어, 마우스 제어, 편의점 주소 크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('chromedriver')
url = 'https://map.naver.com'
driver.get(url)

search = driver.find_element_by_css_selector('input#search-input')

# '씨유' 입력 후 ENTER키 작동
search.send_keys('씨유')
search.send_keys(Keys.ENTER)

time.sleep(0.5)

# 1페이지 ~ 5페이지 크롤링
for j in range(0,5):
    time.sleep(2)
    page = driver.find_elements_by_css_selector('div.paginate a')
    targets = driver.find_elements_by_class_name('lsnx_det')
    
    for target in targets:
        names = target.find_element_by_css_selector('dt a').text
        address = target.find_element_by_css_selector('dd.addr').text
        print(names, address)
    
    print('\n')
    page[j].click()

# 6페이지 이후 크롤링
count = 0
while count < 2:
    for j in range(1,6):
        time.sleep(2)
        page = driver.find_elements_by_css_selector('div.paginate a')
        targets = driver.find_elements_by_class_name('lsnx_det')
        
        for target in targets:
            names = target.find_element_by_css_selector('dt a').text
            address = target.find_element_by_css_selector('dd.addr').text
            print(names, address)
        print('\n')
            
        page[j].click()
    count += 1
