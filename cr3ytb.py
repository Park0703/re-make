# 유튜브 채널 동영상 제목 긁어오기
import csv
import requests
import re 
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

# # 유저아이디 검색@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Channel = '이수안컴퓨터연구소'
# #csv
# filename = '{}채널 영상제목 모음.csv'.format(Channel)
# f = open(filename, 'w', encoding='utf-8-sig', newline='') 
# # newline 자동 줄바꿈 제거 //  encoding='utf8 => utf-8-sig : 깨짐 방어
# writer = csv.writer(f)




# title = Channel
# writer.writerow(['Channel', title]) #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# writer.writerow(['num', 'Channel', 'time'])
# 페이지 넘기는 법

url = 'https://www.youtube.com/c/{}/videos'.format(Channel)
print(url)
# html 정보가 느린 경우
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 내 정보넣기
videos = soup.find_all('div', attrs={'class':"style-scope ytd-grid-renderer"})
print(videos)
# 전적
num = 0

for video in videos :
    print(video)
    num += 1
    match = '{}번째'.format(str(num))
    print(match)
    
#     # 승패
#     vd = wrap.find('div', attrs={'class':'GameResult'}).get_text().strip()
#     print('결과 :', vd)
#     # 챔피언
#     cham = wrap.find('div', attrs={'class':'ChampionName'}).get_text().strip()
#     print('챔피언 :', cham)
    
#     K = wrap.find('span', attrs={'class':('Kill')}).get_text()
#     D = wrap.find('span', attrs={'class':('Death')}).get_text()
#     A = wrap.find('span', attrs={'class':('Assist')}).get_text()
#     KDA = K + ' // ' + D + ' // ' + A
#     print('KDA :', KDA.split('\t'))
    
#     KDAratio = wrap.find('span', attrs={'class':re.compile('^KDARatio')}).get_text()
#     print('KDAratio :', KDAratio)
#     writer.writerow([match, Channel, time])
#     # writer.writerow(match.split('\t'))
#     # writer.writerow(vd.split('\t'))
#     # writer.writerow(cham.split('\t'))
#     # writer.writerow(KDA.split('\t'))
#     # writer.writerow(KDAratio)
#     # writer.writerow('--------------------'.split('\t'))
    
#     # ebook = ebook.get_text()
    
#     # print(ebook)
    
#     # if DB :
#     #     #제목
#     #     title = book.find('a', attrs={'class':'bo3'})
#     #     # if title :
#     #     #     print('제목 :', title.get_text())
#     #     # else :
#     #     #     continue

#     #     #저자
#     #     Author = book.find('a', attrs={'href':re.compile('^/Search/wSearchResult.aspx?')})      

#     #     if Author :
#     #         # print('-', title.get_text(), '//', Author.get_text())
#     #         # 여기에 내용
#     #         title2 = [title1.get_text().strip() for title1 in title]
#     #         writer.writerow(title2)
#     #         Author2 = [Author1 for Author1 in Author]
#     #         writer.writerow(Author2)
#     #     else :
#     #         continue
#     # else : # 넘기기
#     #     continue  
#     #     print('가능')
#     # #가격
#     # print(books[0].find('a', attrs={'class':'bo3'}).get_text())
#     print('------------------------------------------------')
#     # if num == 2 :
#     #     break