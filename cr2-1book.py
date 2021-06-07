# 알라딘 '머신러닝' 검색 - 제목저자 긁고, 5page, ebook이면 생략
import csv
import requests
import re 
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

#csv
filename = '머신러닝 책 모음1.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='') 
# newline 자동 줄바꿈 제거 //  encoding='utf8 => utf-8-sig : 깨짐 방어
writer = csv.writer(f)

title = '알라딘 머신러닝 저서모음'.split('\t')
writer.writerow(title)

# 페이지 넘기는 법
for i in range(1, 3) :
    print('페이지 :', i)  
    url = 'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&KeyWord=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&KeyLastWord=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&chkKeyISBN=&chkKeyTag=&chkKeyTOC=&chkKeySubject=&ViewRowCount=25&page={0}'.format(i)

    # html 정보가 느린 경우
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    
    # 평점
    books = soup.find_all('div', attrs={'class':re.compile('^ss_book_box')})
    page = (str(i)+'페이지').split('\t')
    writer.writerow(page)    
    for book in books :
        # # ebook 판별기
        DB = book.find('span', attrs={'style':'font-size: 14px;'})
        # ebook = ebook.get_text()
        # print(ebook)
        if DB :
            #제목
            title = book.find('a', attrs={'class':'bo3'})
            # if title :
            #     print('제목 :', title.get_text())
            # else :
            #     continue

            #저자
            Author = book.find('a', attrs={'href':re.compile('^/Search/wSearchResult.aspx?')})      

            if Author :
                # print('-', title.get_text(), '//', Author.get_text())
                # 여기에 내용
                title2 = [title1.get_text().strip() for title1 in title]
                writer.writerow(title2)
                Author2 = [Author1 for Author1 in Author]
                writer.writerow(Author2)
            else :
                continue
        else : # 넘기기
            continue  
        #     print('가능')
        # #가격
        # print(books[0].find('a', attrs={'class':'bo3'}).get_text())
    print('--------------------------')