# Naver Login Using XPath
from selenium import webdriver

url = 'https://naver.com'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

# 네이버 홈페이지에서 로그인 클릭
driver.find_element_by_xpath('//*[@id="account"]/div/a').click()

# 아이디, 비밀번호 입력
driver.find_element_by_xpath('//*[@id="id"]').send_keys('your_ID')
driver.find_element_by_xpath('//*[@id="pw"]').send_keys('your_password')

# 로그인 클릭
submit_login = driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input')
submit_login.click()