#1463 1로만들기

import sys

num = int(sys.stdin.readline())
count = 0

while num > 1:
    if num % 3 == 0:
        num = num / 3 
        count += 1
        
    elif num %2 == 0:
        num = num / 2
        count += 1
    else:
        num -= 1
        count += 1

print(count)
