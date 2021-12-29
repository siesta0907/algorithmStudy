# 2908 상수

import sys

A, B =sys.stdin.readline().split()
reverA = ""
reverB = ""
for i in range(1, len(A)+1):
    reverA += A[-i]
for i in range(1, len(B)+1):
    reverB += B[-i]

if int(reverA) < int(reverB):
    print(reverB)
else: print(reverA)
    
