def solution(prg, spd):
    answer = []
    score = 0    
    day = 0
    for i in range(1, 100) :
        day += 1 # day count
        print('1) 날짜 :', day)

        for j in range(0, len(prg)) : # prg, spd
            # 순서대로 100인지 체크하고 100이면 빼기
            print('  2) j :', j) 
            
            # 다행인건 검색은 알아서 처음부터 시작해서 굳이 k = 0을 만들어줄 필요가 없다.
            k = 0
            for l in range(0, len(spd)+1) : # 해당 인덱스가 100 보다 큰지 확인하고 크면 제거하고 스코어 상승
                print('     3) k :', k)
                if prg[k] >= 100 :
                    
                    prg.pop(k)
                    spd.pop(k)
                    print('      자폭', prg, 'k:', k)
                    score += 1 # 순차적으로 조건을 검색했고 한번 뚫리면 끝까지 뚤어야 한다.
                    print(score, 'score')
                    
                    # k = k - 1 # 소용없다 왜냐하면 for문에서 순간 절대적으로 넘어가기 때문
                else : # 0idx부터 시작하는 지수가 100보다 작으면 넘어간다
                    print('      break', prg, 'k', k)
                    # k += 1
                    break    # 브레이크 하니까깐 통으로 넘어간다   
                
            if score > 0 :
                answer.append(score)
                score = 0
                print('@answer :', answer)
                j = 0
                # 점수를 초기화했는데 
                # j = 0   
            # 100이 아니라면 PRG 100만들기
            # if j > k :
            #     j = 0
            if prg[j] < 100 : # j == 1 len(prg) == 2
                prg[j] += spd[j] # 저기로 넣으면 순서대로 검색해서 제거후 변화하는 전체 인덱스에 차질이 생김

                # j ==2 검색하는 문제? 줄어든 만큼만 해야하는게 아닌가?
                
        print('------------------------------ prg :', prg)
        if len(prg) == 0 : # 완전히 다 돌아서없으면 다시변경해야함 len(prg) == 0
            break
    return answer

# solution([95], [4]) # 2
solution([93, 30, 55], [1, 30, 5]) # [2, 1]
# solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) # [1, 3, 2]


# prg 100미만, spd 100미만
# 매 하루당 몇개의 기능이 배포되는지?
# 하루 한번 배포, 하루 끝에, 진도율이 95퍼, 속도가 4%이면, 배포는 2일 뒤 