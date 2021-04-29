def solution(arr):
    answer = []
    # 가장 작은 배열 제거
    
    arr.remove(min(arr))
    answer = arr
    # answer = arr.remove(min(arr))
    # 빈 배열일 대 -1 리턴 
    if answer == [] :
        answer.append(-1)
    print(answer)
    return answer
  
solution([4,3,2,1]) # [4,3,2]
solution([10]) # [-1]