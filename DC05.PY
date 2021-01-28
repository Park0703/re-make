#함수
# 5 -> x+20 -> ?
def open_account():
    print("새로운 계좌가 생성되었습니다.")
#실제로 호출하기 전까지는 실행되지 않음
#호출
open_account()

#입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money              #return 통해서 결과값 반환

#출금
def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else : 
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))

def withdraw_night(balance, money): #저녁 출금
    commission = 100 #수수료
    return commission, balance - money - commission
    
balance = 0 #잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원, 잔액 {1}원".format(commission, balance))


#기본값 설정
def profile(name, age, main_lang): #\하나의 언어
    print("이름 : {0}\t 나이 : {1}\t 주사용언어 : {2}".format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

#같은 학교, 같은 학년, 같은 반, 같은 수업이면 같이 딸려오게
def profile(name, age=17, main_lang="파이썬"): 
    print("이름 : {0}\t 나이 : {1}\t 주사용언어 : {2}".format(name, age, main_lang))
profile("유재석")
profile("김태호")

def profile(name, age, main_lang):
    print(name, age, main_lang)
#순서가 뒤섞여도 잘 지정해주면 결과가 잘나옴
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="파이썬", age=25, name="김태호")


#가변인자를 이용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0} \t 나이 : {1} \t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)
# end 써주면 밑에 있는 문장 계속 출력
profile("유재석", 20, "python", "java", "C", "C++", "C#")
profile("김태호", 25, "kotlin", "swift", "", "", "")

#도중에 함수가 변화하면? 가변인자 사용
def profile(name, age, *language):
    print("이름 : {0} \t 나이 : {1} \t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
        print()
# end 써주면 밑에 있는 문장 계속 출력
profile("유재석", 20, "python", "java", "C", "C++", "C#", "JS")
profile("김태호", 25, "kotlin", "swift")


#지역변수(특정함수에서만)와 전역변수(모든 부분에서)
gun=10
def checkpoint(soldiers): #경계근무
    global gun # 특정요소에 의해서만 변수 : 지역변수 - 코드관리가 어려워져서 권장하지 않음
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
print("전체 총 : {0}".format(gun))
#checkpoint(2) #2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

'''
남 : 키x키x22
여 : 키x키x21
조건1 표준체중은 별도 함수내 계산
    함수명 : std_weight
    전달값 : 키, 성별
조건2 표준 체중은 소수점 둘째자리까지 표시
'''
'''
def std_weight(gender, height):
    if gender == male:
        return height **2 *22
        print("키 {0}cm 남자의 표준체중은 {1}입니다.".format(height, height **2 * 22))
    else:
        return height **2 *22
        print("키 {0}cm 여자의 표준체중은 {1}입니다.".format(height, height **2 * 21))

#최종출력
weight = std_weight(male, 175)
#gender = std_weight(male, 175)
'''

#표준 입출력
print("python", "Java", "javascript", sep=" vs ", end="?")
print("무엇이 더 재미있을까요?")
import sys
print("python", "Java", "javascript", file=sys.stdout) #표준출력
print("python", "Java", "javascript", file=sys.stderr) #표준에러 확인을 해야해서 따로 표시

#출력포멧
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): #키subject, 벨류score 쌍으로 튜플로 보내줌 
    print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust(8) 왼쪽 정렬을 하는데 8칸을 확보해라

#대기순번표
#001, 002, 003,...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 3개만큼의 크기를 확보하고 값을 넣고 없으면 0을 넣어라

#
answer = input("아무값으나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " +answer+ "입니다.")

#다양한 출력포멧
#빈자리 빈공간으로 두고, 오른쪽 정렬 10공간 확보
print("{0: >10}".format(500))
#양수일땐 +표시, 음수일 땐 음수표시
print("{0: >+10}".format(+500)) #+-표시해야 양음수 표시해줌
print("{0: <+10}".format(-500))
#왼쪽 정렬 빈칸 _ 채우기
print("{0:_>+10}".format(-500))
#3자리마다 콤마찍기, 부호, 자릿수확보
print("{0:+,}".format(100000000000000000))
print("{0:^<+30,}".format(100000000000000000))
#소수점출력
print("{0:f}".format(5/3))
#특정자릿수까지 두자리 세번째에서 반올림
print("{0:.2f}".format(5/3))







