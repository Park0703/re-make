def solution(n):
    answer = 0
    for i in range(1, n + 1) : 
        if n%i == 0 : # 나머지 0
            answer += i
    #로직 약수를 더한다 = 약수를 어떻게 구하지?
    # 1 for i in 0~n : if n%i == 0 : answer += i  = 처음부터끝까지 나눠보고 나눠지면 더하기
    # 나눠서
    # 2 
    # 곱해서 값이 나오면 특성상 nxi가 되어야해서 n문이 됨
    print(answer)
    return answer



solution(12)
solution(5)