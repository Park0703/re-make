#파일입출력
score_file = open("score.txt", "a", encoding="utf8") 
#w #a 업핸드 #r리드
score_file.write("코딩: 100")
print("수학 : 0", file=score_file)
print("영어 : 0", file=score_file)
score_file.close() #닫아줘야함


#PICKLE 프로그램상데이터를 파일을 저장하고 유통 

import pickle
'''
profile_file = open("profile.pickle", "wb")
profile = {"이름" : "박명수", "나이" : 30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file()
'''

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

#with
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) #통해서 출력함 // 자동으로 탈출하면서 종료시켜줌

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
            report_file.write("-{0}주차 주간보고-".format(i))
            report_file.write("\n부서 : ")
            report_file.write("\n이름 : ")
            report_file.write("\n업무요약 : ")










