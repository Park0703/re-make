import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
url1 = 'https://comic.naver.com/webtoon/list.nhn?titleId=703846'
res = requests.get(url1)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') 

#화요웹툰, 마음의 소리이면 class


# 모든 제목을 가져옴 // class 속성이 title 인 모든 a element를 반환 // 이건 url일때 // url1(x)
# cartoons = soup.find_all('a', attrs={'class' : 'title'})
# # print(cartoons)
# for cartoon in cartoons :
#     print(cartoon.get_text())

# -----------------------------------------------------------------------------------------------

# 각 화의 제목 링크 따오기
cartoons = soup.find_all('td', attrs={'class' : 'title'})  

# 만화제목 링크가져오기
title = cartoons[0].a.get_text() # 리스트에ㅔ 없다 list index out of range = url을 잘못설정
# print(title) # 제목
link = cartoons[0].a['href']
print("https://comic.naver.com" + link) #완성된 링크 

#  만화제목 링크가져오기
for cartoon in cartoons : 
    title = cartoon.a.get_text()                                             
    link = "https://comic.naver.com" + cartoon.a['href']
    print(title, link) # 제목, 링크 스크레핑
    
'''
#평점구하기 태그명 div, <div class="rating_type">
# total_rates = 0
# cartoons = soup.find_all('div', attrs={'class' : 'rating_type'})  
# for cartoon in cartoons : 
#     rate = cartoon.find('strong').get_text()
#     print(rate)
#     #평점평균 구하기
#     total_rates += float(rate)
# print("전체점수 :", total_rates)
# print("평균점수 :", total_rates / len(cartoons))
# #bs4는 한글지원 ^^./ // exit()