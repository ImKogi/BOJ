"""def a(k,n):
    if k == 0:
        return n
    elif n == 1:
        return 1
    return a((k-1),n) + a(k,(n-1))
"""
# 동적 계획법

def fm(k,n):
    dp = [[0]*(n+1) for _ in range(k+1)]

    for i in range(1,n+1):
        dp[0][i] = i
    
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[k][n]

ts = int(input())

for _ in range(ts):
    k = int(input())
    n = int(input())
    print(fm(k,n))