#for 반복문
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0, 1, 2, 3, 4] :
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6) :
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠그루트"]
for customer in starbucks : 
    print("{0}, 커피가 준비되었습니다".format(customer))

#while 반복문
#5번을 부르지 않으면 버린다.
customer = "토르"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0 :
        print("커피는 폐기처분되었습니다.")

''' 무한루프 문
customer = "아이언맨"
index = 1
while True :
    print("{0}, 커피가 준비되었습니다. 호출{1}번 했습니다.".format(customer, index))
    index += 1
'''
customer = "헐크"
person = "unknown"

while person != customer : 
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

#countinue와 break
absent = [2, 5] #결석
no_book = [7] #책이 없다.
for student in range(1, 11) : # 1~10
    if student in absent :
        continue             #continue 제외하고 바로 지속
    elif student in no_book :
        print("오늘 수업여기까지, {0}은 교무실로 와라.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
#break 걸리면 바로 반복문 탈출

#출석번호가 1234, 앞에 100을 붙이기로 -> 101, 102, 103
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

#학생이름을 길이로 변환
students = ["아이언맨", "토르"]
students = [len(i) for i in students]
print(students)
#대문자
students = ["i-ron man", "thor"]
students = [i. upper() for i in students]
print(students)
'''
50명 매칭, 총 탑승승객수
조건1 승객별 운행소요시간 5~50분사이 난수
조건2 나는 5~15분 사이 승객만 매칭

'''

index = 1
while index <= 50 : 
    print("{0}번째 손님 (소요시간 : {1}분)".format(index, students))
    index += 1
    if index > 50 :
        break




