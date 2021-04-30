def solution(num):
    answer = 0
    # 1 => 짝수 //2 => 홀수 *3+1  , 500이상이면 -1
    for i in range(0, 8000001) :
        if num != 1 : # num이 1이면 멈추기
            break
        else : # num이 1이 아니면
            if num%2 == 0 : # 짝수라면
                num = num//2
                answer += 1
            else : #홀수라면
                num = num*3 + 1
                answer += 1
    if answer > 500 :
        answer = -1     
    print(answer)      
    return answer
  
  
solution(6) # 8
solution(16) # 4
solution(626331) # 500번 이상이면 -1

# def solution(num):
#     answer = 0
#     for i in range(0, 8000001) :
#         if num != 1 : 
#             if num%2 == 0 :
#                 num = num//2
#                 answer += 1
#             else : 
#                 num = num*3 + 1
#                 answer += 1
#     if answer > 500 :
#         answer = -1          
#     return answer