#11050 이항 계수1

import sys

def factorial (n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

n , k = map(int, sys.stdin.readline().split())

print(int(factorial(n)/factorial(n-k)/factorial(k)))
