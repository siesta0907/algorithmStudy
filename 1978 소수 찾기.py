#1978 소수 찾기

import math

N = int(input())
numbers = input().split()
count = 0 

for i in range(0, N):
    num = int(numbers[i])
    s = math.ceil(math.sqrt(num))
    if(num == 1): continue
    if(num == 2):
        count +=1
        continue

    for j in range (2, s+1 ):
        if (num % j == 0): break
        elif j == s:
            count +=1
print(count)
            
        
