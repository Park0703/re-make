#Chapter03-2
#문자형
#문자열 생성
str1 = "im python"
str2 = "python"
str3 = """how are you?"""
str4 = '''thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))      

#빈 문자열 - 따옴표만 해놓으면 빈 문자열 생성
str1_t1 = ''
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자사용
# i'm boy '를 쓰는 경우 ""를 사용하기 혹은 복잡해지면 이스케이프 역슬러시
print("I'\''m boy")
print('a \ b ')

#탭, 줄바꿈
t_s1 = "click \t start!"
t_s2 = "new line \n check!"

print(t_s1)
print(t_s2)
print()

# raw string - escape의 반대 : \를 무시함
raw_s1 = r'D:\python\test'
print(raw_s1)

#멀티라인 입력 - 실수많은 부분 역슬러시로 멀티라인 표시가능
multi_str = \
"""fdsafdsafjdlahfjdksahjfewqhi
\ epvquifewhvfdsbhvjvlhjkvhxjkclhvaafdfdafdaf
\ dsafdsafjkqlhjfewqhdhjjasdjfdhjtoooohtttsdsadsafsd"""
# \ 는 변수 바인딩을 암시함
print(multi_str)

#문자열 연산
str_01 = "python"
str_02 = "Apple"
str_03 = "How are you doing"
str_04 = "seoul! Deajeon! busan! jinju!"

#데이터와 관련
print(str_01*3)
print(str_01 + str_02)
print('y' in str_01) # y가 포함되어 있습니까? true
print('z' in str_01)
print('P' not in str_02) # 대소문자를 구분함, not 활용

#문자열 형변환
print(str(66),type(str(66)))
print(str(10.1))
print(str('true'), type(str('true')))

#문자열함수(upper, isalnum, startwith, count, endswith, isalpha)
print("Capitalize: ", str_01.capitalize())
print("endswith?: ",str_02.endswith("!"))
print("replace", str_01.replace("thon", " good"))
print("sorted: ", sorted(str_01))
print("split:", str_04.split('!'))
    
# 반복(시퀀스)
im_str = "good boy!"
print(dir(im_str))
#___iter___ - 시퀀스 반복 가능
for i in im_str:
    print(i)

#★ 슬라이싱
str_s1 = "nice python"


# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2 가 나옴 
print(str_s1[5:11]) #_부터 : _글자 // [4:]4번째부터 끝까지
print(str_s1[:len(str_s1)]) #str_s1(:11)과 동일, 끝을 모르면 비우거나 len이용
print(str_s1[:len(str_s1)-1]) #str_s1(:11)과 동일
print(str_s1[1:9:2]) #3번째는 2개 단위 스킵인지
print(str_s1[-5:]) # 음수가 들어가면
print(str_s1[1:-2])
print(str_s1[::2]) 
print(str_s1[::-1]) # 역방향 출력

#아스키 코드 - 코드표를 보고 문자를 보고 처리해서 우리에게 보여줌
a = 'z'
print(ord(a)) #아스키코드로 찾아줌
print(chr(122)) #아스키 코드를 문자로 역으로 보여줌







