#2775 부녀회장이 될테야
import sys
a = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]

def apart():
  for i in range(1, 15):
    b = [1]
    for n in range(1, 14):
      b.append(b[n - 1] + a[i - 1][n])
    a.append(b)

apart()

result = []

T = int(sys.stdin.readline())

for t in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    result.append(a[k][n-1])
    
for r in result:
    print(r)









# 재귀함수로 풀었는데 시간초과가 뜸
"""import sys

result = []
memo = [[0 for i in range(15)] for j in range(15)]
for i in range (15):
    memo[0][i] = i

def recursive (floor, num):
    res = 0
    if memo[floor][num] != 0:
        return memo[floor][num]
    else:
        for n in range(1, num+1):
            res += recursive(floor-1, n)
        return res 

T = int(sys.stdin.readline())
for t in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    result.append(recursive(k,n))
for r in result:
    print(r)
"""
