def fibo(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1

    return fibo(n-1) + fibo(n-2)

# fibo (5)
# print(fibo (8))
def sol(n) :    
    dp = []
    for i in range(0, n+1) :
        dp.append(False)
    dp[0] = 1
    dp[1] = 1    
    def fibo(n) :
        if dp[n] :
            return dp[n]
        dp[n] = fibo(n-1) + fibo(n-2)
        
        return dp[n]
    print(fibo(n))    
    print(dp)
# sol(5)    
# dp = []
# for i in range(0, 3) :
#     dp.append(False)
# dp[1] = 1
# print(dp)
# solution(10)
# 0 1 2 3 4 5 6 7  8  9  10 n
# 0 1 1 2 3 5 8 13 21 34 55 
