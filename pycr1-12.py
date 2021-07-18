# headless chrome = 매번 띄우면 메모리소모, 속도 느림 // pc가 아닌 server 에서 수행하면 브라우저 띄울 필요 없음
# 크롬이 없는 크롬 // 백그라운드 동작
     
from selenium import webdriver

# headless
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=3840x2160')

browser = webdriver.Chrome(options = options) # option
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
//*[@id="jsc_c_k5"]/div/div/span/div[2]/div/div
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
# 스크린샷 = 실제로 볼 순없지만 실제 동작상태 확인하기 위해
browser.get_screenshot_as_file('google_movie.png')    
    

# 구글 할인하고 있는 영화정보만 스크래핑
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

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

