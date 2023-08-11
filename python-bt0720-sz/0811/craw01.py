# BeautifulSoup 외부 패키지 설치
# cmd
# pip install bs4 / pip install beautiful4
# : pip list (설치확인)

# vsc 터미널(ctrl + shift + ')
# : pip install beautifulsoap4

# find() 매서드 사용 - 웹 페이지 분석 및 추출
import requests
from bs4 import BeautifulSoup

url = 'https://www.giantsclub.com/html/?pcode=855'
response = requests.get(url)
html = response.text
soap = BeautifulSoup(html, 'html.parser')

# find() : 조건에 맞는 첫 번째 태그만 반환
# id로 요소를 찾을 때는 id 파라미터 사용
id_element = soap.find(id='skipArea')
print(id_element)
print(id_element.text)