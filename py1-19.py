def solution(n):
    answer = 0
    a = []
    b = n
    while(b != 0) : 
        a.append(str(b%10))
        b = b//10
    a.sort()
    a.reverse()
    print(int("".join(a)))
    return answer

solution(118372) # 873211 정렬하고 리버스하고 합치기