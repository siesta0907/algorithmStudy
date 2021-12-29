#1920 수 찾기

import sys

N = sys.stdin.readline()
A = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)



#이분탐색으로 풀었는데 런타임에러로 안됨            
"""
import sys

res = []

N = sys.stdin.readline()
A = list(set(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

for b in B:
    front = A[0]
    back = A[-1]
    
    while True:
        m = A[(A.index(front)+A.index(back))//2]
        if b == m:
            res.append(1)
            break
        elif front == back:
            res.append(0)
            break
        elif b < m:
            back = m-1
        elif b > m:
            front = m+1
            
for r in res:
    print(r)

"""
