print('Hello World')

# 기본출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
# sep= separator ' '은 ' '부분에 들어갈 것을 정의 하고, 매번 출력한다. 
print('P','y','t','h','o','n', sep=' ')
print(sep=',')
# 결과값이 P y t h o n으로 됨.
print('010', '7777', '1234', sep='-')
# 결과값이 010-7777-1234가 됨

# end 옵션
# 특정 단어마다 엔터를 치게 되면 기니깐 end 옵션으로 길게 볼 수 있게 해줌
print('welcome to', end=' ')
print('IT news', end=' ')
print('web site')
print()
# file 옵션
# 예약어 = 예약어는 이미 파이썬에서 정의 내린거라 별도로 정의할 수 없음
import sys
print('learn python', file='sys.stdout')
#file= 이 내용을 외부(하드디스크, usb)에 특정파일로 쓸것이다. 
# sys.stdour 은 콘솔아웃을 의미, terminal에서 안나옴

# ★format 사용 (d, s, f)
# d는 정수, digit : 3
# s는 문자열, 
# f는 float 소수 3.424214123
print('%s %s' %('one', 'two'))
#s는 이어진 문자열을 처리할 수 있음

print('{0} {1}'.format('one', 'two'))
#maping이 되는 것: 짝이 맞는 것이 깔끔한 것
print('{1} {0}'.format('one', 'two'))



