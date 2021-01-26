#IF 분기-상황별 코드
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈" : # 최초조건
    print("우산을 챙기세요.")
elif weather == "미세먼지" : # 다음조건
    print("마스크를 챙기세요.")
else :                          # 그 무엇도 아니면
    print("준비물 필요없어요.")

#정수표현
temp = int(input("기온은 어때요?"))
if 30 <= temp :
    print("날씨가 너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10 :
    print("외투를 챙기세요.")
else :
    print("너무 추워요. 나가지 마세요.")
  
#for 반복문
print("대기번호 : 1")
print("대기번호 : 1")
print("대기번호 : 1")
print("대기번호 : 1")




















