from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import pandas as pd
import datetime

df = pd.DataFrame()

driver = webdriver.Chrome('chromedriver')

# 서울 region=10, 강남 cinema=1372
url = 'http://www.megabox.co.kr/?menuId=theater-detail&region=10&cinema=1372'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

items = soup.select('.lineheight_80')

area = soup.title.text
#data.append(area)

for i in range(0, len(items)):
    data = []

    if items[i].find('th', class_="title").find('div').find('a') != None:
        title = items[i].find('th', class_="title").find('div').find('a').text
    else:
        title = '..'

    # 상영관
    theater_temp = items[i].find('th', class_="room").find('div').text
    digital = items[i].small.text
    theater = theater_temp + ' ' + digital 
    
    # 상영시간, 좌석수
    showtime_temp = items[i].select('span.time')
    seats_temp = items[i].select('span.seat')

    showtime_seats = []
    for j in range(0, len(showtime_temp)):
        showtime = showtime_temp[j].text
        seats = seats_temp[j].text
        showtime_seats.append(showtime + ":" + seats)
    
    # 크롤
    crawling_time = datetime.datetime.now()
    data.append(list([title, theater, showtime_seats, crawling_time]))
    
    df_i = pd.DataFrame(data, columns=['영화명', '상영관', '좌석수', '시간'], index=[area])
    
    df = df.append(df_i)

print(df)
df.to_csv('Megabox1.csv', encoding='ms949')
