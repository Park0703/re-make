#기본출력
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3) #더하기
print(5*3) #곱하기
print(3*(3+1)) #우선순위연산으로

#문자열 기본형
print('풍선')
print("나비")
print("ㅋ"*9) #문자열과 정수를 섞어서 계산출력도 가능

#boolean 자료형 
print(5 > 10) #false
print(5 < 10) #True
print(True) #True
print(False) #flase
print(not True) #False
print(not False) #True
print(not (5 > 10)) #True

#변수
#애완동물을 소개해주세요

print('우리집 강아지의 이름은 연탄이예요.')
print('연탄이는 4살이며, 산책을 아주 좋아해요.')
print('연탄이는 어른일까요? true')

#이름이 연탄이에서 푸름이로 바뀌면?

animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '이예요.')
print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 아주 좋아해요.')
print(name + '는 어른일까요? '+ str(is_adult))

'''
이렇게하면 
여러문장이 
주석처리됩니다.
'''
#여러문장 #처리하려면 드래그+ctrl+/ 해제도 동일
'''
Quiz) 변수를 이용하여 다음문장을 출력하시오

변수명
: station

변수값
: "사당", "신도림", "인천공항" 순서대로 입력

출력문장
: xx행 열차가 들어오고 있습니다.
'''
station1 = "사당"
print(station1 + '행 열차가 들어오고 있습니다.')
print(''+ '행 열차가 들어오고 있습니다.')

#연산자
print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3 = 8
print(5%3) #나머지 구하기 2
print(10%3) #나머지 구하기 1
print(5//3) #1
print(10//3) #3

print(4>=7) #False
print(10>3) #True
print(10<3) #False
print(5<=5) #True

print(3==3) #true
print(4==2) #False
print(3+4==7)#True

print(1!=3) #앞뒤가 같지 않다. true
print((not 1!=3)) #False

print((3>0)and(3<5)) # True
print((3>0)&(3<5)) #True

print((3>0)or(3>0)) #true
print((3>0)|(3>0)) #true #\|

print(5>4>3) #true
print(5>4>7) #False

#간단한 수식
print(2+3*4) #14
print((2+3)*20) #20
number = 2+3*4 #14
print(number)

number = number +2 #16
print(number)

number += 2 #18 
print(number)

number /= 2 #18
print(number)

number -= 2 #16
print(number)

number %= 5 #1
print(number)

#기타 기호
print(abs(-5)) # 절대값
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) #내림. 4
print(ceil(3.14)) #올림. 4
print(sqrt(16)) #제곱근. 4

#랜덤함수 난수
from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값을 생성
print(random()*10) #0.0 ~ 10.0 미만의 임의의 값 생성 
print(int(random()*10)) #0 ~ 10미만의 임의의 값 생성
print(int(random()*10)+1) #1 ~ 10이하의 임의의 값 생성
print(int(random()*45)+1) #1 ~ 45이하의 임의의 값 생성

print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성
print(randint(1,45)) #1 ~ 45 이하의 임의의 값 생성

'''
월 총4회 3회 온라인, 1회 오프라인
조건1 랜덤 날짜지정
조건2 월별 날짜 다름감안 최소 일수 28일 이내
조건3 매월 1~3일은 스터디준비로 제외
'''
date=randint(4,28)
print('오프라인 스터디 모임 날짜는 매월' + str(date) + '일로 선정되었습니다.')

#문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence1 = '파이썬은 쉬워요.'
print(sentence1)

#슬라이싱
jumpin = '950703-1665532'
print("성별 : "+ jumpin[7])
print("월 : "+ jumpin[0:2]) #0~2
print("월 : "+ jumpin[2:4])
print("일 : "+ jumpin[4:6])

print("생년월일 : "+ jumpin[:6]) #처음부터 6 직전까지
print("뒤 7자리 : "+ jumpin[7:]) #7부터 끝까지
print("뒤 7자리(뒤에서부터) : " + jumpin[-7:])
#맨뒤에서 7번째부터 끝까지

#문자열 처리함수
python = "Python is Amazing"
print(python.lower()) #lower 소문자
print(python.upper())
print(python[0].isupper()) #있는지 없는지
print(len(python)) #개수 새기
print(python.replace("Python", "java")) #문자변환

index = python.index("n")
print(index)      #5        #"n"위치 0부터 찾기
index = python.index("n", index + 2)
print(index)

print('hi')
print(python.find("java")) #원하는 값없으면 -1
#print(python.index("java")) #값이 없으니 아예 오류를 내버림
print(python.count("n")) #n이 몇개 있는지

#문자열 포멧
print("a"+"b")
print("a", "b")

#방법1 %
print("나는 %d살입니다." % 20) # 정수 따오기
print("나는 %s를 좋아해요." %"파이썬") # 글자 따오기
print("apple이라는 %c로 시작해요" % "A") # %c 첫글자만 따오기

# %s
print("나는 %s살입니다." % 20) #숫자도 가능
print("나는 %s 색과 %s 색을 좋아해요." % ("파란", "빨간")) # 두개이상 딸 때

#방법2 {}
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다." .format("파란","빨간")) #{}차례로 인색
print("나는 {0}색과 {1}색을 조하해요." .format("파란", "빨간")) #0부터 인식

#방법3 format따로정의
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20,color="빨간"))

#방법4 정의하고 넣기, f 조심
age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자 - 예외를 가능하게 하기
#\n : 줄바꾸기
print("백문이불여일견 \n백견이 불여일타") #\n
#\ : print("나도 '나도코딩'입니다.")
print("나도 \"나도코딩\"입니다.") #\으로 뒷글자 예외 허용하기
print('나도 \'나도코딩\'입니다.')
print("PS C:\\Users\\bsang\\OneDrive\\바탕 화면\\re-make>")# \\ 뒷 역슬러시가 그대로 출력
#\r : 커서를 맨앞으로 보냄
print('red apple\rpine')
#\b : 백스페이스 한글자지우기
print('redd\b apple')
#\t : 탭

'''
사이트별 비밀번호 만들기
1. http:// 앞부분 제외
2. .com 뒷부분 제외
3. 첫3자리 // 글자갯수 // 글자내e // !
'''
#1 정의
address = 'http://naver.com'
print(address[7:12])
print(address[7:12][:3], len(address[7:12]))
print(address[7:12][:3], len(address[7:12]), 
    address[7:12].count("e"))
print(address[7:12][:3], len(address[7:12]), 
    address[7:12].count("e"), "!")

#풀이
url = "http://naver.com"
my_str = url.replace('http://', "") #규칙1
my_str = my_str[:my_str.find(".")] #규칙2
print(my_str)
passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e"), "!")
print(passward)
