# 1712 손익분기점

import math

s = input().split()
A = int(s[0])
B = int(s[1])
C = int(s[2])

i = 0

if B >= C: print(-1)

else:
    if(A/(C-B) == math.ceil(A/(C-B))):
        print(int(A/(C-B))+1)
    else:
        print(int(math.ceil(A/(C-B))))
