#chapter02-2
#파이썬 완전기초
#파이썬 변수

#기본선언 : n정수에 700을 넣어라
n = 700
#컴퓨터 내부적으로는 n이 있는 주소로 들어감
#
# print(n) 함수로 n의 주소를 불러보니 700이 불러짐
print(n)
print(type(n))
# int 정수형이야!
# 동시선언
x = y = z = 700
print(x, y, z)

#선언
var = 75

#재선언
var = 'change value'

#출력
print(var)
print(type(var))

# object reference
#변수값이 할당 상태일 때 
#1. 타입에 맞는 오브젝트 생성
#2. 값생성
#3. 콘솔출력

# 예1)
print(300)
print(type(300))

# 예2)
# n = 777
print(n, type(n))
print()

m = n
print(m, type(n))

#id확인
m=800
n=800

print(id(m))
print(id(n))
print(id(m) == id(n))
#같은 값이면 굳이 여러번 표시안함

#다양한 변수 선언 - 네이밍 규칙이 실력여부
# camel case : Numberofcollege graduated -> method 선언시
# Pascal case : numberofcollege -> class 선언시
# snake case : number_of_college_graduates ->파이썬에서

#선언법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
# 변수는 _와$만 허용 1age = 1(x)

# 예약어는 변수명으로 불가능  ex) for, as, class //python reserved words 참고
#
#int 정수 // float 실수 // complex 복소수
#bool 불린 양자택일 // str : 문자열()시권스 // list : 리스트(시퀀스) // tuple튜플(시권스)
#set 집합, dict 사전

#데이터 타입
str1 = 'python'
bool = True
str2 = 'anaconda' 
float_v = 10.0 #10 = 10.0
int_v = 7

list = [str1, str2]
dict = (
)

#
print(type(str1))
print(type(bool))


#[]{}()
tuple = (7, 8, 9)
set = {7, 8, 9}

# + - * / //몫 %나머지
# abs(x)절대값, pow(x, y) x** y -> 2**3

# 형변환
a = 3.
b = 6
c = .7
d = 12.7

#타입출력
print(type(a), type(b), type(c), type(d))

#타입변환
print(float(b))
print(int(c))
print(int(d))
print(int('true')) 
#true = 1, false = 0
print(complex(3))

x, y - divmod(100, 8)
print(x,y)
print(pow(5,3), 5 ** 3)
#외부 모듈
import math
print(math)
# ceil x이상의 수중에서 가장 작은 정수
