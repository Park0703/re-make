def solution(arr) :
    # 난쟁이 수가 7명이 아닌 9명일 때 가짜 난쟁이 2명을 걸러내는 방법 = 일곱난장이의 키의 합이 100
    # 그들을 찾고 모든 경우의 수를 출력하며, 오름차순
    answer = []
    case = arr
    for i in case :
        for j in case :
            # 제거는 replace(i, 0), remove(i)
            # arr.remove(i).remove(j)
            case.replace(i, 0)
            case.replace(j, 0)
            
            if sum(case) == 100 :
                answer = case.sort()
                print(answer)
                break # 찾았으니 종결 중복은 엿먹어라
              
            case = arr # 못찾으면 되돌리기
            
            # 뭐가 되었든 다음 확인을 위해 연산끝나면 원래 arr로 돌려놔야 함  
                
    # 하나하나 넣어서 조합을 만드는 것은 너무 연산을 많이 소모하니, 채워 넣고 2개를 빼는 방법을 쓰자
    # n**2 이면 해결
      
    
    
    
    
    
    
    
solution([20, 7, 23, 19, 10, 15, 25, 8, 13])
solution([15, 7, 23, 36, 8, 15, 12, 27, 2])