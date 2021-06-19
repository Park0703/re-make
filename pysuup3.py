'''
클래스 : 사용자정의 자료형  
         구조체 + 함수 
         멤버 변수 + 멤버함수

추상화 과정 : 클래스 생성의 과정 // 내가 필요한 정보를 뽑아내는 과정
    예) 계좌
        일반인 : 계좌번호, 은행명, 잔액, 거래내역, 대출가능...
        은행원 : 계좌번호, 지점명, 고객명
        같은 계좌번호여도 관점에 따라 필요한 정보가 달라짐

객체지향언어 => 파이썬 불완전 객체지향
상속 : 기존크래스 이용하여 새로운 클래스 생성.
캡슐화 : 접근제어자. 파이썬에는 없다
다형성 : 상속에 의해 객체를 다른 형태로 봄
         오버로딩(메서드의 다형성)


'''

# class Car :   # 클래스 정의
#     color = ''  # 멤버변수
#     speed = 0 # 멤버변수
#     def upSpeed (self, value) : # 맴버함수, 맴버메서드
#         self.speed += value       # self 자기참조값 , 고유id num
#     def downSpeed(self, value) :
#         self.speed -= value       # 객체내에서만 가능해서 전역변수로 넣으면 안됨 

# mycar1 = Car() # myxar1은 Car클래스의 객체다
# mycar1.color = '빨강'
# mycar1.speed=0

# mycar2 = Car()
# mycar2.color = '노랑'
# mycar2.speed=0

# mycar3 = Car()
# mycar3.color = '파랑'
# mycar3.speed=0

# mycar1.upSpeed(30)
# print('자동차 1의 색상은 %s이며, 현재 속도는 %dkm입니다.'
#       %(mycar1.color, mycar1.speed))
# mycar2.upSpeed(60)
# print('자동차 2의 색상은 %s이며, 현재 속도는 %dkm입니다.'
#       %(mycar2.color, mycar2.speed))
# mycar3.upSpeed(10)
# print('자동차 3의 색상은 %s이며, 현재 속도는 %dkm입니다.'
#       %(mycar3.color, mycar3.speed))

# '''
# 생성자 : 객체화시 관여하는 메서드
#         클래스의 가장중요한 기능은 객체생성
#         생성자 없으면 객체생성 불가
#       __init__ 형태로 생성자 구현함
      
#     클래스 정의 시 생성자를 구현하지 않으면 기본으로 제공됨
    
    
# '''

# class Car :
#     color = ''
#     speed = 0
#     def __init__(self, v1, v2) : # 생성자 // 객체생성시 2개 값을 입력하도록 강제
#         self.color = v1 # 각 매개변수 기다리는 중  
#         self.speed = v2
#     def upSpeed (self, value) : 
#         self.speed += value     
#     def downSpeed(self, value) :
#         self.speed -= value 

# mycar1 = Car('빨강', 0)  # Car() 생성자 호출
# mycar1.upSpeed(30)
# print('색상 %s 속도 %d'%(mycar1.color, mycar1.speed))
# mycar2 = Car('노랑', 60)
# print('색상 %s 속도 %d'%(mycar2.color, mycar2.speed))


# # 클래스 멤버, 인스턴스 멤버
# class Car :
#     color = '' # 인스턴스 멤버
#     speed = 0 # 인스턴스 멤버
#     num = 0 # 인스턴스 멤버
#     count = 0 # 클래스 멤버
#     def __init__(self, v='') : #v='' 매개변수 없는 경우도 가능
#         self.color = v # 인스턴스 멤버
#         self.speed = 0 # 인스턴스 멤버
#         Car.count += 1 # 클래스 멤버
#         self.num = Car.count # 인스턴스 멤버
#     def printMessage(self) :
#         print('색상 : %s, 속도 : %dkm, 번호 : %d, 생산번호 :%s' %
#               (self.color, self.speed, self.num, Car.count))
# mycar1, mycar2, mycar3  = None, None, None # 객체가 없음

# mycar1 = Car()
# mycar1.speed = 30
# mycar1.printMessage()       
# mycar1.printMessage()
# mycar2 = Car()
# mycar2.speed = 50
# mycar1.printMessage() # 똑같은데 생산번호가 +1 왜냐하면 count를 공통으로 쓰니깐
# mycar2.printMessage()       
        
# # Car 클래스
# Car.count += 10
# print(mycar1.count)        
# print(mycar2.count)
# print(Car.count)        
# mycar1.printMessage()
# mycar2.printMessage()        
        
# mycar3 = Car('빨강')      
# mycar1.speed = 0
# mycar1.printMessage()       
        
# class Card :
#     kind = ''
#     number  = 0
#     no = 0
#     count = 0
#     def __init__(self, v='Spade', s=1) : #v='' 매개변수 없는 경우도 가능
#         self.kind = v # 인스턴스 멤버
#         self.number = s # 인스턴스 멤버
#         Card.count += 1 # 클래스 멤버
#         self.no = Card.count
#     def printMessage(self) :
#         print('색상 : %s, 속도 : %d, 번호 : %d, 생산번호 : %s'%
#               (self.kind, self.number, self.no, Card.count))            
        
# card1 = Card()
# card2 = Card('Heart')
# card3 = Card('Spade', 10)
# card1.printMessage()         
# card2.printMessage()               
# card3.printMessage()               
        
# class Car :
#     speed = 0
#     door = 3
#     def upSpeed(self, value) :
#         self.speed += value
#         print('현재속도(부모클래스):%d' % self.speed)

# class Sedan(Car) :       
#       pass # 자손클래스는 없고, 부모와 같다
    
# class Truck(Car) :
#     def upSpeed(self, value) :
#         self.speed += value
#         if self.speed > 150 :
#             self.speed = 150
#         print('현재속도(자손클래스) :%d' % self.speed) 

# sedan1 = Sedan()        
# truck1 = Truck()
# print('트럭 :', end='')        
# truck1.upSpeed(200)        
# print('승용차 :', end='')        
# sedan1.upSpeed(200)        
        
# # 다중상속
# class Container :
#     room = 1
# class MovingCar(Container, Car) :
#     pass
# mcar1 = MovingCar()
# mcar1.upSpeed(60)
# print('이동차량의 방갯수 :', mcar1.room, ', 문의갯수:', mcar1.door)       

# 부모클래스        
        
#1  
# print('123456-2234567'[7])
# jumin = input('"-"를 포함한 주민등록번호를 입력하세요')       
# if jumin[6] != '-' :
#     print('주민번호 입력오류') 
# else :    
#     if int(jumin[7]) == 1 | int(jumin[7]) == 3 :
#         print(jumin[7])
#         print('남자')
#     elif int(jumin[7]) == 2 | int(jumin[7]) == 4: 
#         print(jumin[7])
#         print('여자')
#     else :
#         print(jumin[7])      
#         print('내국인 아님')      
        
#2
# import re
# def check_enco(word): # 암호이면 True
#     return re.compile('[^0-9]').match(word) != None # 숫자 제외 특수문자 면
# encodi = 'abcdefghijklmnopqrstuvwxyz0123456789'

# def check_deco(word): # 복호이면 True
#     return re.compile('[0-9]').match(word) != None
# decodi = '`~!@#$%^&*()-_+=|[]{};:,./qwertyuiop'

# def code(x1) :
#     no = ''
#     if check_enco(x1) : # 암호가 맞으면
#       for i in range(0, len(x1)) : # 입력문자를 처음부터 끝까지
#          no += decodi[encodi.find(x1[i])] # 복호화
#       print(no)   
#       return
    
#     elif check_deco(x1) : # 복호가 맞으면
#       for i in range(0, len(x1)) : # 입력문자를 처음부터 끝까지
#          no += encodi[encodi.find(x1[i])] # 암호화 
#       print(no)  
#       return

# code('`qwer')



# 3
# import re
# def check_hex(no):
#     p = re.compile('[0-9a-fA-F]')
#     return p.match(no) != None
# unkn = input('숫자입력')
# if check_hex(unkn) :
#     print('10진수 :',int(no, 16))
# else :
#     print('16진수가 아님')   

# class Line :
#     length = 0
#     def __init__(self, length) :
#         # 멤버변수 => 매개변수
#         self.length = length
#         # 객체를 문자열로 변경
#     def __repr__(self) :
#         return '선의 길이 :' + str(self.length)
#         # 객체간 연산자 사용시 호출 메서드 
#     def __add__(self, other) :
#         print('+ 호출',end='')
#         return self.length + other.length
    
#     def __lt__(self, other) :
#         print('< 호출',end='')
#         return self.length < other.length
#     def __eq__(self, other) :
#         print('== 호출',end='')
#         return self.length == other.length
#     def __gy__(self, other) :
#         print('> 호출',end='')
#         return self.length > other.length

# myline1 = Line(200)
# myline2 = Line(100)
# print('myline1 :',myline1) # __repl__ 
# print('myline2 :',myline2)
# print('두선 길이의 합 :', myline1 + myline2)

# if myline1 < myline2 : # lt
#     print('myline2 가 더 길어요')
# if myline1 == myline2 : # eq
#     print('myline 가 같아요')
# if myline1 > myline2 : # gt
#     print('myline1 가 더 길어요')

# class Circle :
#     r = 0
#     def __init__(self, r) :
#         # 멤버변수 => 매개변수
#         self.r = r
#         # 객체를 문자열로 변경
#     def __repr__(self) :
#         PI = 3.141592
#         def getArea(r) :
#             return (r**2)*PI
#         def getLength(r) :
#             return (2*r)*PI
#         return '반지름:'+str(self.r)+',넓이:'+str(round(getArea(self.r),2))+',둘레:'+str(round(getLength(self.r),2))
#         # 객체간 연산자 사용시 호출 메서드 
#     def __add__(self, other) :
#         print('+ 호출',end='')
#         return self.r + other.r
    
#     def __lt__(self, other) :
#         print('< 호출',end='')
#         return self.r < other.r
#     def __eq__(self, other) :
#         print('== 호출',end='')
#         return self.r == other.r
#     def __gy__(self, other) :
#         print('> 호출',end='')
#         return self.r > other.r
# # + add
# # - sub
# # * mul
# # / truediv
# # // floordiv
# # %mod
# # **pow

# # & and
# # \ or
# # ^ xor

# # < lt
# # > gt
# # <= le
# # >= ge
# # == eq
# # != ne
# # 

# Circle1 = Circle(10)
# Circle2 = Circle(5)
# print('Circle1 :',Circle1) # __repl__ 
# print('Circle2 :',Circle2)
# print('두선 길이의 합 :', Circle1 + Circle2)

# if Circle1 < Circle2 : # lt
#     print('Circle2 가 더 길어요')
# if Circle1 == Circle2 : # eq
#     print('Circle 가 같아요')
# if Circle1 > Circle2 : # gt
#     print('Circle1 가 더 길어요')

# 추상함수 : 부모클래스의 멤버함수를 자손클래스에서 오버라이딩 하도록 강제하는 함수
class Superclass :
    def method(self) :
        raise NotImplementedError
class SubClass(Superclass) :
    # pass
    def method(self) :
        print('subClass에서 SuperClass의 method 함수를 오버라이딩(덮어쓰기)')
sub1 = SubClass()
sub1.method()
import pysuup4 as ps
print(ps.add(3,4))

# from pysuup4 import add 
# print(add(3,4))
print('pysuup4.__name__',dir(ps))






























