def solution(n):
    answer = 0
    print(sum([int(i) for i in str(n)]))

    return answer
  
solution(123) # 6 1+2+3
solution(987) # 24 9+8+7

# 1풀이 split '+'join
# 2풀이 list(map(int, reversed(str(n))))