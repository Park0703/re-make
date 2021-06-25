# # db 처리 => 오라클에서 혹시 알고 있다면 같은 팀 개인채팅

# import sqlite3
# dbpath = 'test.sqlite' # 데이터베이스 파일
# conn = sqlite3.connect(dbpath) # dbpath 파일에 데이터 저장
# cur = conn.cursor()            # sql 구문 실행하기 위한 객체
# # executescript                  # 여러개의 문장을 실행
# cur.executescript('''           
#     drop table if exists items ;
#     create table items (item_id integer primary key,
#         name text unique, price integer);
#     insert into items (name, price) values ('Apple', 800) ;
#     insert into items (name, price) values ('Orange', 500) ;
#     insert into items (name, price) values ('Banana', 300) ;     
# ''')
# conn.commit()    # 실제로 cur sql 문장 실행완료
# cur = conn.cursor() # sql 구문 실행하기 위한 객체
# cur.execute('select * from items') #한개의 sql문장 실행 vs executescript 
# item_list = cur.fetchall() # cur 실행후 결과값 모두리턴
# print(item_list)
# print(type(item_list))
# print(type(item_list[0]))

# for item_id, name, price in item_list :
#     print(item_id, name, price)

# for item in item_list :
#     print(item[0], item[1], item[2])

# '''
# 프로그램 =(conn:db연결 // cur:db명령전달 //)> db파일
# '''

# # 레코드 한개씩 조회
# cur = conn.cursor() 
# cur.execute('select * from items')
# while True : 
#     row = cur.fetchone()
#     if row == None :
#         break ;
#     print(row[0], row[1], row[2])

# # 레코드 추가하기
# sql = "insert into items (name, price) values ('Peach', 3000)"
# cur = conn.cursor() # sql구문 실행하기 위한 객체
# cur.execute(sql)
# conn.commit()

# cur = conn.cursor() # sql구문 실행하기 위한 객체
# cur.execute('select * from items')
# item_list = cur.fetchall()
# print(item_list)
# conn.close()
# # 'iddb' sqlite db를 생성하기

# dbpath1 = 'iddb.sqlite' # 데이터베이스 파일
# conn = sqlite3.connect(dbpath1) # dbpath 파일에 데이터 저장
# cur = conn.cursor()      

# cur.executescript('''           
#     drop table if exists usertable ;
#     create table usertable (id char(4) primary key,
#         username char(15), email char(15), birthyear int);
# ''')

# # cur.executescript('''           
# #     insert into items (id, username, email, birthyear) 
# #         values ('Apple', 800) ;
# # ''')

# # while True :
# #     d1 = input('사용자id=>')
# #     if d1 == '':
# #         break
# #     d2 = input('사용자이름 =>')
# #     d3 = input('이메일=>')
# #     d4 = input('출생년도=>')
# #     # 숫자형으로 들어가는 부분이랑 작은 따옴표 안들어감
# #     sql = "insert into usertable values ('"+d1+"','"+d2+"','"+d3+"',"+d4+")"
# #     print(sql)
# #     cur.execute(sql)
# #     conn.commit()
# # conn.close()

# # 데이터 조회
# # conn = sqlite3.connect(dbpath1)
# # cur = conn.cursor() 
# # cur.execute('select * from usertable')
# # user_list = cur.fetchall()
# # for u in user_list :
# #   print(u)
# # conn.close()

# data = [('test4','테스트4','test4@naver.com', 1991),
#         ('test5','테스트5','test5@naver.com', 1992),
#         ('test6','테스트6','test6@naver.com', 1993),
#         ('test7','테스트7','test7@naver.com', 1994)]

# # 불편하니깐 편리한 방법
# conn = sqlite3.connect(dbpath1)
# cur = conn.cursor()   
# while True :
#     d1 = input('사용자id=>')
#     if d1 == '':
#         break
#     d2 = input('사용자이름 =>')
#     d3 = input('이메일=>')
#     d4 = int(input('출생년도=>'))
#     # 숫자형으로 들어가는 부분이랑 작은 따옴표 안들어감
#     sql = "insert into usertable values (?,?,?,?)"
#     param = []
#     param.append(d1)
#     param.append(d2)
#     param.append(d3)
#     param.append(d4)
#     cur.executemany(sql, param, data)
#     conn.commit()
#     # 기계어번역 => 파라미터값 대기 =>  db에 추가
# cur.execute('select * from usertable')
# user_list = cur.fetchall()
# for u in user_list :
#     print(u)
# conn.close()

# #데이터 삭제
# conn = sqlite3.connect(dbpath1)
# cur = conn.cursor()   
# cur.execute("delete from usertable where id = 'test7'")
# conn.commit()
# conn.close
# #데이터변경
# conn = sqlite3.connect(dbpath1)
# cur = conn.cursor()   
# cur.execute("update usertable set birthyear = 1991  where id = test1")
# conn.commit()
# conn.close

# #1건만 조회
# conn = sqlite3.connect(dbpath1)
# cur = conn.cursor()   
# cur.execute("select * from usertable where id = 'test1'")
# id, name, email, year = cur.fetchone()
# print('id :', id,', 이름:', name, ', 이메일 :', email, ', 출생연도 :', year)
# conn.close

# 오라클 접속하기
# pip install cx_Oracle
# 
# import cx_Oracle

# # 1 #
# import cx_Oracle
# conn = cx_Oracle.connect('kic','1234','localhost/xe')
# cur = conn.cursor()

# while True :
    # de = input('sql 입력하세요 \n')
    # if de == '' :
        # break 
    # cur.execute(de)
    # de_list = cur.fetchall()
    # print('조회 레코드 수 :',len(de_list), '조회 컬럼 수 :',len(de_list[0]))
    # for d in de_list :
        # print(d)
# conn.close()

# # 2 #
# import os.path

# while True :
    # file = input('원본파일의 이름을 입력하세요 : ')
    # if os.path.exists(file) :
        # copy = input('복사본파일의 이름을 입력하세요 : ')
    # with open(file,'r',newline='',encoding='utf8') as infp:
        # with open(copy,'w',encoding='utf8') as outfp:
    # header = infp.readline()
    # header = header.strip()
    # header_list = header.split(",")
    # outfp.write(','.join(map(str,header_list))+'\r\n')
    # for row in infp:
        # outfp.write(row)
        # print('복사완료')
    # else :
        # print('원본파일이 존재하지 않습니다.')
        # break

# import os.path
# def copyfile(c) :
#     if os.path.exists(myfile) :
#         try : 
#             with open(myfile, 'r', newline = '', encoding = 'UTF8') as infp :
#                 copiedfile = input('복사본파일이름')
#                 with open (copiedfile, 'w', encoding = 'UTF8') as outfp :
#                     header = infp.readline()
#                     header = header.strip()
#                     header_list=header.split(',')
#                     outfp.write(','.join(map()))
#         except:
#             print('wrong')
        
        
        
# infile = input('원본팓일이름')
# try :
#     inFp : open(infile, 'r', encoding = 'utf-8')
#     outfile = input('복사본')
# except :
#     print('원본 파일이 존재하지 않았습니다.')

# ##################
# xlsx 파일읽기 pip install openpyxl
# xls

# import openpyxl
# filename = 'sales_2015.xlsx'
# book = openpyxl.load_workbook(filename)
# sheet = book.worksheets[0]
# data = [] # 모든데이터 정보를 리스ㅡ로 저장, 리스트로 한행 저장,
# for row in sheet.rows :
#     line = [] # 한행의 셀값을 리스트 저장
#     for l, d in enumerate(row) :
#       # list에서 data와 index를 동시에 제공
#       # l index, d data 
#         print(l,',',d,',',d.value)
#         line.append(d.value)
#     print(line) # 한행 데이ㅌ터를 리스트로 저장
#     data.append(line)
# # print(data)

# # enumerate 함수로 data 조회
# for i, d in enumerate(data) :
#     print(i+1, ':', d)
    
# import openpyxl
# filename = 'sales_2015.xlsx'
# book = openpyxl.load_workbook(filename)
# # book.worksheets 모든 sheet 정보
# # sheet : sheet 정보 하나
# for i, sheet in enumerate(book.worksheets) :
#     print(book.sheetnames[i]) # sheet names
#     data = []
#     for r, row in enumerate(sheet.rows) :
#         line = []
#         for i, c in enumerate(row) :
#             line = []
#             line.append(c.value)
#         print(r+1, ':', line)
#         data.append(line)

# xls 파일 읽기
# pip install xlrd
from xlrd import open_workbook
# infile = 'ssec1804.xls'
# workbook = open_workbook(infile)
# print('sheet의 갯수 :', workbook.nsheets)
# # workbook.sheets() xls 파일의 sheet 데이터들
# # worksheet 한개의 sheet 정보
# for worksheet in workbook.sheets() :
#     print('worksheet 이름 :', worksheet.name)
#     print('행의 수:', worksheet.nrows)
#     print('컬럼의 수 :', worksheet.ncols)
#     for row_index in range(worksheet.nrows) :
#         for column_index in range(worksheet.ncols) :
#           # worksheet.cell_value 행의 인덱스, 열의 인덱스
#             print(worksheet.cell_value(row_index, column_index),
#                   ',',end='')
#         print()
# pandas

# pip install pandas
import pandas as pd 
# infile = 'sales_2015.xlsx'
# # sheet_name = None  모든 sheet 읽기
# # index_cal None 인덱스 컬럼없음으로 설정
# df = pd.read_excel(infile, sheet_name = None, index_col = None)
# row_output = [] # 모든 sheet의 데이터 저장
# for worksheet_name, data in df.items() :
#     print('===', worksheet_name, '===')
#     # data 중 판매가격이 200 초과 되는 데이터만 row output 리스트에 저장
#     # 판매가격에 $ 콤마를 제거하고 숫자형태로 변형
#     row_output.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > 200.0])
# #ales_all_2015.xlsx에 row_output데이터 저장하기
# #pd.concat : row_output 데이터 연결하기
# # axis = 0 row 연결 # axis = 1 col 연결
# # ignore_index = True 인덱스 없음
# filtered_row = pd.concat(row_output, axis=0, ignore_index=True)
# print(type(filtered_row))
# writer = pd.ExcelWriter('sales_all_2015.xlsx', engine= 'openpyxl')
# #to_excel 데이터 프레임 객체를 엑셀형태 데이터로 변경
# filtered_row.to_excel(writer, sheet_name = 'sale_2015', index = False)
# writer.save()

# pd 로 xls 파일,,, sheet 여러개 저장하기
# import pandas as pd
# infile = 'ssec1804.xls'
# outfile = 'ssec1804_bak.xls'
# writer = pd.ExcelWriter(outfile) # 복사될 파일
# df = pd.read_excel(infile, sheet_name = None, index_col=None)
# for worksheet_name, data in df.items() :
#     print('===',worksheet_name,'===')
#     print(data)
#     # 복사될 파일의 sheet 한개 생성
#     data.to_excel(writer,sheet_name=worksheet_name, index=False, header=False)
# writer.save() # 파일로 엑셀 데이터 생성
# writer.close() # 저장 완료 후 파일 연결 종료

import pandas as pd
import xlrd
# dict > series
# dict_data = {'a':1, 'b':2, 'c':3}
# sr = pd.Series(dict_data)
# print(type(sr))
# print(sr)
# # a idx   1 values
# # b    2
# # c    3
# print(sr.index) # abc
# print(sr.values) # 123

# # list > series
# list_data = ['2019-01-02', 3.14, 'ABC', 100, True] 
# # 인덱스값이 없으면 숫자를 붙여줌
# sr = pd.Series(list_data)
# print(sr)
# print(sr.index)
# print(sr.values)

# # 튜플 > series
# tup_data = ('길동', '1990-01-01','남',True)
# sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
# print(sr)
# print(sr.index)
# print(sr.values)

# # 시리즈 데이터 조회
# # 원소 1개 선택
# print(sr[0]) # 첫번째 데이터
# print(sr['이름']) # 인덱스명으로 조회
# # 원소 여러개
# print(sr[[1,2]]) # 1,2번 idx 조회
# print(sr[['생년월일','성별']])
# print(sr[[0,3]])
# print(sr[['이름','성별']])
# # 원소 여러개, 범위지정
# print(sr[1:2]) # 1번 인덱스 부터 2번 앞인덱스까지
# print(sr['생년월일':'성별']) # 인덱스 명 순서대로 조회



# # 데이ㅌ터 프레임 생성하기
# import pandas as pd
# dict_data = {'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}
# df = pd.DataFrame(dict_data)
# print(df)
# print(type(df))

# df = pd.DataFrame([[15,'남','서울중'],[17,'여','서울고']],
#                   index=['길동','길순'], # index 행이름
#                   columns=['나이', '성별','학교']) # col 열의 이름
# print(df)
# print(type(df))
# print(df.index)
# print(df.columns)

# # df.index=['학생1','학생2'], # index 행이름
# # df.columns=['연령', '남녀','소속']
# # print(df)
# # print(type(df))
# # print(df.index)
# # print(df.columns)

# df.rename(columns = {'나이' : '연령', '성별' : '남녀', '학교' : '소속'}, inplace = True)
# print(df)
# print(df.index)
# print(df.columns)
# df.rename(index = {'길동' : '학생1', '길순' : '학생2'}, inplace = True)
# print(df)
# print(df.index)
# print(df.columns)

# exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95], '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
# edf = pd.DataFrame(exam_data, index = ['홍길동', '이몽룡', '김삿갓'])
# print(edf)
# print('mean :\n', edf.mean()) # 전체 각 컬럼 별 평균
# print('수학mean :', edf['수학'].mean()) # 열 평균
# print('수학mean :', edf.loc['홍길동'].mean()) # 행 평균 

# print('median :\n', edf.median()) # 중앙값
# print('수학median :\n', edf['수학'].median()) # 중앙값

# print('max :\n',edf.max()) # 최대
# print('min :\n',edf.min()) # 최소
# print('std :\n',edf.std()) # 표준편차
# print('corr :\n',edf.corr()) # 상관계수
# print('corr :\n',edf[['수학','영어']].corr()) # 상관계수

# # 한개 행 삭제하기
# df2 = edf[:]
# print(df2)
# df2.drop('홍길동', inplace = True) # 행 제거
# print(df2)

# # 두개 행 삭제하기
# df3 = edf # 얕은 복사 객체는 동일, 이름만 추가
# df3 = edf[:] # 컬럼의 처음붙터 끝까지 정보 깊은 복사 (객체까지 생성)
# print(df3)
# df3.drop(['홍길동', '김삿갓'], inplace = True) # 행 제거
# print(df3)

# # copy로 객체 복사
# df4 = edf.copy() 
# df4.drop('홍길동', inplace=True)
# df4.drop('체육', axis = 1, inplace=True)
# print(df4) # 전혀 다른 객체이기 때문에 깊은 복사
# print(edf)

# # 두컬럼 삭제
# df5 = edf.copy() 
# df5.drop(['음악', '체육'], axis = 1, inplace = True)
# print(df5)

# # 행 선택하기
# # 열 선택하기

# # loc 인덱스 1개 iloc[인덱스의 순서]
# row1 = edf.loc['홍길동']
# print(row1)
# row2 = edf.iloc[0]
# print(row2)

# df = pd.DataFrame({'A':[1,4,7], 'B':[2,5,8], 'C':[3,6,9]})
# print(df)
# # iloc 로 행조회
# print(df.iloc[0])
# print(df.loc[0])  # 인덱스 지정안하면 똑같이 나옴

# df = pd.DataFrame(data = ([[1,4,7], [2,5,8], [3,6,9]]),
#                   index = [2, 'A', 4],
#                   columns = [51, 52, 54])
# print(df)
# # print(df.iloc[4]) # 오류
# print(df.loc[4]) # 세번째 행의 값 출력

# exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95], '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
# edf = pd.DataFrame(exam_data, index = ['홍길동', '이몽룡', '김삿갓'])

# print(edf)
# print(edf.loc[['이몽룡','김삿갓']])
# print(edf.iloc[[1,2]])

# print(edf)
# print(edf.loc['이몽룡':'김삿갓'])
# print(edf.iloc[1:3]) # 범위는 하나의 숫자

# math1 =  edf['수학']
# print(math1)
# print(type(math1))

# eng1 =  edf.영어
# print(eng1)
# print(type(eng1))

# mu_gy =  edf[['음악', '체육']] # 컬럼으로
# print(mu_gy)



# 1
# import pandas as pd
# infile = "sales_2015.xlsx"
# df = pd.read_excel(infile, sheet_name = 'january_2015', index_col = None)

# row_output = []
# row_output.append( df[["Customer Name","Sale Amount"]])

# filtered_row = pd.concat(row_output, axis = 0, ignore_index= True)
# writer = pd.ExcelWriter('sales_2015_amt.xlsx', engine='openpyxl')
# filtered_row.to_excel(writer, sheet_name='sale_2015_amt', index =False)
# writer.save()
# writer.close()

#2
import pandas as pd
infile = "sales_2015.xlsx"
df = pd.read_excel(infile, sheet_name = None, index_col = None)

row_output = []
for worksheet_name, data in df.items():
    print("===", worksheet_name, "===")
row_output.append(data[["Customer Name","Sale Amount"]])

filtered_row = pd.concat(row_output, axis = 0, ignore_index= True)
writer = pd.ExcelWriter('sales_2015_allamt.xlsx', engine='openpyxl')
filtered_row.to_excel(writer, sheet_name='sale_2015_allamt', index =False)
writer.save()
writer.close()












