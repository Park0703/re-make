#클래스 붕어빵 기계의 틀, 재료넣으면 계속 뽑아냄, 연관이 있는 함수의 집합
#일반유닛
class unit:
    def __init__(self, name, hp, damage): # 언더바 2번
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다".format(self.name))
        print("체력{0}, 공격력{1}".format(self.hp, self.damage))
                
marine1 = unit("마린", 40, 5)
marine1 = unit("마린", 40, 5)
tank = unit("탱크", 150, 35) # self를 제외한 모든 정보를 다 넣어줘야 함

#마린과 탱크는 unit의 이닛
#__init__ 객체를 만들때 자동으로 호출되는 생성자


# 멤버변수 self.xx 클래스내 정의된 변수, 초기화 및 사용가능

#레이스 : 공중기능, 비행, 클로킹 기능

wraith1 = unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

#마인드컨트롤
wraith2 = unit("레이스", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))

#메소드
class attackunit:#(unit): #상속하는법(상속클래스)
    def __init__(self, name, hp, damage): # 언더바 2번
        self.name = name
        self.hp = hp
        self.damage = damage
#공격함수
    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
#피해함수
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
            
#파이어뱃
firebat1 = attackunit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격2번
firebat1.damaged(25)           
firebat1.damaged(25)

#상속 물려받기
class unit: #부모 클래스
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class attackunit(unit):#(unit): #상속하는법(상속클래스) # 자식클래스
    def __init__(self, name, hp, damage):
        unit.__init__(self, name, hp) # 상속됨
        self.damage = damage # 별도 설정

class flyableunit:#(unit): #상속하는법(상속클래스) # 아내클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
class flyableattackunit(attackunit, flyableunit):#(unit): #상속하는법(상속클래스) # 손자클래스
    def __init__(self, name, hp, damage,  flying_speed):
        unit.__init__(self, name, hp, damage) #attackunit 상속됨
        flyableunit.__init__(self.flying_speed) #flyableunit 상속됨
        
#연산자 오버로딩  부모클래스 이외에 자식클래스 정의 매소드를 가져와서 새로 정의해서 쓰기     
#unit move /// #move재정의     
        
        
#pass        
class building(unit):
    def __init__(self, name, hp):
        pass
supply_depot = building("서플라이디폿", 500)  

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass  #게임오버는 그냥 넘겨버림

game_start()
game_over()
        
        
#super
class building(unit):
    def __unit__(self, name, hp):
        super().__init__(name, hp, 0) # 셀프없이
        # 다중 상속할떄는 문제발생        
        #super().__init__() #super 가장 마지막 부분만 상속해줌
        unit.__init__(self)   #그래서 별도로 표시해줘야함.
        flyableunit.__init__(self)   #그래서 별도로 표시해줘야함.
        
        
        
        
        