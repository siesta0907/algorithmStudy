# 2193번 이친수
# Dp문제

memo = [0]*100
memo[1] = 1
memo[2] = 1

def DP (n) :
    if memo[n] > 0:
        return memo[n];
    memo[n] = DP(n-1) + DP(n-2)
    return memo[n]

n = int(input())
res = DP(n)
print(res)
