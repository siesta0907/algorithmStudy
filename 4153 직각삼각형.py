#4153 직각삼각형

import sys

res = []

while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0: break
    if a > b and a > c:
        if a**2 == b**2 + c**2: res.append("right")
        else: res.append("wrong")
    elif b > a and b > c:
        if b**2 == a**2 + c**2: res.append("right")
        else: res.append("wrong")
    elif c > a and c > b:
        if c**2 == b**2 + a**2: res.append("right")
        else: res.append("wrong")
    else:
        res.append("wrong")

for r in res: print(r)
