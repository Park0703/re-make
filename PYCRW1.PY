import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

#검색했을 때 뒤에 붙은 검색어로 
baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요:')
#최종 검색 quote로 해당부분 번역해줌
url = baseUrl + urllib.parse.quote_plus(plusUrl)

#해당 내용 가져오고 html변수로 저장됨
html = urllib.request.urlopen(url).read()
# bs로 분석
soup = BeautifulSoup(html, 'html.parser')

#title은 sh_blog_title이란 것을 전부 가져옴
title = soup.find_all(class_='sh_blog_title')

#1번반복할때  title, href
for i in title :
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()        