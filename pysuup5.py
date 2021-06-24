# 정규식
# data = '''
# park 800905-123456
# kim 700905-123456
# choi 850101-a123456
# '''
# result = []
# for line in data.split('\n') :
#     word_result = []
#     for word in line.split(' ') :
#         if len(word) == 14 and word[:6].isdigit and\
#             word[7:].isdigit():
#             word = word[:6]+'-'+'*******'
#         word_result.append(word)
#     result.append(' '.join(word_result))
# print('\n'.join(result))

# import re
# pat = re.compile("(\d{6,7})[-]\d{7}")
# print(pat.sub('\g<1>-*******', data))
# () 그룹
# \g<1> 1번째 그룹
# [] 문자
# {n} n개 갯수
# ca{2,5}t a문자가 2개이상 5개 이하
# ct : false
# cat : false
# caat : true
# caaat : true
# \d 숫자
# ? : 0 또는 1  없거나 1개만 가능
# ca?t // ct true cat true caat false 
# * 0 개이상
# ca*t // ct true, cat true, caat true
# + 1 개 이상
# ca+t // ct false, cat true, caat true
# \s 공백
# \s+ 공백 문자 1개 이상
# 
# 
# 
# 
# #
# 1

# class Rect :
#     h = 0
#     b = 0
#     def __init__(self, height, base) :    
#         self.h = height
#         self.b = base        
#     def __repr__(self) :
#         def getArea(h, b) :
#             return h*b
#         def getLength(h, b) :
#             return (h+b)*2         
#         return '넓이 :'+str(getArea(self.h, self.b))+', 둘레:'+str(getLength(self.h, self.b))
      
#     def getArea(h, b) :
#         return h*b
#     def getLength(h, b) :
#         return (h+b)*2 
      
#     def __lt__(self, other) :
#         print('< 호출',end='')
#         return self.getArea() < other.getArea()
#     def __eq__(self, other) :
#         print('== 호출',end='')
#         return self.getArea() == other.getArea()
#     def __gy__(self, other) :
#         print('> 호출',end='')
#         return self.getArea() > other.getArea()
      
# if __name__ == "__main__" :
#   rect1 = Rect(10,20)
#   rect2 = Rect(10,10)
#   print(rect1)
#   print(rect2)
#   if rect1 > rect2 :
#     print(rect1.area(),"면적이 더 큰 사각형 입니다.")
#   elif rect1 < rect2 : 
#     print(rect2.area(),"더 큰 사각형 입니다.")
#   elif rect1 == rect2 :
#     print(rect1.area(),"=",rect2.area(),"같은 크기의 사각형 입니다.")

# 2
# class Calculator:
#   value = 0
#   def __init__(self):
#     self.value = 0

#   def add(self,val):
#     self.value += val

# class UpgradeCarculator(Calculator):
#   def minus(self,val):
#     self.value -= val
# def new_func():
#     ​

# new_func()

# if __name__ == "__main__" :
#    cal = UpgradeCalculator()
#    cal.add(10)
#    cal.minus(7)
#    print(cal.value) # 10에서 7을 뺀 3을 출력
#3
# class MaxLimitCalculator(Calculator):
#   def add(self, val):
#   self.value += val
#     if self.value > 100:
#       self.value=100

# import re
# str1 = 'The quick brown fox jumps over the laze dog Te Thhhe'
# str_list = str1.split()
# print(str_list)
# pattern = re.compile('Th*e')
# count = 0
# for word in str_list :
#     if pattern.search(word) :
#         count += 1
# print('결과1 : {0:s}:{1:d}'.format('갯수', count))

# # re...I 대소문자 구분없이
# pattern = re.compile('Th*e', re.I)
# count = 0
# for word in str_list :
#     if pattern.search(word) :
#         count += 1
# print('결과2 : {0:s}:{1:d}'.format('갯수', count))

# # 결과2 에 맞는 문자열 출력
# print('결과3 :', end = '')
# for word in str_list :
#     if pattern.search(word) :
#         print(word, end=',')
# print()

# # 결과2에 맞는 문자열 리스트로 저장하기
# print('결과4 :', re.findall(pattern, str1))
# print('결과5, 갯수 :', len(re.findall(pattern, str1)))

# #패턴에 맞는 문자열로 치환하기
# pattern = re.compile('Th*e')
# print('결과 6:', pattern.sub('*',str1))
# print('결과 7:', pattern.sub('a',str1))

# # str2 문자열 온도의 평균을 출력하기
# str2 = '서울 : 25도, 부산 : 23도, 대구: 27도, 광주 : 26도, 대전 : 25도'
# pattern1 = re.compile('\\d+')
# str2_list = str2.split(',')
# list1 = re.findall(pattern1, str2)
# list1 = list(map(int, list1))
# print(sum((list1)) / len(list1))

# # 파일 읽기
# infp = None
# inStr = ''
# #open('파일이름', '파일읽기 설정', '인코딩 방식') 
# # r 읽기 모드
# # w 쓰기 모드, 파일이 존재하지 않으면 파일 생성 존재하면 내용 변경
# # a 쓰기 모드,                          파일이 존재하면 내용이 추가됨
# # t 텍스트 모드,기본값
# # b 이진 모드 binary 모드, 이미지, 동영상
# # infp = open("test0616.py","rt", encoding="UTF8")
# # while True :
# #     inStr = infp.readline()
# #     if inStr == None or inStr == '':
# #         break
# #     print(inStr, end = '')
# # infp.close()


# # 파일에 데이터 저장하기
# # outfp = open('data.txt', 'w', encoding='UTF8')
# # while True :
# #     outStr = input('내용입력 =>')
# #     if (outStr == '') :
# #         break
# #     outfp.writelines(outStr+'\n')
# # outfp.close()
# # print('프로그램 종료')

# outfp = open('data.txt', 'r', encoding='UTF8')
# while True :
#     outStr = outfp.readline()  # 한줄씩 읽음
#     if outStr == None or outStr == '':
#         break
#     print(outStr, end = '')
# outfp.close()

# infp = open('data.txt', 'r', encoding='UTF8')
# print(infp.read()) # 처음부터 끝까지 문자열로 반환, 바이너리도 가능
# infp.close()

# infp = open('data.txt', 'r', encoding='UTF8')
# print(infp.readlines())  # 처음부터끝까지 한줄씩 분리하여 리스트로 반환
# infp.close()

# infp = open('data.txt', 'r', encoding='UTF8')
# for str_line in infp.readlines() :
#     print(str_line, end='')  # 처음부터끝까지 한줄씩 분리하여 리스트로 반환
# infp.close()

# # 파일 존재여부 확인
# import os.path
# file = 'data.txt' # 상대 경로, 현위치에서 얼마나 바뀌었는가
# if os.path.isfile(file) :
#     print(file, '은 파일입니다.')
# elif os.path.isdir(file) :
#     print(file, '은 폴더입니다.')
    
# if os.path.exists(file) :
#     print(file, '은 존재합니다.')
# else :
#     print(file, '은 없는 파일 입니다.')    
    
# import os
# print(os.getcwd()) #   작업폴더 기준
    
# file = 'C:/Users/pc/Desktop/PYTHON/data.txt'    # 절대 경로
# print(os.path.basename(file))
# # 폴더의 하위 폴더 목록 조회하기
# # dirName 조회대상 폴더
# # subDirList 조회폴더의 하위폴더 목록 리스트리턴
# # fnames : 조회폴더의 하위 파일 이름 목록 리스트로 리턴
# print('폴더 목록 보기 : os.walk 모듈 사용')
# for dirName, subDirList, fnames in os.walk('C:/Users/pc/Desktop/PYTHON') :
#     for fname in fnames :
#         print(os.path.join(dirName, fname))
#     print(subDirList)

# import os
# print('현재 운영체제 : ', os.name)
# print('현재 폴더 : ', os.getcwd())
# print('현재 폴더 하위정보 목록 : ', os.listdir())

# # # 폴더 생성하기
# # os.mkdir('temp')
# # file = 'C:/Users/pc/Desktop/PYTHON/temp'    # 절대 경로
# # print(os.path.basename(file))
# # outfp = open('indata.txt', 'w', encoding='UTF8')
# # while True :
# #     outStr = input('내용입력 =>')
# #     if (outStr == '') :
# #         break
# #     outfp.writelines(outStr+'\n')
# # outfp.close()
# # print('프로그램 종료')


# # # 폴더 삭제하기 // 안에 파일이 존재하면 안됨
# # os.rmdir('temp')

# # outfp 파일을 close() 구문 없이 코딩하기
# with open('temp/indata.text', 'w', encoding = 'UTF8') as outfp :
#     outfp.write('hello\nhello\n')

# # 파일 삭제하기
# os.remove('temp/indata.txt')
# # temp 폴더 삭제하기
# os.rmdir('temp')

# # mod2.py 파일읽어서 mod2.bak 파일로 복사하기
# infp = open('mod2.py', 'r', encodin='UTF8')
# outfp = open('mod2.bak', 'w', encodin='UTF8')

# while True :
#     inStr = infp.readline()
#     if inStr == ' ' :
#         break
#     outfp.writelines(inStr)
# infp.close()
# outfp.close()
# print('프로그램 종료')

#이미지 파일 읽기
# infp = open('apple.png', 'rb') # b를 해줘야 이진파일인 것을 앎
# outfp = open('apple2.png', 'wb')
# while True :
#     inStr = infp.read()

#     if not inStr :
#         print(inStr)   
#         break
#     outfp.write(inStr)
# infp.close()
# outfp.close()

# 홍길동,100
# 김삿갓,50
# 이몽룡,90
# 임꺽정,80
# import os
# import re
# infp = open('data.txt', 'r', encoding='UTF8') # b를 해줘야 이진파일인 것을 앎
# inStr = infp.read()
# print(inStr)
# pattern = re.compile(r'\d{2,3}')
# list1 = re.findall(pattern, inStr)
# print(list1)
# list1 = list(map(int, list1))
# print('점수합계 : ', sum(list1),', 평균 :', sum(list1) / len(list1))



















    