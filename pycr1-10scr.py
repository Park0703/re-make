'''
# 구글 할인하고 있는 영화정보만 스크래핑
import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/top'
# 크롬에서 접속한 정보를 유저에이전트로 가져감
headers = {
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
  'Accept-Language':'ko-KR,ko'
  } # 언어, ko=KR, ko

res = requests.get(url, headers = headers) # hearder 라고 해버림
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs = {'class':'ImZGtf mpg5gc'})
print(len(movies))
# div, 클래스명도 잘적었는데도 0이라고 뜸 //   왜그런지 분석
# ith open('movie.html', "w", encoding='utf8') as f:
    # f.write(res.text) # 이렇게하면 너무 내용이 많으니깐
#    f.write(soup.prettify()) # 예쁘게 출력
    # 왜그랬냐면 접속자마다(국가, 크롬, 사용자데이터) 서로다른 페이지를 return => userAgent (x) header(o)
    # useragent

# 동적페이지 => 초기 10개 로딩, 스크롤바를 맨아래로 내려야 추가적인 로딩이 되면서 10개 추가 로딩
# 그냥하면 못함 => 셀레니움으로 해결

for movie in movies:
    title = movie.find('div', attrs = {'class' : 'WsMG1c nnK0zc'}).get_text()
    print(title)
    '''
    
    
     
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
#페이지이동
url = 'https://play.google.com/store/movies/top'
browser.get(url)    
    
# 스크롤 내리기 # 동적 페이지 대응
# browser.execute_script("window.scrollTo(0, 2160)") # 해상도 1920x1080 세로 만큼
# 바탕화면 > 우클릭 > 디스플레이 설정 > 메뉴 > PC해상도 확인

# 화면 가장 아래로 스크롤 내리기 # 동적 페이지 대응
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서높이를 가져와 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

while True : 
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지로딩 대기
    time.sleep(interval)
    # 현재 문서높이를 가져와 저장
    curr_height = browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 현재높이와 이전 높이가 같다면 더이상 늘어나는 페이지가 없다. 끝났다.
    if curr_height == prev_height :
        break
    prev_height = curr_height
    
print('스크롤 완료')    
    
    

# 구글 할인하고 있는 영화정보만 스크래핑
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')
# 각 항목 리스트에 들어갈 수 있는 단위로 쪼겜
movies = soup.find_all('div', attrs = {'class':'Vpfmgd'}) # 새로 생기는 건 리스트로 관리
print(len(movies))

for movie in movies:
    title = movie.find('div', attrs = {'class' : 'WsMG1c nnK0zc'}).get_text()
    # print(title)
    original_price = movie.find('span', attrs = {'class' : 'SUZt4c djCuy'})
    if original_price :
        original_price = original_price.get_text()
    else :
        # print(title, '<할인되지 않은 가격입니다.>')
        continue
    
    # 할인된 가격
    price = movie.find('span', attrs = {'class' : 'VfPpfd ZdBevf i5DZme'}).get_text()
    
    # 링크
    link = movie.find('a', attrs = {'class' : 'JC71ub'})['href']
    # https://play.google.com/ + link
    
    print(f'제목 : {title}')
    print(f'할인 전 금액 : {original_price}')
    print(f'할인 후 금액 : {price}')
    print(f'링크 :', 'https://play.google.com' + link)
    print('-'*100)

browser.quit()

# headless chrome = 매번 띄우면 메모리소모, 속도 느림 // pc가 아닌 server 에서 수행하면 브라우저 띄울 필요 없음
# 크롬이 없는 크롬 // 백그라운드 동작