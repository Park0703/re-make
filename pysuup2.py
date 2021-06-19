# # int(문자열을 정수현으로 변환)
# #int('20', 16) 16진수로 20을 표현
# print('{0:d}{1:5d}{2:05d}'.format(100,200,300)) 
# # 그대로, 5자리확보, 공백은 0으로 채워서
# for i in range(1,6) : # 가로
#     print(i, '단', end='')
# print()
# for i in range(1,6) : # 가로
#     for j in range(1,4) : # 세로
#         print(i,'x',j,'=',j*i,end=' ' )
#     print(' ')

# print('안녕하세요'[0])
# print('안녕하세요'[-1])
# print('안녕하세요'[:-1])
# print('안녕하세요'[:-1:2]) # 간격
# print('안녕하세요'[::-1]) # 역순

# a='hello'
# cnt = 0
# for i in range(0, len(a)) :
#     if a[i] == 'l' :
#       cnt += 1
#     print(cnt)

# print(a.count('l'))
# print(a.find('l'))
# print(a.find('l', 3)) # 왼쪽부터 3인덱스 이후 찾기
# print(a.index('l'))

# instr = '123'
# if instr.isdigit() :
#   print(instr, '숫자입니다.')
# if instr.isalpha() :
#   print(instr, '문자입니다.')
# if instr.isalnum() :
#   print(instr, '문자+숫자입니다.')
# if instr.isupper() :
#   print(instr, '대문자입니다.')
# if instr.islower() :
#   print(instr, '소문자입니다.')
# if instr.isspace() :
#   print(instr, '공백입니다.')

# instr = 'scHool'
# print(instr.capitalize()) # 첫 문자만 대문자
# print(instr.upper())
# print(instr.lower())
# print(instr.swapcase()) # 대소문자 반대로

# # 변수 : 하나 변수 하나 값
# # 배열 : 하나 변수 여러 값
# # 
# # 구조체
# # 클래스 값 + 함수
# # 
# # 
# # 
# # #
# #list
# arr = ['10',20,30,40,50,60,70,80,90]
# # print(arr)
# # print(type(arr))
# # # 자료구조
# # print(arr[0])
# # print(arr[-1])
# # print(arr[len(arr)-1])
# # print(arr[::-1])

# # print(sum(int(arr[:])))
# # print(sum(int(arr[0])))
# # list 배열 []
# # tuple 상수화된 리스트( )
# # dict {key : value} 상인 객채
# # set 중복이 안되도록 요소 저장하는 객체
# # #

# a = [0,0,0,0]
# b = []
# print(a, len(a))
# print(b, len(b))

# mylist = [30,10,20]
# mylist.append(40)
# # %s 문자열 출력함
# mylist.sort()
# print('리스트 : %s' % mylist)
# print(mylist.pop())
# print(mylist)
# mylist.reverse()
# print(mylist)
# print(mylist.index(20))
# mylist.insert(2,222)
# print(mylist)
# mylist.remove(222)
# print(mylist)
# mylist.extend([50,60,70])
# print(mylist)
# print(mylist.count(30))
# ss='2021/06/20'
# list=ss.split('/')
# print(str(int(list[0])-10))
# print(list)
# m = '10,20,50,60,30,40,50,60,30'
# # m = m.replace(m[0], "")
# # print(m)
# # print( sum(int(m)) )

# ss=  '홍길동'
# sslist = ss.split(' ')
# hap= ''
# for n in range(0, len(sslist)+2) :
#     hap += ss[n]
#     hap += '#'
# print(hap)

# ss=  '(홍길동'
# print(ss[::-1])
# for n in range(len(ss)-1, -1, -1) :
#     print(ss[n], end='')
# ss=  '(홍길동'
# if ss.startswith('(') == False :
#   print('(', end = '')
# if ss.endswith('(') == False :
#   print(')', end = '')


# # # 1
# lett = input('한개의 문자를 입력하세요')
# if lett.isdecimal() :
#     print(int(lett)+20)
# elif lett == lett.lower() :
#     print(lett.upper())
# elif lett == lett.upper() :
#     print(lett.lower())


# # # 2 
# now = []
# sta = []
# for i in range(1, (10 + 1)) :
#     now.append(i)
#     sta.append(sum(now))
# print(now)    
# print(sum(sta))    
    
# # # # 3
# jari = input('자연수를 입력하세요')
# hap = 0
# for i in range(len(jari)-1, -1, -1) : 
#     jari  = int(jari)  
#     hap += jari // 10**i
#     jari = jari % 10**i
#     print('i :', i, 'jari :', jari, 'hap :', hap) 
#     print(hap)
    
# # 4
# aa = []    
# for i in range(0, 200, 2) :
#     aa.append(i)
# bb = aa[::-1]      
# for i in range(0, 10) :
#     print('aa[%s]='%i,aa[i],end=',' )
# print()
# for i in range(0, 10) :
#     print('bb[%s]='%(len(bb)-i-1),bb[(len(bb)-i-1)],end=',' )

    
# # 5
# h = int(input('모래시계의 높이를 홀수로 입력하세요 :'))
# for i in range(1,h+1) :
#     if i == (h//2+1) :
#         print('{0:^5s}'.format('*'))
#     elif i < (h//2+1) :
#         print('{0:^5s}'.format('*'*(h-2*(i-1))))
#     else :
#         print('{0:^5s}'.format('*'*(2*(i-(h//2+1))+1)) )    
    
    
# 리슽트 여러개
#
#   
    
# dddd.insert(1, 'ddd')
# dddd.remove('ddd')    
# del dddd[]
    
# dddd.sort(reverse=True)    
# reverse()    
# print(dddd[1][dddd.index('kim')])    
    
# for     
    
# member_list = {'lee' : 100,'hong':70, 'kim' : 90}
# print(member_list)    
# print(type(member_list))    
# print(len(member_list))       
# print(member_list['kim'])   
# member_list['park'] = 70
# print(member_list['park'])  
# print(member_list)  
# print(member_list.keys())
# print(member_list.values())
# print(member_list.items()) # 튜플형태로 저장 됨

# singer = {}
# singer['이름'] = '트와이스'
# singer['구성원수'] = 9
# singer['데뷔곡'] = '우아하게'
# singer['소속사'] = 'JYP'
# print(singer.keys())

# for i in singer.values() :
#     print(i)

# for i in singer.items() :
#     print(i)
#     print('%s=>%s'%(i[0], i[1]))
# print('이름' in singer)
# foods = \
#   {'떡볶이':'오뎅', '짜장면':'단무지', '라면':'김치', '맥주':'치킨'}
# for i in foods.keys() :
#     print('%s=>%s' % (i, foods[i]))



# # f = input('음식 : ')
# # if f in foods :
# #     print('%s=>%s' % (f, foods[f]))

# # else : 
# #     print('미등록음식 입니다')
# #     ans = input('등록하시겠습니까?')
# #     if ans == 'y' : 
# #         foods[f] = f
# #         print(f)
# #     elif ans == 'n' :
# #         print('종료되었습니다')
        
# import operator
# dic, list2 = {}, []
# dic = { 'Thomas' : '토마스', 'Edward':'에드워드', 'Henry':'헨리', 'Gothen':'고든','James':'제임스'}        
# print(dic.items())        
# list2=sorted(dic.items(), key=operator.itemgetter(1))
# # key=operator.itemgetter(0) itemgetter ㅌ튜플 중 1번째 데이ㅓ 기준 정렬 // reverse 1번째 기준으로 내림차순
# # Thomas 시작
# print(list) 

# # 튜플
# tp1 = (10,20,30)
# print(tp1)
# # tp1.append(40)
# # print(tp1[0])
# # tp1[0]=100
# list1 = list(tp1)
# # tp1.append(40)
# aaa = {30,10,20,10}
# print(aaa) # 순서지정못함,
# bbb = {30,10,20,10, 40}
# print('교집합 :',aaa & bbb)
# print('교집합 :',aaa.intersection(bbb) )
# print('합집합 :',aaa | bbb)
# print('합집합 :',aaa.union(bbb) )

# # coomprehension // 패턴있는 list, dict, set 간편하게 작성
# numbers = []
# for n in range(2,11,2) :
#     numbers.append(n)
# print(numbers)
# print([ x for x in range(1,11) if x%3==0 or x%2==0])

# cl = ['black','white']
# sl = ['s','m','l']
# dl = ((c,s) for c in cl for s in sl)
# print(dl)
# # <generator object <genexpr> at 0x000001FC96786DD0>
# # iterable한 객체 // 객체를 여러개 모아서 가지고 있는것, 
# for d in dl :
#     print(d)

# dl = [(c,s) for c in cl for s in sl]
# print(dl)

# set12 = {x**2 for x in [1,1,2,2,3,3]}
# print(set12)
# set12 = [x**2 for x in [1,1,2,2,3,3]]
# print(set12)

# set2 = { x**2 for x in range(1,11) if x%2==0}
# print(set2)
# print(sorted(set2))
# # dict
# prod = {'냉장고':220, '건조기':140, 'TV':130, '세탁기':150, '오디오':50, '컴퓨터':250}
# print(prod)
# prod1 = {}
# for name in prod.keys() :
#     if prod.get(name) < 200 :
#         prod1[name] = prod.get(name)
# print(prod1)
# prod2 = {}
# for p,v in prod.items() :
#     if v < 200 :
#         prod2.update({p:v})
# print(prod2)

# prod3 = {p:v for p, v in prod.items() if v < 200}
# print(prod3)

# #map
# before = ['2021', '02','08']
# print(before)
# after = list(map(int, before))
# print(after)


# {나라 : 수도}
# 1 나라와 수도를 등록하고 
# 화면에 나라이름을 입력받아 
# 해당 나라의 수도를 출력하기
# 등록된 나라가 아닌 경우 수도를 입력받아 등록하기.
#1
# country = input('수도를 알고 싶은 나라는? : ')
# ctrs = {'한국':'서울'}
# if country in ctrs :
#     print('%s=>%s' % (country, ctrs[country]))
# else : 
#     print('등록된 나라가 아닙니다')
#     ans = input('수도를 등록하시겠습니까?(y/n)')
#     if ans == 'y' : 
#         cap = input('수도를 입력해주세요')
#         ctrs[country] = cap
#         print('%s=>%s' % (country, ctrs[country]))
#         print('등록이 완료되었습니다')
#     elif ans == 'n' :
#         print(ctrs)
#         print('종료되었습니다') 
 
# 2
# from random import *
# r = randrange(1000, 10000)
# print(str(randrange(1000, 10000)))
# ans = [ 8, 1, 2, 6 ]
# answer = ''
# for n in range(0, len(ans)) :
#     answer += str(ans[n])

# cnt = 0
# while True :
#     cnt += 1
#     num = input('서로다른 4자리 숫자를 입력 :')
#     check = 0
#     for i in range(0,4):
#         if answer[i] == num[i] :
#             check += 1
            
#     if num == answer :
#         break
#     else :
#         print('strike : {}, Ball : 2'.format(check))
# print(cnt,'번만에 맞췄습니다.')

# 함수, 람다
# lambda 함수 객채,

# def coffee_machine(button) :
#     print()
#     print('# 1 뜨물 준비')
#     print('# 2 종이컵준비')
#     if button == 1 :
#         print('# 3 보통커피')
#     elif button == 2 :
#         print('# 3 설탕커피')
#     elif button == 2 :
#         print('# 3 블랙커피')
#     else :
#         print('#3 커피종류없음')
#     print('# 4 물을 붓는다')
        
# coffee=int(input('커피종류 선택 : 1 보통, 2설탕, 3보통'))
# coffee_machine(coffee)

# def func1 () :
#     a=20
#     b=1000 # 지역 변수
#     gval=200
#     print('func1() 함수호출함 :', 'f1 gval:',gval, 'f1 a:',a,'f1 b:',b)
    
# gval = 100 #전역변수
# a=10

# if __name__ == '__main__' : #프로그램 실행시 시작위치
#     func1()
#     print('main() 함수에서 호출함', 'gval',gval, 'a',a)
    
# def func2() :    
#     print('func2에서 func1 호출')
#     func1()
#     print('전역변수 gval',gval)

# if __name__ == '__main__' : #프로그램 실행시 시작위치
#     func2()
# # func1 변수를 원한다면 func1을 호출하는 func2코드를 써야함  지역변수를 불러내서 해야함

# def add(v1, v2) :
#     return v1+v2
# hap, sub =0,0
# hap = add(10,20)

# print('10+20',hap)
# # 리턴값 여러개면 리스트로 전달
# def multi (v1, v2) :
#     list1 = []
#     res1 = v1+v2
#     res2 = v1-v2
#     list1.append(res1)
#     list1.append(res2)
#     return list1
# hap, sub =0,0
# list1 = multi(100,200)
# hap = list1[0]
# sub = list1[1]
# print('multi 함수리턴 :',hap,sub)

# # 가변 매개변수
# def multiParam (* p) :
#     result = 0
#     for i in p :
#         result += 1
#     return result

# hap, sub =0,0
# list2 = multi(100,200)
# hap = list2[0]
# sub = list2[1]
# print('multi 함수리턴 :',hap,sub)
# print('multiparam', multiParam())
# print('multiparam', multiParam(10))
# print('multiparam', multiParam(10,20))
# print('multiparam', multiParam(10,20,30))

# # yield 함수 종료없이 중간중간 값을 리턴
# def genFun(num) :
#     for i in range(10, num+10) :
#         yield i # i 변수의 값을 전달. 리턴하지 않음 // return 은 출력
#         print(i, '값 반환')
# print('호출',list(genFun(5))) # 이방식으로 리스트 저장 가능 vs comprehension이 훨 낫지
# for data in genFun(5) :
#     print('main출력 :',data)

# 문제
# calc 두개 수와 하나의 연산자를 매개변수로 받아 결과를 전달하도록 작성
# oper = input('연산자를 선택(+,-,*,/) =>')
# var1 = int(input('첫번째 수 =>'))
# var2 = int(input('두번째 수 =>'))
# def calc(x, y, z) :
#     result = 0
#     if z == '+' :
#         result = x+y
#     elif z == '-' :
#         result = x-y
#     elif z == '*' :
#         result = x*y
#     elif z == '+' :
#         result = x/y
#     return result
# res = calc(var1, var2, oper)
# print(var1, var2, oper, res)
# %.2f 실수출력 서식문자
# .2 소숫점 이하 2자리까지 출력
# def getMean(numlist) :
#     if len(numlist) :
#         return sum(numlist) / len(numlist)
#     else :
#         return 0
# def getMean1(numlist) :
#     return sum(numlist) / len(numlist) if len(numlist) > 0 else 0
    
    
# def getSum(numlist) :
#     return sum(numlist)
    
# list3 = [2,3,3,4,4,5,5,6,6,8,8]
# print(getMean(list3))
# print(getSum(list3))

# list3 = []
# print(getMean(list3))
# print(getSum(list3))

    
# tp2 = (2,3,3,4,4,5,5,6,6,8,8)
# print(getMean(tp2))
# print(getSum(tp2))

# # 람다식
# hap1 =lambda num1=0, num2=1 : num1+num2
# print(hap1(10,20))
# 기본값 설정되어서 지정없으면 기본값 적용
# print(hap1())
# com1 =lambda num1, num2 : num1*num2
# print(com1(10,20))


# # 리스트 처리
# mylist = [1,2,3,4,5]
# def add10(num) :
#     return num+10
# for i in range(len(mylist)) :
#     mylist[i] = add10(mylist[i])
# print(mylist)

# add2 = lambda num :num+9
# for i in range(len(mylist)) :
#     mylist[i] = add2(mylist[i])
# print(mylist)

# for i in range(len(mylist)) :
#     mylist[i] = (lambda num : num +10)(mylist[i])
# print(mylist)

# # map  함수 리스트 내부요소를 함수와 연결하여 수정
# mylist = [1,2,3,4,5]
# add2 = lambda num : num +10
# mylist = list(map(add2, mylist))
# print(mylist)

# mylist = list(map(lambda num : num -10, mylist))
# print(mylist)

# list1 = [1,2,3,4]
# list2 = [10,20,30,40]

# hap = list(map(lambda num1, num2 : num1+ num2, list1, list2 ))
# print(hap)

# hap = list(map((lambda num1, num2 : num1+ num2), list1, list2 ))
# hap = list(map((lambda hap1, num1, num2 : hap1 + num1 + num2), hap, list1, list2 ))
# print(hap)
# 예외처리 : 실행하지 못하는 환경이면 // 예외가 발생한 경우 try except
# idx='파이썬'.index('일') # 예외 발생, 비정상 종료
# print('파이썬')

# mystr = '파이썬 공부 중 파이썬을 열심히 공부합시다'
# strpos=[] # 파이썬의 위치값을 저장
# index = 0
# while True :
#     index = mystr.find('파이썬', index) #0
#     strpos.append(index)
#     if index == -1 : 
#         break
#     index += 1
# print('위치 :', strpos, ', 문자개수 :', len(strpos))


# mystr = '파이썬 공부 중 파이썬을 열심히 공부합시다'
# strpos=[] # 파이썬의 위치값을 저장
# index = 0
# while True :
#     index = mystr.find('파이썬', index) #0
#     strpos.append(index)
#     if index == -1 : 
#         break
#     index += 1
# print('위치 :', strpos, ', 문자개수 :', len(strpos))

#try except



# mystr = '파이썬 공부 중 파이썬을 열심히 공부합시다'
# strpos=[] # 파이썬의 위치값을 저장
# index = 0
# while True :
#     try :
#         index = mystr.find('파이썬', index) #0
#         strpos.append(index)
#         index += 1
#     except :
#         break
# print('위치 :', strpos, ', 문자개수 :', len(strpos))


# try :
#     int('123')
# except :
#     print('숫자만 입력')

# 안녕하세요 경찰청 정보화장비기획담당관이세요?
# 수고많으십니다.
# 다름이 아니라 통계청 정책 연구목적으로 
# 서울특별시 여성안심 홈세트 지원 정책 실효성 분석을 위해
# 자치구 및 행정동 별 범죄 건수
# 특히 여성 범죄 관련
# 개인정보제외하고 범죄건수가


# 담당부서 여성범죄 수사과 데이터 
# 임다희 행정관
# 02-3150-2888


# 수사기획과 
# 수사운영지원담당 행정관
# 윤석열 범죄담당 통계
# 02-3150-1632
# 경찰청 홈페이지 2019년 20년은? 
# 데이터 확정 아직 공개 불가

# 자치구별 관리는 
# 최소단위가 경찰서
# 요청 정보공개청
# 공공데이터포털 // 5대 범죄 // 
# 정보공개청구사이트 부서배정 8월
# 보통 언제쯤 받을수 있을지?
# 2주 안 

# # 1
# x1 = int(input('피보나치 수열의 요소 갯수 입력 :'))
# fibbo = 0
# def fibo (x) :
#     fibbo += 1
#     if x == 0 :
#         return 0
#     if x == 1 : 
#         return 1    
#     return fibo(x-1) + fibo(x-2)

# print('fibo :',fibo(x1))
# print(fibbo)

# 2
# na = int(input('숫자입력 :'))
# def route(x) :
#     temp = 1
#     if x%2 == 0 : # 짝수
#         while True:
#             if x > 1 :                
#                 temp *= x
#                 x -= 1                
#                 print(temp, x)
#             elif x == 1 :
#                 print(temp)
#                 break
#         return temp
#     elif x%2 == 1 : # 홀수
#         print(x*(x+1)/2)
# route(na)
    
# 3    
# num1 = int(input('자연수 입력'))
# nap = (lambda num : num%2) 
# if nap(num1) == 0 : 
#     print('짝수')
# elif nap(num1) == 1 : 
#     print('홀수') 
    
# # # 람다식
# hap1 =lambda num1=0, num2=1 : num1+num2
# print(hap1(10,20))
# # 기본값 설정되어서 지정없으면 기본값 적용
# print(hap1())
# com1 =lambda num1, num2 : num1*num2
# print(com1(10,20))

# mylist = [1,2,3,4,5]
# def add10(num) :
#     return num+10
# for i in range(len(mylist)) :
#     mylist[i] = add10(mylist[i])
# print(mylist)

# add2 = lambda num :num+9
# for i in range(len(mylist)) :
#     mylist[i] = add2(mylist[i])
# print(mylist)

# for i in range(len(mylist)) :
#     mylist[i] = (lambda num : num +10)(mylist[i])
# print(mylist)

# # map  함수 리스트 내부요소를 함수와 연결하여 수정
# mylist = [1,2,3,4,5]
# add2 = lambda num : num +10
# mylist = list(map(add2, mylist))
# print(mylist)

# mylist = list(map(lambda num : num -10, mylist))
# print(mylist)

# list1 = [1,2,3,4]
# list2 = [10,20,30,40]

# hap = list(map(lambda num1, num2 : num1+ num2, list1, list2 ))
# print(hap)

# hap = list(map((lambda num1, num2 : num1+ num2), list1, list2 ))
# hap = list(map((lambda hap1, num1, num2 : hap1 + num1 + num2), hap, list1, list2 ))
# print(hap)

# num1 = input('숫자형문자1')
# num2 = input('숫자형문자2')
# try :
#     num1 = int(num1)
#     num2 = int(num2)
#     res = num1 / num2
#     print(res)
#     while True :
#         print('z')
# except ValueError as e :
#     print('숫자만, 변환불가')
#     print(e)

# except ZeroDivisionError as e :
#     print('두번째 문자는 0 불가')
#     print(e)
    
# except KeyboardInterrupt as e :
#     print('반복방지')
#     print(e)
# except : # 맨마지막에, 그외 오류들
#     print('코딩확인하세요')
# finally : # 결과 상관없이 실행
#     print('프로그램 종료')
    
# try :
#     age = int(input('나이를 입력하세요'))
# except :
#     print('나이가 아니다')
# else : # 정상처리가 되면
#     if age < 19 :
#         print('미성년자')
#     else :
#         print('성인')
# # pass 구현문장이 없음
# try :
#     f = open('없는 파일', 'r')
# except FileNotFoundError :
#     pass # 구현할 내용이 없다  그렇다고 생략하면 error

# raise 강제 예외 발생
# try :
#     print(1)
#     raise ValueError # 예외 발생
#     print(2)
# except ValueError : # 에러처리
#     print('ValueError')





















