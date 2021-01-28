#예외처리
#잘못 INPUT이 된 상황
try :  
    print("나누기 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하게쇼 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
    # 예외넣었을 때 ValueError: invalid literal for int() with base 10: 'r'
except ValueError :
    print("에러! 잘못된 값을 입력하였습니다.")
# 0 으로 나누면? ZeroDivisionError: division by zero

except ZeroDivisionError :
    print("에러! 0을 입력하였습니다.")

except Exception as err :
    print("에러! 알 수 없는 에러가 발생하였습니다.")

