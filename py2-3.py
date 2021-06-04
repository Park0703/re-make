def solution(bridge_length, weight, truck_weight) :
    answer = 0
    sum_weight = 0
    permission = 0
    # 0 넣기
    position = []
    for r in range(0, len(truck_weight)) :
        position.append(0)
    # print(position)

    # 무게 검열 및 차량이동 
    for i in range(0, len(truck_weight) + bridge_length) : # 차량 한대를 처음 부터 끝까지 건너기
    #     if sum(tr_we) < we :
    #         continue
        # 여기에 몇대까지 보낼건지 제한 둬야 함. 0 ~ 허용대수sum
        # if
        def check(depth) :
            if depth + 1 == len(truck_weight) : # 마지막 까지 탐색했는데 
                
                break # 마무리 동작할게
            
            for k in range(0, len(truck_weight))
                if truck_weight[k] > weight : # 11 > 10
                    continue # 0이면 1로 패스
                else : # 10, 9 <= 10 이면
                    if
                    sum_weight += truck_weight[k] # 까지 더한다
            
            check(depth + 1)
            
        for j in range(0, len(truck_weight)) : # 각 차량 이동 // 모든 자리를 더해준다.
            # if  # 조건에 부합하는 트럭만 이동할 수 있다.
            
            # if total : # total_weight < weight: 인 조합만 가능
            #     continue
            
            if bridge_length > position[j] :  # 총길이보다 작으면 해당 위치
                position[j] += 1
                print(position) # 각 트럭의 현위치
        # 턴이 넘어가면 제거하고  // 파이썬 for문 특성상 본리스트 회손하면 안돌아감          
        # if position[0] == bridge_length :
        #     position.pop(0)
        

        answer += 1 # return 완벽
    print(truck_weight)    
    print(answer)
    return answer
  



solution(2, 10, [ 7, 4, 5, 6 ]) # 8
# solution(100, 100, [ 10 ]) # 101
# solution(100, 100, [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]) # 110
# 트럭이 1차선 다리를 건너는 시간은?
# 1초에 1만큼, 트럭이 다리에 완전히 올라야 무게 고려
# 1) 
