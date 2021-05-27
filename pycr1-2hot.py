# pip install beautifulsoup4
# pip install lxml  분석 parser

import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday.nhn'
res = requests.get(url)
res.raise_for_status()

# soup 이 모든 정보를 가지고 있음, 바로 element에 접근가능
soup = BeautifulSoup(res.text, 'lxml') 

# 홈페이지를 잘 알 때
# print(soup.title) 
# # <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>

# print(soup.title.get_text()) 
# # 네이버 만화 > 요일별  웹툰 > 전체웹툰

# # 페이지 > ctrl shift i 개발자도구 > element > a태그

# print(soup.a) # 첫번째로 발견되는 a태그를 알려줘 
# <a href="#menu" onclick="document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"><span>메인 메뉴로 바로가기</span></a>

# print(soup.a.attrs) # a태그의 속성 dict 
# # {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}

# print(soup.a['href']) # a element의 href의 속성 '값'       
# #menu


# 잘모를땐 find
# print(soup.find('a', attrs={'class':'Nbtn_upload'})) #  class가 'class':'Nbtn_upload'인 를 찾아줘
#<a class="Nbtn_upload" href="/mypage/myActivity.nhn" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>

# print(soup.find('li', attrs={'class':'rank01'})) #li 태그 중 ranks01을 찾기
# <li class="rank01">
# <a href="/webtoon/detail.nhn?titleId=758037&amp;no=19" onclick="nclk_v2(event,'rnk*p.cont','758037','1')" title="참교육-19화">참교육-19화</a>
# <span class="rankBox"><img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0</span>
# </li>

rank1 = soup.find('li', attrs={'class':'rank01'})
# print(rank1.a) # a element 만 나옴
# <a href="/webtoon/detail.nhn?titleId=758037&amp;no=19" onclick="nclk_v2(event,'rnk*p.cont','758037','1')" title="참교육-19화">참교육-19화</a>

# print(rank1.a.get_text())

''' 자식입려
# print(rank1.next_sibling)
# # 두번해주면 나온다
# print(rank1.next_sibling.next_sibling)
# # 출력없음, 줄바꿈가능성
# rank2 = rank1.next_sibling.next_sibling # 그 다음 element 정보
# print(rank2.a.get_next())
# rank3 = rank2.next_sibling.next_sibling # 그 다음 element 정보
# print(rank3.a.get_text()) # 윈드브레이커-3부 - 103화 도둑찾기
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text()) # 소녀의 세계-2부 45화
'''

''' 자식
print(rank1.parent) # ol까지 나옴
'''

''' 정밀하게 찾고 싶을 때
#가긴가는데 찾는 내용만 나옴
rank2 = rank1.find_next_sibling('li') # 소녀의 세계-2부 45화
print(rank2.a.get_text())
'''

''' 전체에서 내용으로 태그찾고 싶을 때
# soup 전체, text는 열고닫는 사이에 <>내용</>
webtoon = soup.find('a', text = '싸이코 리벤지-27화')
print(webtoon)
# <a href="/webtoon/detail.nhn?titleId=753858&amp;no=28" onclick="nclk_v2(event,'rnk*p.cont','753858','10')" title="싸이코 리벤지-27화">싸이코 리벤지-27화</a>
'''






