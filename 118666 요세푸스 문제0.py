#11866 요세푸스 문제0

import sys

N, k = map(int, sys.stdin.readline().split())
nums = []
res = []
for i in range(1, N+1):
    nums.append(i)

i = 1
p = 0

while nums:
    if p == len(nums): p = 0  
    if i == k:
        res.append(nums.pop(p))
        i = 1
    else:
        i += 1
        p += 1  

print("<", end = '')
for i in range(N-1):
    print(res[i], end = ', ')

print(res[-1] , end = ">")
