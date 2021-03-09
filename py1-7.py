def solution(arr, div):
    answer = []
    arr.sort()
    # arr fmf divi로 나누어 떨어지면
    for i in arr :
        if i%div == 0 :
            answer.append(i)
    return answer
  
  
  
  
  
solution( [5, 9, 7, 10], 5 )
solution( [2, 36, 1, 3], 1 )
solution( [3, 2, 6], 10 )