'''
1. main이 실행 되도록  Rect 클래스 구현하기
    가로,세로를 멤버변수로.
    넓이(area),둘레(length)를 구하는 멤버 함수를 가진다
    클래스의 객체를 print 시 :  (가로,세로),넓이:xxx,둘레:xxx가 출력
'''    
class Rect :
    w=0
    h=0
    def __init__(self,w,h) :
        self.w = w
        self.h = h
    def __repr__(self) :
        return "(%d,%d), 넓이:%d,둘레:%d" % \
       (self.w,self.h,self.area(),self.length())
    def __gt__(self,other) :
        return self.area() > other.area()
    def __lt__(self,other) :
        return self.area() < other.area()
    def __eq__(self,other) :
        return self.area() == other.area()
    def area(self) :
        return self.w * self.h
    def length(self) :
        return (self.w + self.h) * 2
    

if __name__ == "__main__" :
     rect1 = Rect(10,20)
     rect2 = Rect(10,10)
     print(rect1)
     print(rect2)
     if rect1 > rect2 :
         print(rect1.area(),"면적이 더 큰 사각형 입니다.")
     elif  rect1 < rect2 :  
         print(rect2.area(),"더 큰 사각형 입니다.")
     elif rect1 == rect2 :
         print(rect1.area(),"=",rect2.area(),"같은 크기의 사각형 입니다.")
'''
2. main 이 실행 되도록, Calculator 클래스를 상속받은 
   UpgradeCalculator  클래스 구현하기
'''   
class Calculator:
      value=0
      def __init__(self):
           self.value = 0

      def add(self, val):
          self.value += val

class UpgradeCalculator(Calculator) :
      def minus(self, val):
          self.value -= val
    

cal = UpgradeCalculator()  #객체화 
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력

'''
3. 2번에서 구현한 Calculator 클래스를 이용하여 
   MaxLimitCalculator 클래스 구현하기
MaxLimitCalculator 클래스에서 value 값은 절대 100 이상의 값을 가질수 없다.
'''

class MaxLimitCalculator(Calculator) :
      def add(self, val):   #오버라이딩 
          self.value += val
          if self.value > 100 :
              self.value = 100
    
cal = MaxLimitCalculator()
cal.add(500) # 50 더하기
cal.add(600) # 60 더하기
print(cal.value) # 100 출력

