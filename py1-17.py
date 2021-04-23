def solution(x, n):
    answer = []
    a = x
    for i in range(0, n) : 
        answer.append(x)
        x += a
    print(answer)
    return answer

solution(2, 5) #[2,4,6,8,10]
solution(4, 3) #[4,8,12]
solution(-4, 2)#[-4,-8]

# x부터 x씩 증가해 n개 리턴