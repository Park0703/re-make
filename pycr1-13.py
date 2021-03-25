# 페이스북 그룹 글 복사하기
     
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('C:/Users/pc/Desktop/PYTHON/PROJECT/chromedriver.exe')

#페이지이동

url = 'https://www.facebook.com/groups/TensorFlowKR' # 페이스북 그룹 '텐서플로우' 페이지
browser.get(url)    
    
# 스크롤 내리기 # 동적 페이지 대응
browser.execute_script("window.scrollTo(0, 2160)") # 해상도 1920x1080 세로 만큼
# 바탕화면 > 우클릭 > 디스플레이 설정 > 메뉴 > PC해상도 확인

# 화면 가장 아래로 스크롤 내리기 # 동적 페이지 대응
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 3 # 2초에 한번씩 스크롤 내림

# 현재 문서높이를 가져와 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

for i in range(0, 3) : 
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지로딩 대기
    time.sleep(interval)
    # 현재 문서높이를 가져와 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    # 현재높이와 이전 높이가 같다면 더이상 늘어나는 페이지가 없다. 끝났다.
    if curr_height == prev_height :    
        break
    prev_height = curr_height
        
    
print('스크롤 완료')    
    
    
# 더보기 누르기
# more = 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p'
# .click() 눌러버리기

# 피드전체 // 더보기와 관계없는  div class = feed_con
# feeds = "du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"
# span 글을 긁어올 때, 하위 div[i]로 긁어야하나, span 통으로도 긁어지나 : 실험 필요

# 이름 div class = "nc684nl6" 단 이름이 <span>이름</span> 태그로 둘러쌓임
# 본문 span class : feed_text
# feed_text = 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m'


# 구글 할인하고 있는 영화정보만 스크래핑
#  텐서플로우 그룹 feed 스크래핑
import csv
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'lxml')

feeds = soup.find_all('div', attrs = {'class':'du4w35lb k4urcfbm l9j0dhe7 sjgh65i0'}) # 새로 생기는 건 리스트로 관리
print(len(feeds))

# 이 movie in movies의 개념이 리스트 내의 반복되는 각 인덱스 명칭이다. 각객체(o), 상위div(x)




filename = '캐글코리아피드.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

title = 'num    name   feed'.split('\t')
writer.writerow(title)
# 파일 만들어서 컬럼까지 넣은 상태, 이제 행을 넣으면 됨




num = 0
for feed in feeds : # 본문내용
    num += 1
    # print(num, '============================================================')
    # more = feed.find_element_by_class("oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p")
    # more = feed.find_element_by_tag_name('더 보기')
    # if more :
    #     more = more.click()
    # else :
    #     continue
    # more = feed.find('div', attrs = {'role':'button'})
    # more.click()
    # 더보기 클릭\
    # more = feed.find_element_by_class('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p').click()
    # more.click()
    # more = feed.find('div', attrs = {'class':'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p'})
    # more.click()
    # more = more_div.find_element(By.XPATH, '//*[@id="jsc_c_210"]/div/div/span/div[2]/div/div')
    # more.click()
    
    
    # 재활용 태그의 경우 두번 거르면 고유성 확보 가능
    name_div = feed.find('h2', attrs = {'class':'gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl aahdfvyu hzawbc8m'})
    name = name_div.find('span').get_text()
    # if name :
    # print('작성자 : ', name)    
    # else :
    #     continue
    
    phara = feed.find('div', attrs = {'dir':'auto'}).get_text()
    # print(phara)
    
    # row 채우기
    writer.writerow(str(num))
    writer.writerow(name)
    writer.writerow(phara)
    
    # original_price = movie.find('span', attrs = {'class' : 'SUZt4c djCuy'})
    # if original_price :
    #     original_price = original_price.get_text()
    # else :
    #     # print(title, '<할인되지 않은 가격입니다.>')
    #     continue
    
    # # 할인된 가격
    # price = movie.find('span', attrs = {'class' : 'VfPpfd ZdBevf i5DZme'}).get_text()
    
    # # 링크
    # link = movie.find('a', attrs = {'class' : 'JC71ub'})['href']
    # # https://play.google.com/ + link
    
    # print(f'제목 : {title}')
    # print(f'할인 전 금액 : {original_price}')
    # print(f'할인 후 금액 : {price}')
    # print(f'링크 :', 'https://play.google.com' + link)
    # print('-'*100)

browser.quit()







# 해당 내용을 직접 지칭해줘야 한다.

# for movie in movies:
#     title = movie.find('div', attrs = {'class' : 'WsMG1c nnK0zc'}).get_text()
#     # print(title)
#     original_price = movie.find('span', attrs = {'class' : 'SUZt4c djCuy'})
#     if original_price :
#         original_price = original_price.get_text()
#     else :
#         # print(title, '<할인되지 않은 가격입니다.>')
#         continue
    
#     # 할인된 가격
#     price = movie.find('span', attrs = {'class' : 'VfPpfd ZdBevf i5DZme'}).get_text()
    
#     # 링크
#     link = movie.find('a', attrs = {'class' : 'JC71ub'})['href']
#     # https://play.google.com/ + link
    
#     print(f'제목 : {title}')
#     print(f'할인 전 금액 : {original_price}')
#     print(f'할인 후 금액 : {price}')
#     print(f'링크 :', 'https://play.google.com' + link)
#     print('-'*100)

# browser.quit()