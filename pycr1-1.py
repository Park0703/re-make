#나도 코딩 - 
# 스크래핑 = 웹페이지에서,, 크롤링 페이지 내 링크 안에서 내용들
# type = 'text' 과 value = '아이디를 입력하세요' 는 attribute라고 하며 element의 세부 속성임
# type = text, password, button // href
# xpath = elem  
# ent 지칭 간편한 경로, full path
# 상위, 하위는 부모자식 관계

# 개발자도구 f12에서 href가 표시
# ctrl shift c 로 각 component element  확인

# pip install requests // library 설치

'''
import requests
#res 라는 변수에 담아서 
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com") # 403 접속권한이 없다.
res.raise_for_status() # 정상이면 계속 진행
'''

'''  응답상태 확인하는 법
#1 응답코드 확인
print('응답코드 :', res.status_code) # 200이면 정상

#2 if 로 동작
# if res.status_code == requests.codes.ok : # 정상이면
#     print('정상입니다.')
# else :
#     print('문제가 생겼습니다.[에러코드 ', res.status_code, ']')

# #3 올바른 문서면 진행이고, 아니면 forbidden 에러가 남
# res.raise_for_status() 
# print('웹스크래핑을 진행합니다.')
'''

''' res의 웹 html 상태 긁어오기
#코드 글자 세기 = 18000
print(len(res.text))
#코드 출력 -=> 엄청길다
# print(res.text)
#열기 (구글.html 파일명, 쓰기모드, utf8파일로 인코딩) f이름 저장, f로 res.text를 쓴다.
# with open('mygoogle.html', 'w', encoding='utf8') as f:
#     f.write(res.text)
'''

'''
# 정규식 library == 원하는 값 매칭
import re
# abcd, book, desk

#re의 compile
p = re.compile('ca.e') # 원하는 형태
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case(o) | caffe(x)
# ^ (^de) : 문자열의 시작 > desk, destination(o) | fade(x)
# $ (se$) : 문자열의 끝 > case, base (o) | face (x)
'''


'''
# match 함수
# m = p.match('case')
# m = p.match('caffe') #'NoneType' object has no attribute 'group'
# match : careless에서 care, 주어진 문자열의 처음부터 일치하는지 확인

# m = p.search('careless') 
# search : 주어진 문자열 중에 일치하는게 있는지 확인

# def print_match(m) :
  
#     # 1 print group
#     # print(m.group()) # case ==> 'case'가 정규식 'ca.e'와 매칭해서 출력 |!매칭이면 에러발생

#     # 2 
#     if m : 
#         print('m.group():', m.group()) # 일치하는 문자열 반환 | care
#         print('m.string:', m.string) # 입력받은 문자열 | careless
        
#         print('m.start():', m.start()) # 일치하는 문자열의 시작 index | 0
#         print('m.end():', m.end()) # 일치하는 문자열의 끝 index | 4
#         print('m.span():', m.span()) # 일치하는 문자열의 시작/끝 index | (0, 4)
#     else :
#         print('매칭이 되지 않음')
        
        
            
# print_match(m)

m = p.findall('good care cafe' ) # ['care', 'cafe']
# findall : 일치하는 모든 것을 리스트 형태로 반환
print(m)
'''

# 전체 긁어오기 실습
import requests
url = 'https://naver.com/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
res = requests.get(url, headers = headers) # 접속하는 대상이 컴퓨터인 경우 방어하는 경우도 있음
res.raise_for_status() # 정상이면 계속 진행
with open('nadocoding.html', 'w', encoding='utf8') as f:
    f.write(res.text)
# user agent string    
# WhatisUseragent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
    
    
    