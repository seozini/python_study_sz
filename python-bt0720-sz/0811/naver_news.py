### 네이버 뉴스 헤드라인 크롤링 ###

import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/015/0004878770?sid=105'
response = requests.get(url)
html = response.text
soap = BeautifulSoup(html,'html.parser')

headline = soap.select('.media_end_head_headline')
print(headline)
print(headline.text)