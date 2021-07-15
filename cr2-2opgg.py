# opgg 내 20개 전적 // 승패 kda
import csv
import requests
import re 
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

# # 유저아이디 검색@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Username = '지땅땅'
# #csv
filename = '{}전적 긁어오기.csv'.format(Username)
f = open(filename, 'w', encoding='utf-8-sig', newline='') 
# newline 자동 줄바꿈 제거 //  encoding='utf8 => utf-8-sig : 깨짐 방어
writer = csv.writer(f)




title = Username
writer.writerow(['Username', title]) #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
writer.writerow(['num', 'general', 'cham', 'rate', 'KDA', 'KDAratio'])
# 페이지 넘기는 법

url = 'https://www.op.gg/summoner/userName={}'.format(Username)

# html 정보가 느린 경우
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

# 내 정보넣기
rank = soup.find('div', attrs={'class':re.compile('^sub-tier__rank-tier')}).get_text().strip()
general = soup.find('span', attrs={'class':re.compile('^sub-tier__gray-text')}).get_text().replace('/', '').strip()
rate = soup.find('div', attrs={'class':re.compile('^sub-tier__gray-text')}).get_text().strip()
entire = soup.find('table', attrs={'class':('GameAverageStats')})
K = entire.find('span', attrs={'class':('Kill')}).get_text()
D = entire.find('span', attrs={'class':('Death')}).get_text()
A = entire.find('span', attrs={'class':('Assist')}).get_text()
KDA = K + ' // ' + D + ' // ' + A
KDAratio = soup.find('span', attrs={'class':re.compile('^KDARatio')}).get_text()

# print('Username', Username)
# print('general', general.get_text().replace('/', '').strip())
# print('rank', rank.get_text().strip())
# print(rate.get_text().strip())
# print('KDA', KDA)
# print('KDAratio', KDAratio.get_text())

writer.writerow(['total', general, rank, rate, KDA, KDAratio])
# writer.writerow(rank)
# writer.writerow(rate)
# writer.writerow(KDA.split('\t'))
# writer.writerow(KDAratio)
# writer.writerow('--------------------'.split('\t'))

wraps = soup.find_all('div', attrs={'class':'GameItemWrap'})
# 전적
num = 0
for wrap in wraps :
    num += 1
    match = '{}번째'.format(str(num))
    print(match)
    
    # 승패
    vd = wrap.find('div', attrs={'class':'GameResult'}).get_text().strip()
    print('결과 :', vd)
    # 챔피언
    cham = wrap.find('div', attrs={'class':'ChampionName'}).get_text().strip()
    print('챔피언 :', cham)
    
    K = wrap.find('span', attrs={'class':('Kill')}).get_text()
    D = wrap.find('span', attrs={'class':('Death')}).get_text()
    A = wrap.find('span', attrs={'class':('Assist')}).get_text()
    KDA = K + ' // ' + D + ' // ' + A
    print('KDA :', KDA.split('\t'))
    
    KDAratio = wrap.find('span', attrs={'class':re.compile('^KDARatio')}).get_text()
    print('KDAratio :', KDAratio)
    writer.writerow([match, vd, cham, KDA, KDAratio])
    # writer.writerow(match.split('\t'))
    # writer.writerow(vd.split('\t'))
    # writer.writerow(cham.split('\t'))
    # writer.writerow(KDA.split('\t'))
    # writer.writerow(KDAratio)
    # writer.writerow('--------------------'.split('\t'))
    
    # ebook = ebook.get_text()
    
    # print(ebook)
    
    # if DB :
    #     #제목
    #     title = book.find('a', attrs={'class':'bo3'})
    #     # if title :
    #     #     print('제목 :', title.get_text())
    #     # else :
    #     #     continue

    #     #저자
    #     Author = book.find('a', attrs={'href':re.compile('^/Search/wSearchResult.aspx?')})      

    #     if Author :
    #         # print('-', title.get_text(), '//', Author.get_text())
    #         # 여기에 내용
    #         title2 = [title1.get_text().strip() for title1 in title]
    #         writer.writerow(title2)
    #         Author2 = [Author1 for Author1 in Author]
    #         writer.writerow(Author2)
    #     else :
    #         continue
    # else : # 넘기기
    #     continue  
    #     print('가능')
    # #가격
    # print(books[0].find('a', attrs={'class':'bo3'}).get_text())
    print('------------------------------------------------')
    # if num == 2 :
    #     break