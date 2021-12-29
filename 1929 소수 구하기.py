#1929 소수 구하기

import sys
import math

def PrimeNum(num):
    if num == 1: return False
    for n in range(2, int(math.sqrt(num))+1):
        if num % n == 0: return False
    return True

res = []
M, N = map(int, sys.stdin.readline().split())

for i in range (M, N+1):
    if PrimeNum(i): res.append(i)
        
for r in res: print(r)
