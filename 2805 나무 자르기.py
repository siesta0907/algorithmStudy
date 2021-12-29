#2805 나무 자르기

import sys

N, M = map (int, sys.stdin.readline().split())
heights = list(map (int, sys.stdin.readline().split()))
res = 0
H = 0

while res < M:
    for h in heights:
        res = h - H
