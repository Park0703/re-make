
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
import cx_Oracle
# conn = cx_Oracle.connect('kic', '1234', 'localhost/xe')
# conn = cx_Oracle.connect('kic', '1234', '192.168.0.52/xe')
# 오라클서버 ip주소 cmd에서 ipconfig로 확인
# localhost : 내컴퓨터,
# conn = cx_Oracle.connect('user', 'user p.w', '오라클서버/ip주소')
# 오라클 로컬호스트 서버 접속
# xe 오라클 서버아이디 sid :xe
# localhost .. 1521 sid: xe
# cur = conn.cursor()
# cur.execute("select * from student")
# st_list = cur.fetchall()
# for st in st_list:
#     print(st)

# csv 파일읽기 => 복사하기
# 파이썬에서 명령문에서 데이터 입력받기

# with open("jeju1.csv", "r", newline='', encoding='utf8') \
#         as infp:
#     with open('jeju1_bak.csv', 'w', encoding='utf8') as outfp:
#         header = infp.readline()
#         print(header)
#         header = header.strip()
#         header_list = header.split(',')
#         outfp.write(','.join(map(str, header_list))+'\r\n')
#         for row in infp:
#             outfp.write(row)

print("     abc      ".strip())
