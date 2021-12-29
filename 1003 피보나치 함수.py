#1003 피보나치 함수
import sys

def fibonacci (n):
    if n == 0: return 0 
    elif n == 1: return 1
    else: fibonacci(n-1) + fibonacci(n-2)

T = int(sys.stdin.readline())
case = []

for i in range(T):
    t = int(sys.stdin.readline())
    case.append(t)
    
for c in case:
    x, y = fibonacci(c)
    

