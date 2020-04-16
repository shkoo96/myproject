from flask import Flask
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import urllib


location = '송파구'
enc_location = urllib.parse.quote(location + '+날씨')
url = 'https://search.naver.com/search.naver?query='+ enc_location

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

info = soup.select('div.info_data')[0]
temp_now = info.select_one('span.todaytemp').text.strip()
min_temp = info.select_one('span.min').text.strip()
max_temp = info.select_one('span.max').text.strip()
sensible_temp = info.select_one('span.sensible > em').text.strip()
print(location + ' 현재 기온은 ' + temp_now + '˚, 오늘 최고 기온은 ' + max_temp + ', 최저 기온은 ' + min_temp + ', 체감온도는 ' + sensible_temp + '입니다')
