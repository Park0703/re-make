# 1
h = int(input('높이'))
for i in range(1,  h+1) :
    print('{:^9}'.format('*'*(2*i-1)))



# 2
y = int(input('year?'))
if y % 4 == 0 :
    print('평년')5
else :
    if y % 100 == 0 :
        print('평년')
    else :
        if y % 400 == 0 :
            print('윤년')
        else :
            print('평년')

# 3 
sum = 0
for i in range(1, 1000, 2) :
    sum += i
    if sum > 1000 :
        print(i, sum)
        break

#4
for i in range(-20, 51) :
    hwa = ((9/5)*i)+32
    print('섭시온도 :', i, '화씨온도 :', hwa)

#5
co = int(input('금액을 입력해주세요 :'))
for i in (500, 100, 50, 10, 1) :
    if co != 0 :
        print(i,'원 동전의 갯수 :',co//i)
        co = co%i