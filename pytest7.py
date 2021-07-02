
# 1 
# list1 = [x for x in range(1, 10)]
# print(list1)
# list2 = [x for x in range(11, 20)]
# print(list2)

# # 2
# list3 = list(map(lambda l1, l2 : l1+l2, list1, list2))
# print(list3)

# # 3 
# def mean(x) :
#     return sum(x) / len(x) 
# print("평균:", mean(list3))
# # 4
# def median(x) :
#     return x[int(len(x)/2)] 
# print("중간값:",median(list3))
# # 5
# import math as m
# def sd(x) :
#     ssd = 0
#     for i in x :
#         ssd += m.pow(i - mean(x), 2)
#     return pow(ssd / len(x), 1/2) 
# print("표준편차:",sd(list3))


# 평가자 체크리스트


# 1. test0622.xlsx 파일을 읽어 df 변수에 저장하기. index이름은 학생의 이름으로 한다.
from openpyxl import load_workbook
import pandas as pd
df1 = pd.read_excel('test0622.xlsx', engine = 'openpyxl')
df1 = pd.DataFrame(df1,
                   columns=['알고리즘','파이썬','R'])
print(df1)

# df1.set_index(df1.iloc[0], drop=True)
# # 1) df 지정에서 인덱스 지정
print(df1.iloc[0])

# 2) 사전에 레코드 컬럼값으로 입력 후 
# index = ['홍길동', '김삿갓', '이몽룡']
# df1.set_index(' ', inplace = True)

# 3) 원본 수정 .. 이건 불법이지만 향후 문제를 푸는데 가능
# df1 = pd.DataFrame(df1)


# print(df1)

# 2. 알고리즘 과목의 평균을 구하여 출력하는 코드
# print(df1['알고리즘'].mean())

# 3. 파이썬 과목의 중간값을 구하여 출력하는 코드 작성하기
# print(df1['파이썬'].median())

# 4. R 과목의 표준편차값을 구하여 출력하는 코드 작성하기
# print(df1['R'].std())
# 5. 각 과목의 상관계수를 출력하는 코드 작성하기
# print(df1.corr())
# 6. 홍길동 학생의 과목 평균을 구하는 코드를 작성하기
# print(df1.iloc[0].mean(axis=1))
# 7. 각 과목별 합계을 구하는 코드 작성하기
# print(df1.sum())
# 8. 각 이름별 합계을 구하는 코드 작성하기
# print(df1.sum(axis=1))














