# Chapter02-1
# 파이썬 완전 기초
# print 사용법
# 
print('%10s' % ('nice'))
#s는 10개 자릿수
print('{:>10}'.format('nice'))
#10자리 확보하고
#        nice

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
#음수면 오른쪽부터 채움
#nice       

print('{:_>10}'.format('nice'))
#언더바'_'로 넣으면
print('{:^10}'.format('nice'))
#^은 가운데 정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
#.은 왼쪽부터 5글자 절삭을 시킴, 허가
print('{:10.5}'.format('pythonstudy'))

## %d
print('%d %d' % (1,2))
print('{}{}'. format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%1.18f' % (3.143413))
print('{:f}'.format(3.143413))


print('%06.2f' % (3.14232132141))
#정수부는 6자리, 그 나머지는 0으로 채움. 소수자릿수는 2f인 14만큼
print('{:06.2f}'.format(3.1423213214))
#sd를 명시를 잘하고, 정수부와 소수부f도 잘 구분해야한다.

# file indexing 

