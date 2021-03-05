def solution(arr):
    answer = []
    i = 0
    for num in arr : # for ,계수 상승
        if arr[i:i+1] != arr[i+1:i+2] : # 현재와 +1이 같을 때
            answer.append(arr[i]) #ard
            # continue
        i += 1
    print(i)
    print(answer)
    return answer
            
  

solution([1,1,3,3,0,1,1]) # 1,3,0,1
# arr(4,4,4,3,3)     # 4, 3