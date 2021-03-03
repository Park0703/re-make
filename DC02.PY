#리스트 [] 순서를 지니는 객체의 집합
# 칸별로 10, 20, 30

subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30]
print(subway)

# 조세호씨가 타고 있다면
entertainer = ['유재석', '조세호', '박명수']
print(entertainer)
print(entertainer.index("조세호"))
# 다음역에서 하하가 탄다면?
entertainer.append('하하') #append는 맨뒤에 추가
print(entertainer)
#정형돈을 유재석 조세호 사이에
entertainer.insert(1, '정형돈') #넣기, (순서, 내용)
print(entertainer)
#뒤에서부터 꺼내기
print(entertainer.pop())
print(entertainer) # Rjsosenl
print(entertainer.pop())
print(entertainer)
print(entertainer.pop())
print(entertainer)

#같은 사람의 이름이 몇명이 있는지?
entertainer.append("유재석")
print(entertainer)
print(entertainer.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)
#순서뒤집기 가능
num_list.reverse()
print(num_list)
#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장 서로다른 자료형 이어붙이기
num_list.extend(mix_list)
print(num_list)


#사전
cabinet = {3:"유재석", 100:"김태호"} #key는 3, value값은 유재석
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5]) #할당되지 않으면 keyerror
print(cabinet.get(5)) #없으면 none표시
print(cabinet.get(5, "사용가능")) #없으면 ""을 대신보내줌

#확인하기
print(3 in cabinet) #True
print(5 in cabinet) #False

#string도 가능
cabinet = {"a-3" : '정형돈'}
print(cabinet['a-3'])
#새손님
print(cabinet)
cabinet["a-3"] = '김종국' #유재석이 빠지고 김종국이 들어감
cabinet["c-20"] = "조세호"
print(cabinet)
#손님체크아웃
del cabinet["a-3"]
print(cabinet)
#내용들만 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items()) 
#폐점
cabinet.clear()
print(cabinet)


#튜플  // 내용변경추가 불가, 속도가 빠르다.
menu = ("돈까스", "치즈가스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") #'tuple' object has no attribute 'add'
# 변수
name = "김종국"
age = "20"
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby)=("김종국", 20, "코딩")
print(name, age, hobby)


#집합(set) 
# 중복 안됨, 순서없음
my_set = {1,2,3,3,3}
print(my_set)

java={"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])
#교집합 and
print(java&python)
print(java.intersection(python))
#합집합 or
print(java|python)
print(java.union(python)) # 순서없음
#차집합 (java는 가능, python은 불가능)
print(java - python)
print(java.difference(python))
#추가
python.add("김태호")
print(python)
#제거
java.remove("김태호")
print(java)

#자료구조의 변경 - 서로바꾸기
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) #{'주스', '커피', '우유'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) #['주스', '커피', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) #('주스', '커피', '우유') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) #{'커피', '우유', '주스'} <class 'set'>

'''
추첨을 통해 1명 치킨, 3명 커피
추첨프로그램
조건1 20명, 아이디 1~20
조건2 무작위 추첨, 중복 불가
조건3 radom모듈 shuffle, sample
'''

from random import *
'''
list = [1,20]
print(list)
event = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
chicken = event.shuffle(1)
print(chicken)
coffee_list = event - chicken
coffee = coffee_list.shuffle(3)
print(coffee)

print('-당첨자 발표- \n 치킨당첨자 :  \n 커피당첨자 :  \n-축하합니다.-')
'''
users = range(1,21)
users = list(users) 
shuffle(users)
print(users)
winners = sample(users, 4)

print("당첨자발표")
print("치킨당첨자 : {0}".format(winners[0]))
print("치킨당첨자 : {0}".format(winners[1:3]))
print("축하합니다.")


