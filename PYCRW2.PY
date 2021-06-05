# 기술노트
# 뉴스, 날씨 ,증권 등 계속 변화하는 내용에 크로울러가 유용

from urllib.request import urlopen
from bs4 import BeautifulSoup

#url 함수 호출 reponse 로 테그 데이터가 클라이언트로 오는 것
html = urlopen('https://news.naver.com/')

bsObject - BeautifulSoup(html, 'html.parser')

for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))