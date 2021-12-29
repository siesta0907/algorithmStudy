#1010 다리 놓기

import sys

result = []
res = 1
T = int(sys.stdin.readline())

for t in range(T):
    N, M = map(int,sys.stdin.readline().split())
    for n in range (1, N+1):
        res = res * M
        res = res / n
        M = M -1
    result.append(res)
    res = 1

for r in result:
    print(int(r))
